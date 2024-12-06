import logging

import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

from denvr.config import Config
from denvr.utils import snakecase

logger = logging.getLogger(__name__)


class Session:
    """
    Session(config: Config)

    Handles authentication and HTTP requests to Denvr's API.
    """

    def __init__(self, config: Config):
        self.config = config
        self.session = requests.Session()

        # Set the auth, header and retry strategy for the session object
        self.session.auth = self.config.auth
        self.session.headers.update({"Content-Type": "application/json"})
        self.session.mount(
            self.config.server,
            HTTPAdapter(
                max_retries=Retry(
                    total=self.config.retries,
                    # TODO: Consider making these configurable in the future?
                    backoff_factor=0.1,
                    status_forcelist=(408, 425, 429, 500, 502, 503, 504),
                    allowed_methods={"GET", "PUT", "POST", "DELETE"},
                )
            ),
        )

    def request(self, method, path, **kwargs):
        url = "/".join([self.config.server, *filter(None, path.split("/"))])
        logger.debug("Request: self.session.request(%s, %s, **%s", method, url, kwargs)
        resp = self.session.request(method, url, **kwargs)
        resp.raise_for_status()
        result = resp.json()
        logger.debug("Response: resp.json() -> %s", result)
        # According to the spec we should just be return result and not {"result": result }?
        # For mock-server testing purposes we'll support both.
        result = result.get("result", result) if isinstance(result, dict) else result
        # Standardize the response keys to snakecase if it's a dict'
        if isinstance(result, dict):
            return {snakecase(k): v for k, v in result.items()}

        return result

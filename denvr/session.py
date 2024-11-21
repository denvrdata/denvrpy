import copy
import os

import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

from denvr.config import Config


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
        url = os.path.join(self.config.server, os.path.splitroot(path)[-1])
        resp = self.session.request(method,url, **_filter_none(kwargs))
        resp.raise_for_status()
        result = resp.json()
        # According to the spec we should just be return result and not {"result": result }?
        # For mock-server testing purposes we'll support both.
        return result.get("result", result) if isinstance(result, dict) else result


def _filter_none(kwargs):
    """
    A utility function to remove None param or json payload values.
    We also provide debug logging to track when these are removed.
    """
    result = {}
    for (kw, args) in kwargs.items():
        result[kw] = {}
        for (k, v) in args.items():
            if v is None:
                # print("Dropping missing argument {}".format(k))
                continue
            else:
                result[kw][k] = v

    return result

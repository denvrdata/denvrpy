import os

import requests

from denvr.config import Config


class Session:
    """
    Session(config: Config)

    Handles authentication and HTTP requests to Denvr's API.
    """

    def __init__(self, config: Config):
        self.config = config

    def request(self, method, path, **kwargs):
        url = os.path.join(self.config.server, os.path.splitroot(path)[-1])
        kwargs["headers"] = {"Content-Type": "application/json"}
        kwargs["auth"] = self.config.auth
        resp = requests.request(method, url, **kwargs)
        resp.raise_for_status()
        return resp.json()["result"]

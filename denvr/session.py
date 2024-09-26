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

    def request(self, method, path, params=None, json=None):
        url = os.path.join(self.config.server, os.path.splitroot(path)[-1])
        kwargs = {
            "headers": {"Content-Type": "application/json"},
            "auth": self.config.auth,
        }

        # TODO: Fill missing params with potential defaults.
        # TODO: Something is wrong with the auth kwarg right now.
        if method == "get":
            response = requests.get(url, params=params, **kwargs)
        elif method == "post":
            response = requests.post(url, params=params, json=json, **kwargs)
        elif method == "delete":
            response = requests.delete(url, params=params, json=json, **kwargs)
        else:
            raise Exception(f"HTTP method {method} is not yet supported.")

        response.raise_for_status()
        return response.json()["result"]

import time

import requests
from requests.auth import AuthBase


class Auth(AuthBase):
    """
    Auth(server, username, password)

    Handles authorization, renewal and logouts given a
    username and password.
    """

    def __init__(self, server, username, password):
        # Requests an initial authorization token
        # storing the username, password, token / refresh tokens and when they expire
        resp = requests.post(
            f"{server}/api/TokenAuth/Authenticate",
            headers={"Content-type": "application/json"},
            json={"userNameOrEmailAddress": username, "password": password},
        )
        resp.raise_for_status()
        content = resp.json()["result"]

        self._server = server
        self._access_token = content["accessToken"]
        self._refresh_token = content["refreshToken"]
        self._access_expires = time.time() + content["expireInSeconds"]
        self._refresh_expires = time.time() + content["refreshTokenExpireInSeconds"]

    @property
    def token(self):
        if time.time() > self._refresh_expires:
            raise Exception("Auth refresh token has expired. Unable to refresh access token.")

        if time.time() > self._access_expires:
            resp = requests.get(
                f"{self._server}/api/TokenAuth/RefreshToken",
                params={"refreshToken": self._refresh_token},
            )
            resp.raise_for_status()
            content = resp.json()["result"]
            self._access_token = content["accessToken"]
            self._access_expires = time.time() + content["expireInSeconds"]

        return self._access_token

    def __call__(self, request):
        request.headers["Authorization"] = "Bearer " + self.token
        return request

    def __del__(self):
        # TODO: Add a logout request on auth object deletion
        pass

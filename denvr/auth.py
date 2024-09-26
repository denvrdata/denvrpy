import os
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
        response = requests.post(
            os.path.join(server, "api", "TokenAuth", "Authenticate"),
            headers={"Content-type": "application/json"},
            json={"userNameOrEmailAddress": username, "password": password},
        )

        # Just let requests raise an HTTPError if one occured
        response.raise_for_status()
        content = response.json()["result"]
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
            response = requests.get(
                os.path.join(self._server, "api", "TokenAuth", "RefreshToken"),
                params={"refreshToken": self._refresh_token},
            )
            response.raise_for_status()
            content = response.json()["result"]
            self._access_token = content["accessToken"]
            self._access_expires = time.time() + content["expireInSeconds"]

        return self._access_token

    def __call__(self, request):
        request.headers["Authorization"] = "Bearer " + self.token
        return request

    def __del__(self):
        # TODO: Add a logout request on auth object deletion
        pass

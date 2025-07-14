import time

import requests
from requests.adapters import HTTPAdapter
from requests.auth import AuthBase

from denvr.utils import retry


class Auth(AuthBase):
    """
    Auth(server, username, password)

    Handles authorization, renewal and logouts given a
    username and password.
    """

    def __init__(self, server, username, password, retries=3):
        self._server = server
        self._session = requests.Session()
        self._session.headers.update({"Content-type": "application/json"})
        if retries:
            self._session.mount(
                self._server,
                HTTPAdapter(max_retries=retry(retries=retries, idempotent_only=False)),
            )

        # Requests an initial authorization token
        # storing the username, password, token / refresh tokens and when they expire
        resp = self._session.post(
            f"{self._server}/api/TokenAuth/Authenticate",
            json={"userNameOrEmailAddress": username, "password": password},
        )
        resp.raise_for_status()
        content = resp.json()["result"]
        self._access_token = content["accessToken"]
        self._refresh_token = content["refreshToken"]
        self._access_expires = time.time() + content["expireInSeconds"]
        self._refresh_expires = time.time() + content["refreshTokenExpireInSeconds"]

    @property
    def token(self):
        if time.time() > self._refresh_expires:
            raise Exception("Auth refresh token has expired. Unable to refresh access token.")

        if time.time() > self._access_expires:
            resp = self._session.get(
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

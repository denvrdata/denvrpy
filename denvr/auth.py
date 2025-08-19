import os
import time
import requests

from requests.adapters import HTTPAdapter
from requests.auth import AuthBase

from denvr.utils import retry


def auth(src: str, credentials: dict, server: str, retries: int) -> AuthBase:
    """
    auth(src, credentials, server, retries)

    A simply auth factory function which determines the correct Auth type to use.

    Args:
        src: Filepath for the credentials config
        credentials: Lookup dict for apikey, username and/or password
        server: Server to authenticate against for bearer auth
        retries: Retry attempts for requests using bearer auth

    Priority:
    - Environment variables take precedence over configuration files.
    - DENVR_APIKEY / apikey takes precedence over DENVR_USERNAME / username and DENVR_PASSWORD / password.

    NOTE:
        We're intentionally letting the loaded username/password go out of scope for security reasons.
        The auth object should be able to handle everything from here onward.
    """
    apikey = os.getenv("DENVR_APIKEY", credentials.get("apikey", ""))
    if apikey:
        return ApiKey(apikey)

    username = os.getenv("DENVR_USERNAME", credentials.get("username", ""))
    if not username:
        raise Exception(f"Could not find username in 'DENVR_USERNAME' or {src}")

    password = os.getenv("DENVR_PASSWORD", credentials.get("password", ""))
    if not password:
        raise Exception(f"Could not find password in 'DENVR_PASSWORD' or {src}")

    return Bearer(server, username, password)


class ApiKey(AuthBase):
    """
    ApiKey(key)

    Simply wraps the provied key and injects the header into requests.
    """

    def __init__(self, key):
        self._key = key

    def __call__(self, request):
        request.headers["Authorization"] = f"ApiKey {self._key}"
        return request


class Bearer(AuthBase):
    """
    Bearer(server, username, password)

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
        request.headers["Authorization"] = f"Bearer {self.token}"
        return request

    def __del__(self):
        # TODO: Add a logout request on auth object deletion
        pass

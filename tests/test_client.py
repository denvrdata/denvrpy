from pytest_httpserver import HTTPServer

from denvr.client import client


def test_client(httpserver: HTTPServer):
    httpserver.expect_request(
        "/api/TokenAuth/Authenticate",
        method="post",
        json={
            "userNameOrEmailAddress": "alice@denvrtest.com",
            "password": "alice.is.the.best",
        },
    ).respond_with_json(
        {
            "result": {
                "accessToken": "access1",
                "refreshToken": "refresh",
                "expireInSeconds": 60,
                "refreshTokenExpireInSeconds": 3600,
            },
        },
    )

    virtual = client("servers/virtual")
    assert type(virtual).__name__ == "Client"

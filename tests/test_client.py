import sys
import tempfile

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

    content = """
    [defaults]
    server = "{}"
    api = "v2"
    cluster = "Hou1"
    tenant = "denvr"
    vpcid = "denvr"
    rpool = "reserved-denvr"
    retries = 5

    [credentials]
    username = "alice@denvrtest.com"
    password = "alice.is.the.best"
    """.format(httpserver.url_for("/"))
    kwargs = {"delete_on_close": False} if sys.version_info >= (3, 12) else {"delete": False}
    with tempfile.NamedTemporaryFile(**kwargs) as fp:
        fp.write(content.encode())
        fp.close()

        virtual = client("servers/virtual")
        assert type(virtual).__name__ == "Client"

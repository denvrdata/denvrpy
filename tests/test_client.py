import os
import sys
import tempfile

from pytest_httpserver import HTTPServer

from denvr.client import client
from tests.utils import temp_env


def test_client(httpserver: HTTPServer):
    httpserver.expect_request(
        "/api/TokenAuth/Authenticate",
        method="post",
        json={"userNameOrEmailAddress": "alice@denvrtest.com", "password": "alice.is.the.best"},
    ).respond_with_json(
        {
            "result": {
                "accessToken": "access1",
                "refreshToken": "refresh",
                "expireInSeconds": 60,
                "refreshTokenExpireInSeconds": 3600,
            }
        }
    )

    content = """
    [defaults]
    server = "{}"
    """.format(httpserver.url_for("/"))
    kwargs = {"delete_on_close": False} if sys.version_info >= (3, 12) else {"delete": False}
    with tempfile.NamedTemporaryFile(**kwargs) as fp:  # type: ignore
        fp.write(content.encode())
        fp.close()

        with temp_env():
            os.environ["DENVR_CONFIG"] = fp.name
            os.environ["DENVR_USERNAME"] = "alice@denvrtest.com"
            os.environ["DENVR_PASSWORD"] = "alice.is.the.best"

            virtual = client("servers/virtual")
            assert type(virtual).__name__ == "Client"

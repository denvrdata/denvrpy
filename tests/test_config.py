# We just need to mock the Auth object
import os
import sys
import tempfile
from unittest.mock import Mock, patch

import pytest

from denvr.config import config
from tests.utils import temp_env


@patch("requests.post")
def test_config(mock_post):
    mock_post.return_value = Mock(
        raise_for_status=lambda: None,
        json=lambda: {
            "result": {
                "accessToken": "access1",
                "refreshToken": "refresh",
                "expireInSeconds": 60,
                "refreshTokenExpireInSeconds": 3600,
            }
        },
    )

    # Realistic config file
    content = """
    [defaults]
    server = "https://api.cloud.denvrdata.com"
    api = "v2"
    cluster = "Hou1"
    tenant = "denvr"
    vpcid = "denvr"
    rpool = "reserved-denvr"
    retries = 5

    [credentials]
    username = "test@foobar.com"
    password = "test.foo.bar.baz"
    """
    kwargs = {"delete_on_close": False} if sys.version_info >= (3, 12) else {"delete": False}
    with tempfile.NamedTemporaryFile(**kwargs) as fp:  # type: ignore
        fp.write(content.encode())
        fp.close()

        conf = config(path=fp.name)

        assert conf.auth._access_token == "access1"
        assert conf.auth._refresh_token == "refresh"
        assert conf.server == "https://api.cloud.denvrdata.com"
        assert conf.api == "v2"
        assert conf.cluster == "Hou1"
        assert conf.tenant == "denvr"
        assert conf.vpcid == "denvr"
        assert conf.rpool == "reserved-denvr"
        assert conf.retries == 5

    # Test with no config file and just auth environment variables
    with temp_env():
        os.environ["DENVR_CONFIG"] = os.path.join(os.getcwd(), "missing", "config.toml")
        os.environ["DENVR_USERNAME"] = "test@foobar.com"
        os.environ["DENVR_PASSWORD"] = "test.foo.bar.baz"
        conf = config()

        assert conf.auth._access_token == "access1"
        assert conf.auth._refresh_token == "refresh"
        assert conf.server == "https://api.cloud.denvrdata.com"
        assert conf.api == "v1"
        assert conf.cluster == "Msc1"
        assert conf.tenant is None
        assert conf.vpcid is None
        assert conf.rpool == "on-demand"
        assert conf.retries == 3

    # Test with no config and just a username
    with temp_env():
        os.environ["DENVR_CONFIG"] = os.path.join(os.getcwd(), "missing", "config.toml")
        os.environ["DENVR_USERNAME"] = "test@foobar.com"
        with pytest.raises(Exception, match=r"^Could not find password in"):
            config()

    # Test no auth info
    with temp_env():
        os.environ["DENVR_CONFIG"] = os.path.join(os.getcwd(), "missing", "config.toml")
        with pytest.raises(Exception, match=r"^Could not find username in"):
            config()

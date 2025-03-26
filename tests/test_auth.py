from unittest.mock import Mock, patch

import pytest
from requests.exceptions import HTTPError

from denvr.auth import Auth


@patch("requests.get")
@patch("requests.post")
def test_auth(mock_post, mock_get):
    # Mock getting the access token
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

    auth = Auth("https://api.test.com", "alice@denvrtest.com", "alice.is.the.best")

    # Set an error case if we try to refresh the token too soon.
    mock_get.return_value = Mock(
        # A bit of a hack cause we can't raise an exception from a lambda function
        raise_for_status=lambda: (_ for _ in ()).throw(HTTPError("500 Server Error"))
    )

    r = auth(Mock(headers={}))
    assert "Authorization" in r.headers
    assert r.headers["Authorization"] == "Bearer access1"


@patch("requests.get")
@patch("requests.post")
def test_auth_refresh(mock_post, mock_get):
    # Mock getting the access token
    mock_post.return_value = Mock(
        raise_for_status=lambda: None,
        json=lambda: {
            "result": {
                "accessToken": "access1",
                "refreshToken": "refresh",
                "expireInSeconds": -1,
                "refreshTokenExpireInSeconds": 3600,
            }
        },
    )

    auth = Auth("https://api.test.com", "alice@denvrtest.com", "alice.is.the.best")

    # Mock the get function to return a new access token
    mock_get.return_value = Mock(
        raise_for_status=lambda: None,
        json=lambda: {"result": {"accessToken": "access2", "expireInSeconds": 30}},
    )

    r = auth(Mock(headers={}))
    assert "Authorization" in r.headers
    assert r.headers["Authorization"] == "Bearer access2"


@patch("requests.post")
def test_auth_expired(mock_post):
    # Mock getting the access token
    mock_post.return_value = Mock(
        raise_for_status=lambda: None,
        json=lambda: {
            "result": {
                "accessToken": "access1",
                "refreshToken": "refresh",
                "expireInSeconds": -1,
                "refreshTokenExpireInSeconds": -1,
            }
        },
    )

    auth = Auth("https://api.test.com", "alice@denvrtest.com", "alice.is.the.best")

    # Test error when the refresh token is too old.
    with pytest.raises(Exception, match=r"^Auth refresh token has expired.*"):
        auth(Mock(headers={}))

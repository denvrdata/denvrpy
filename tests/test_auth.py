from unittest.mock import Mock, patch

import pytest
from requests.exceptions import HTTPError

from denvr.auth import Auth


@patch("requests.Session")
def test_auth(mock_session_class):
    # Create a mock session instance
    mock_session = Mock()
    mock_session_class.return_value = mock_session

    # Mock the post method (for initial authentication)
    mock_session.post.return_value = Mock(
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

    # Mock the get method (for token refresh)
    mock_session.get.return_value = Mock(
        # A bit of a hack cause we can't raise an exception from a lambda function
        raise_for_status=lambda: (_ for _ in ()).throw(HTTPError("500 Server Error"))
    )

    auth = Auth("https://api.test.com", "alice@denvrtest.com", "alice.is.the.best", 0)

    r = auth(Mock(headers={}))
    assert "Authorization" in r.headers
    assert r.headers["Authorization"] == "Bearer access1"


@patch("requests.Session")
def test_auth_refresh(mock_session_class):
    # Create a mock session instance
    mock_session = Mock()
    mock_session_class.return_value = mock_session

    # Mock the post method (for initial authentication)
    mock_session.post.return_value = Mock(
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

    # Mock the get method (for token refresh)
    mock_session.get.return_value = Mock(
        raise_for_status=lambda: None,
        json=lambda: {"result": {"accessToken": "access2", "expireInSeconds": 30}},
    )

    auth = Auth("https://api.test.com", "alice@denvrtest.com", "alice.is.the.best", 0)

    r = auth(Mock(headers={}))
    assert "Authorization" in r.headers
    assert r.headers["Authorization"] == "Bearer access2"


@patch("requests.Session")
def test_auth_expired(mock_session_class):
    # Create a mock session instance
    mock_session = Mock()
    mock_session_class.return_value = mock_session

    # Mock the post method (for initial authentication)
    mock_session.post.return_value = Mock(
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

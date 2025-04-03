from unittest.mock import MagicMock

import pytest
from requests.exceptions import HTTPError, JSONDecodeError

from denvr.utils import raise_for_status


def test_raise_for_status_pass():
    response = MagicMock()
    response.status_code = 200
    result = raise_for_status(response)
    assert result is None


def test_raise_for_status_error():
    response = MagicMock()
    response.status_code = 500
    response.url = "http://localhost:9000"
    response.reason = "Server Error"
    with pytest.raises(HTTPError):
        raise_for_status(response)

    # Also handle different encoding for reason
    response.reason = "Server Error".encode("utf-8")
    with pytest.raises(HTTPError):
        raise_for_status(response)

    response.reason = "Server Error".encode("iso-8859-1")
    with pytest.raises(HTTPError):
        raise_for_status(response)


def test_raise_for_status_error_with_details():
    response = MagicMock()
    response.status_code = 404
    response.url = "http://localhost:9000"
    response.reason = "Not Found"
    response.json = lambda: {
        "error": {"message": "These are not the droids you're looking for."}
    }
    with pytest.raises(HTTPError, match="droids"):
        raise_for_status(response)

    # Handle fallback cases for no json or unknown schema
    # TODO: Use caplog for these cases.
    # https://docs.pytest.org/en/latest/how-to/logging.html#caplog-fixture
    response.json = lambda: {"err": "These are not the droids you're looking for."}
    with pytest.raises(HTTPError):
        raise_for_status(response)

    # A bit of a hack cause we can't raise an exception from a lambda function
    response.json = lambda: (_ for _ in ()).throw(JSONDecodeError("err", "", 0))
    with pytest.raises(HTTPError):
        raise_for_status(response)

from unittest.mock import Mock

import pytest
from pytest_httpserver import HTTPServer
from pytest_httpserver.httpserver import UNDEFINED

from denvr.api.v1.clusters import Client
from denvr.config import Config
from denvr.session import Session
from denvr.validate import validate_kwargs


def test_get_all():
    """
    Unit test default input/output behaviour when mocking the internal Session object.
    """
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    client.get_all()

    client_kwargs = {}

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/clusters/GetAll",
        {},
        {},
    )

    client.get_all(**client_kwargs)

    session.request.assert_called_with(
        "get",
        "/api/v1/clusters/GetAll",
        **request_kwargs,
    )


def test_get_all_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(
        defaults={"server": httpserver.url_for("/")},
        auth=None,
    )

    session = Session(config)
    client = Client(session)

    client_kwargs = {}

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/clusters/GetAll",
        {},
        {},
    )

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/clusters/GetAll",
        method="get",
        query_string=request_kwargs.get("params", None),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.get_all(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_get_all_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs = {}

    client.get_all(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.

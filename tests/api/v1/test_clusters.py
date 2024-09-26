from unittest.mock import Mock

import pytest

from denvr.api.v1.clusters import Client
from denvr.session import Session


def test_get_all():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.get_all()

    client_kwargs = {}
    request_kwargs = {}

    client.get_all(**client_kwargs)

    session.request.assert_called_with("get", "/api/v1/clusters/GetAll", **request_kwargs)
    session.reset_mock()

    client_kwargs = {}

    request_kwargs = {}

    client.get_all(**client_kwargs)

    session.request.assert_called_with(
        "get",
        "/api/v1/clusters/GetAll",
        **request_kwargs,
    )


@pytest.mark.integration
def test_integration_get_all(mock_config):
    session = Session(mock_config)
    client = Client(session)

    client_kwargs = {}

    client.get_all(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.

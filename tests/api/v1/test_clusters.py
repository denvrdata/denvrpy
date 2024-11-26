from unittest.mock import Mock

import pytest

from denvr.api.v1.clusters import Client
from denvr.config import Config
from denvr.session import Session


def test_get_all():
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    client.get_all()

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

from unittest.mock import Mock

import pytest

from denvr.api.v1.servers.images import Client
from denvr.config import Config
from denvr.session import Session
from denvr.validate import validate_kwargs


def test_get_operating_system_images():
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    client.get_operating_system_images()

    client_kwargs = {}

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/servers/images/GetOperatingSystemImages",
        {},
        {},
    )

    client.get_operating_system_images(**client_kwargs)

    session.request.assert_called_with(
        "get",
        "/api/v1/servers/images/GetOperatingSystemImages",
        **request_kwargs,
    )


@pytest.mark.integration
def test_integration_get_operating_system_images(mock_config):
    session = Session(mock_config)
    client = Client(session)

    client_kwargs = {}

    client.get_operating_system_images(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.

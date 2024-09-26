from unittest.mock import Mock

from denvr.api.v1.servers.images import Client


def test_get_operating_system_images():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.get_operating_system_images()

    client_kwargs = {}
    request_kwargs = {}

    client.get_operating_system_images(**client_kwargs)

    session.request.assert_called_with("get", "/api/v1/servers/images/GetOperatingSystemImages", **request_kwargs)
    session.reset_mock()

    client_kwargs = {}

    request_kwargs = {}

    client.get_operating_system_images(**client_kwargs)

    session.request.assert_called_with(
        "get",
        "/api/v1/servers/images/GetOperatingSystemImages",
        **request_kwargs,
    )

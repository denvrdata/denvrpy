from unittest.mock import Mock

from denvr.api.v1.clusters import Client


def test_get_all():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.get_all()

    kwargs = {}

    client.get_all(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "get",
        "/api/v1/clusters/GetAll",
        **kwargs,
    )
    session.reset_mock()

    kwargs = {}

    client.get_all(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "get",
        "/api/v1/clusters/GetAll",
        **kwargs,
    )

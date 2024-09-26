from unittest.mock import Mock

from denvr.api.v1.vpcs import Client


def test_get_vpcs():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.get_vpcs()

    kwargs = {
        "params": {
            "cluster": None,
        },
    }

    client.get_vpcs(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "get",
        "/api/v1/vpcs/GetVpcs",
        **kwargs,
    )
    session.reset_mock()

    kwargs = {
        "params": {
            "cluster": "cluster",
        },
    }

    client.get_vpcs(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "get",
        "/api/v1/vpcs/GetVpcs",
        **kwargs,
    )


def test_get_vpc():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.get_vpc()

    kwargs = {
        "params": {
            "id": None,
            "cluster": None,
        },
    }

    client.get_vpc(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "get",
        "/api/v1/vpcs/GetVpc",
        **kwargs,
    )
    session.reset_mock()

    kwargs = {
        "params": {
            "id": "id",
            "cluster": "cluster",
        },
    }

    client.get_vpc(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "get",
        "/api/v1/vpcs/GetVpc",
        **kwargs,
    )


def test_create_vpc():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.create_vpc()

    kwargs = {
        "json": {
            "id": None,
            "cluster": None,
        },
    }

    client.create_vpc(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "post",
        "/api/v1/vpcs/CreateVpc",
        **kwargs,
    )
    session.reset_mock()

    kwargs = {
        "json": {
            "id": "id",
            "cluster": "cluster",
        },
    }

    client.create_vpc(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "post",
        "/api/v1/vpcs/CreateVpc",
        **kwargs,
    )


def test_destroy_vpc():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.destroy_vpc()

    kwargs = {
        "params": {
            "id": None,
            "cluster": None,
        },
    }

    client.destroy_vpc(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "delete",
        "/api/v1/vpcs/DestroyVpc",
        **kwargs,
    )
    session.reset_mock()

    kwargs = {
        "params": {
            "id": "id",
            "cluster": "cluster",
        },
    }

    client.destroy_vpc(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "delete",
        "/api/v1/vpcs/DestroyVpc",
        **kwargs,
    )

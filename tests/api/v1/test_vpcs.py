from unittest.mock import Mock

from denvr.api.v1.vpcs import Client


def test_get_vpcs():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.get_vpcs()

    client_kwargs = {
        "cluster": None,
    }
    request_kwargs = {
        "params": {
            "Cluster": None,
        },
    }

    client.get_vpcs(**client_kwargs)

    session.request.assert_called_with("get", "/api/v1/vpcs/GetVpcs", **request_kwargs)
    session.reset_mock()

    client_kwargs = {
        "cluster": "Cluster",
    }

    request_kwargs = {
        "params": {
            "Cluster": "Cluster",
        },
    }

    client.get_vpcs(**client_kwargs)

    session.request.assert_called_with(
        "get",
        "/api/v1/vpcs/GetVpcs",
        **request_kwargs,
    )


def test_get_vpc():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.get_vpc()

    client_kwargs = {
        "id": None,
        "cluster": None,
    }
    request_kwargs = {
        "params": {
            "Id": None,
            "Cluster": None,
        },
    }

    client.get_vpc(**client_kwargs)

    session.request.assert_called_with("get", "/api/v1/vpcs/GetVpc", **request_kwargs)
    session.reset_mock()

    client_kwargs = {
        "id": "Id",
        "cluster": "Cluster",
    }

    request_kwargs = {
        "params": {
            "Id": "Id",
            "Cluster": "Cluster",
        },
    }

    client.get_vpc(**client_kwargs)

    session.request.assert_called_with(
        "get",
        "/api/v1/vpcs/GetVpc",
        **request_kwargs,
    )


def test_create_vpc():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.create_vpc()

    client_kwargs = {
        "id": None,
        "cluster": None,
    }
    request_kwargs = {
        "json": {
            "id": None,
            "cluster": None,
        },
    }

    client.create_vpc(**client_kwargs)

    session.request.assert_called_with("post", "/api/v1/vpcs/CreateVpc", **request_kwargs)
    session.reset_mock()

    client_kwargs = {
        "id": "id",
        "cluster": "cluster",
    }

    request_kwargs = {
        "json": {
            "id": "id",
            "cluster": "cluster",
        },
    }

    client.create_vpc(**client_kwargs)

    session.request.assert_called_with(
        "post",
        "/api/v1/vpcs/CreateVpc",
        **request_kwargs,
    )


def test_destroy_vpc():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.destroy_vpc()

    client_kwargs = {
        "id": None,
        "cluster": None,
    }
    request_kwargs = {
        "params": {
            "Id": None,
            "Cluster": None,
        },
    }

    client.destroy_vpc(**client_kwargs)

    session.request.assert_called_with("delete", "/api/v1/vpcs/DestroyVpc", **request_kwargs)
    session.reset_mock()

    client_kwargs = {
        "id": "Id",
        "cluster": "Cluster",
    }

    request_kwargs = {
        "params": {
            "Id": "Id",
            "Cluster": "Cluster",
        },
    }

    client.destroy_vpc(**client_kwargs)

    session.request.assert_called_with(
        "delete",
        "/api/v1/vpcs/DestroyVpc",
        **request_kwargs,
    )

from unittest.mock import Mock

import pytest

from denvr.api.v1.vpcs import Client
from denvr.session import Session


def test_get_vpcs():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.get_vpcs()

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


@pytest.mark.integration
def test_integration_get_vpcs(mock_config):
    session = Session(mock_config)
    client = Client(session)

    client_kwargs = {
        "cluster": "Cluster",
    }

    client.get_vpcs(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_get_vpc():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.get_vpc()

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


@pytest.mark.integration
def test_integration_get_vpc(mock_config):
    session = Session(mock_config)
    client = Client(session)

    client_kwargs = {
        "id": "Id",
        "cluster": "Cluster",
    }

    client.get_vpc(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_create_vpc():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.create_vpc()

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


@pytest.mark.integration
def test_integration_create_vpc(mock_config):
    session = Session(mock_config)
    client = Client(session)

    client_kwargs = {
        "id": "id",
        "cluster": "cluster",
    }

    client.create_vpc(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_destroy_vpc():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.destroy_vpc()

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


@pytest.mark.integration
def test_integration_destroy_vpc(mock_config):
    session = Session(mock_config)
    client = Client(session)

    client_kwargs = {
        "id": "Id",
        "cluster": "Cluster",
    }

    client.destroy_vpc(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.

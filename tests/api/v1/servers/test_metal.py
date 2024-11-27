from unittest.mock import Mock

import pytest

from denvr.api.v1.servers.metal import Client
from denvr.config import Config
from denvr.session import Session


def test_get_hosts():
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    client.get_hosts()

    client_kwargs = {
        "cluster": "Cluster",
    }

    request_kwargs = {
        "params": {
            "Cluster": "Cluster",
        },
    }

    client.get_hosts(**client_kwargs)

    session.request.assert_called_with(
        "get",
        "/api/v1/servers/metal/GetHosts",
        **request_kwargs,
    )


@pytest.mark.integration
def test_integration_get_hosts(mock_config):
    session = Session(mock_config)
    client = Client(session)

    client_kwargs = {
        "cluster": "Cluster",
    }

    client.get_hosts(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_get_host():
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    # Check that missing required arguments without a default should through a TypeError
    if any(getattr(config, k, None) is None for k in ["Id", "Cluster"]):
        with pytest.raises(TypeError, match=r"^Required"):
            client.get_host()
    else:
        client.get_host()

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

    client.get_host(**client_kwargs)

    session.request.assert_called_with(
        "get",
        "/api/v1/servers/metal/GetHost",
        **request_kwargs,
    )


@pytest.mark.integration
def test_integration_get_host(mock_config):
    session = Session(mock_config)
    client = Client(session)

    client_kwargs = {
        "id": "Id",
        "cluster": "Cluster",
    }

    client.get_host(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_add_host_vpc():
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    # Check that missing required arguments without a default should through a TypeError
    if any(getattr(config, k, None) is None for k in ["cluster", "id", "vpcId"]):
        with pytest.raises(TypeError, match=r"^Required"):
            client.add_host_vpc()
    else:
        client.add_host_vpc()

    client_kwargs = {
        "id": "id",
        "cluster": "cluster",
        "vpc_id": "vpcId",
    }

    request_kwargs = {
        "json": {
            "id": "id",
            "cluster": "cluster",
            "vpcId": "vpcId",
        },
    }

    client.add_host_vpc(**client_kwargs)

    session.request.assert_called_with(
        "post",
        "/api/v1/servers/metal/AddHostVpc",
        **request_kwargs,
    )


@pytest.mark.integration
def test_integration_add_host_vpc(mock_config):
    session = Session(mock_config)
    client = Client(session)

    client_kwargs = {
        "id": "id",
        "cluster": "cluster",
        "vpc_id": "vpcId",
    }

    client.add_host_vpc(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_remove_host_vpc():
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    # Check that missing required arguments without a default should through a TypeError
    if any(getattr(config, k, None) is None for k in ["cluster", "id", "vpcId"]):
        with pytest.raises(TypeError, match=r"^Required"):
            client.remove_host_vpc()
    else:
        client.remove_host_vpc()

    client_kwargs = {
        "id": "id",
        "cluster": "cluster",
        "vpc_id": "vpcId",
    }

    request_kwargs = {
        "json": {
            "id": "id",
            "cluster": "cluster",
            "vpcId": "vpcId",
        },
    }

    client.remove_host_vpc(**client_kwargs)

    session.request.assert_called_with(
        "post",
        "/api/v1/servers/metal/RemoveHostVpc",
        **request_kwargs,
    )


@pytest.mark.integration
def test_integration_remove_host_vpc(mock_config):
    session = Session(mock_config)
    client = Client(session)

    client_kwargs = {
        "id": "id",
        "cluster": "cluster",
        "vpc_id": "vpcId",
    }

    client.remove_host_vpc(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_reboot_host():
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    # Check that missing required arguments without a default should through a TypeError
    if any(getattr(config, k, None) is None for k in ["cluster", "id"]):
        with pytest.raises(TypeError, match=r"^Required"):
            client.reboot_host()
    else:
        client.reboot_host()

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

    client.reboot_host(**client_kwargs)

    session.request.assert_called_with(
        "post",
        "/api/v1/servers/metal/RebootHost",
        **request_kwargs,
    )


@pytest.mark.integration
def test_integration_reboot_host(mock_config):
    session = Session(mock_config)
    client = Client(session)

    client_kwargs = {
        "id": "id",
        "cluster": "cluster",
    }

    client.reboot_host(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.

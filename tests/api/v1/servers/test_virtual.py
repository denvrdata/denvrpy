from unittest.mock import Mock

import pytest

from denvr.api.v1.servers.virtual import Client
from denvr.config import Config
from denvr.session import Session
from denvr.validate import validate_kwargs


def test_get_servers():
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    client.get_servers()

    client_kwargs = {
        "cluster": "Cluster",
    }

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/servers/virtual/GetServers",
        {
            "params": {
                "Cluster": "Cluster",
            },
        },
        {},
    )

    client.get_servers(**client_kwargs)

    session.request.assert_called_with(
        "get",
        "/api/v1/servers/virtual/GetServers",
        **request_kwargs,
    )


@pytest.mark.integration
def test_integration_get_servers(mock_config):
    session = Session(mock_config)
    client = Client(session)

    client_kwargs = {
        "cluster": "Cluster",
    }

    client.get_servers(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_get_server():
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    # Check that missing required arguments without a default should through a TypeError
    if any(getattr(config, k, None) is None for k in ["Id", "Namespace", "Cluster"]):
        with pytest.raises(TypeError, match=r"^Required"):
            client.get_server()
    else:
        client.get_server()

    client_kwargs = {
        "id": "Id",
        "namespace": "Namespace",
        "cluster": "Cluster",
    }

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/servers/virtual/GetServer",
        {
            "params": {
                "Id": "Id",
                "Namespace": "Namespace",
                "Cluster": "Cluster",
            },
        },
        {"Id", "Namespace", "Cluster"},
    )

    client.get_server(**client_kwargs)

    session.request.assert_called_with(
        "get",
        "/api/v1/servers/virtual/GetServer",
        **request_kwargs,
    )


@pytest.mark.integration
def test_integration_get_server(mock_config):
    session = Session(mock_config)
    client = Client(session)

    client_kwargs = {
        "id": "Id",
        "namespace": "Namespace",
        "cluster": "Cluster",
    }

    client.get_server(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_create_server():
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    # Check that missing required arguments without a default should through a TypeError
    if any(getattr(config, k, None) is None for k in ["cluster", "configuration", "ssh_keys", "vpc"]):
        with pytest.raises(TypeError, match=r"^Required"):
            client.create_server()
    else:
        client.create_server()

    client_kwargs = {
        "name": "name",
        "rpool": "rpool",
        "vpc": "vpc",
        "configuration": "configuration",
        "cluster": "cluster",
        "ssh_keys": ["foo"],
        "operating_system_image": "operatingSystemImage",
        "personal_storage_mount_path": "personalStorageMountPath",
        "tenant_shared_additional_storage": "tenantSharedAdditionalStorage",
        "persist_storage": True,
        "direct_storage_mount_path": "directStorageMountPath",
        "root_disk_size": 1,
    }

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/servers/virtual/CreateServer",
        {
            "json": {
                "name": "name",
                "rpool": "rpool",
                "vpc": "vpc",
                "configuration": "configuration",
                "cluster": "cluster",
                "ssh_keys": ["foo"],
                "operatingSystemImage": "operatingSystemImage",
                "personalStorageMountPath": "personalStorageMountPath",
                "tenantSharedAdditionalStorage": "tenantSharedAdditionalStorage",
                "persistStorage": True,
                "directStorageMountPath": "directStorageMountPath",
                "rootDiskSize": 1,
            },
        },
        {"cluster", "configuration", "ssh_keys", "vpc"},
    )

    client.create_server(**client_kwargs)

    session.request.assert_called_with(
        "post",
        "/api/v1/servers/virtual/CreateServer",
        **request_kwargs,
    )


@pytest.mark.integration
def test_integration_create_server(mock_config):
    session = Session(mock_config)
    client = Client(session)

    client_kwargs = {
        "name": "name",
        "rpool": "rpool",
        "vpc": "vpc",
        "configuration": "configuration",
        "cluster": "cluster",
        "ssh_keys": ["foo"],
        "operating_system_image": "operatingSystemImage",
        "personal_storage_mount_path": "personalStorageMountPath",
        "tenant_shared_additional_storage": "tenantSharedAdditionalStorage",
        "persist_storage": True,
        "direct_storage_mount_path": "directStorageMountPath",
        "root_disk_size": 1,
    }

    client.create_server(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_start_server():
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    # Check that missing required arguments without a default should through a TypeError
    if any(getattr(config, k, None) is None for k in ["cluster", "id", "namespace"]):
        with pytest.raises(TypeError, match=r"^Required"):
            client.start_server()
    else:
        client.start_server()

    client_kwargs = {
        "id": "id",
        "namespace": "namespace",
        "cluster": "cluster",
    }

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/servers/virtual/StartServer",
        {
            "json": {
                "id": "id",
                "namespace": "namespace",
                "cluster": "cluster",
            },
        },
        {"cluster", "id", "namespace"},
    )

    client.start_server(**client_kwargs)

    session.request.assert_called_with(
        "post",
        "/api/v1/servers/virtual/StartServer",
        **request_kwargs,
    )


@pytest.mark.integration
def test_integration_start_server(mock_config):
    session = Session(mock_config)
    client = Client(session)

    client_kwargs = {
        "id": "id",
        "namespace": "namespace",
        "cluster": "cluster",
    }

    client.start_server(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_stop_server():
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    # Check that missing required arguments without a default should through a TypeError
    if any(getattr(config, k, None) is None for k in ["cluster", "id", "namespace"]):
        with pytest.raises(TypeError, match=r"^Required"):
            client.stop_server()
    else:
        client.stop_server()

    client_kwargs = {
        "id": "id",
        "namespace": "namespace",
        "cluster": "cluster",
    }

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/servers/virtual/StopServer",
        {
            "json": {
                "id": "id",
                "namespace": "namespace",
                "cluster": "cluster",
            },
        },
        {"cluster", "id", "namespace"},
    )

    client.stop_server(**client_kwargs)

    session.request.assert_called_with(
        "post",
        "/api/v1/servers/virtual/StopServer",
        **request_kwargs,
    )


@pytest.mark.integration
def test_integration_stop_server(mock_config):
    session = Session(mock_config)
    client = Client(session)

    client_kwargs = {
        "id": "id",
        "namespace": "namespace",
        "cluster": "cluster",
    }

    client.stop_server(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_destroy_server():
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    # Check that missing required arguments without a default should through a TypeError
    if any(getattr(config, k, None) is None for k in ["Id", "Namespace", "Cluster"]):
        with pytest.raises(TypeError, match=r"^Required"):
            client.destroy_server()
    else:
        client.destroy_server()

    client_kwargs = {
        "id": "Id",
        "namespace": "Namespace",
        "cluster": "Cluster",
    }

    request_kwargs = validate_kwargs(
        "delete",
        "/api/v1/servers/virtual/DestroyServer",
        {
            "params": {
                "Id": "Id",
                "Namespace": "Namespace",
                "Cluster": "Cluster",
            },
        },
        {"Id", "Namespace", "Cluster"},
    )

    client.destroy_server(**client_kwargs)

    session.request.assert_called_with(
        "delete",
        "/api/v1/servers/virtual/DestroyServer",
        **request_kwargs,
    )


@pytest.mark.integration
def test_integration_destroy_server(mock_config):
    session = Session(mock_config)
    client = Client(session)

    client_kwargs = {
        "id": "Id",
        "namespace": "Namespace",
        "cluster": "Cluster",
    }

    client.destroy_server(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_get_configurations():
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    client.get_configurations()

    client_kwargs = {}

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/servers/virtual/GetConfigurations",
        {},
        {},
    )

    client.get_configurations(**client_kwargs)

    session.request.assert_called_with(
        "get",
        "/api/v1/servers/virtual/GetConfigurations",
        **request_kwargs,
    )


@pytest.mark.integration
def test_integration_get_configurations(mock_config):
    session = Session(mock_config)
    client = Client(session)

    client_kwargs = {}

    client.get_configurations(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_get_availability():
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    # Check that missing required arguments without a default should through a TypeError
    if any(getattr(config, k, None) is None for k in ["cluster"]):
        with pytest.raises(TypeError, match=r"^Required"):
            client.get_availability()
    else:
        client.get_availability()

    client_kwargs = {
        "cluster": "cluster",
        "resource_pool": "resourcePool",
        "report_nodes": True,
    }

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/servers/virtual/GetAvailability",
        {
            "params": {
                "cluster": "cluster",
                "resourcePool": "resourcePool",
                "reportNodes": True,
            },
        },
        {"cluster"},
    )

    client.get_availability(**client_kwargs)

    session.request.assert_called_with(
        "get",
        "/api/v1/servers/virtual/GetAvailability",
        **request_kwargs,
    )


@pytest.mark.integration
def test_integration_get_availability(mock_config):
    session = Session(mock_config)
    client = Client(session)

    client_kwargs = {
        "cluster": "cluster",
        "resource_pool": "resourcePool",
        "report_nodes": True,
    }

    client.get_availability(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.

from unittest.mock import Mock

import pytest

from denvr.api.v1.servers.virtual import Client
from denvr.session import Session


def test_get_servers():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.get_servers()

    client_kwargs = {
        "cluster": "Cluster",
    }

    request_kwargs = {
        "params": {
            "Cluster": "Cluster",
        },
    }

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
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.get_server()

    client_kwargs = {
        "id": "Id",
        "namespace": "Namespace",
        "cluster": "Cluster",
    }

    request_kwargs = {
        "params": {
            "Id": "Id",
            "Namespace": "Namespace",
            "Cluster": "Cluster",
        },
    }

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
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
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

    request_kwargs = {
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
    }

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
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.start_server()

    client_kwargs = {
        "id": "id",
        "namespace": "namespace",
        "cluster": "cluster",
    }

    request_kwargs = {
        "json": {
            "id": "id",
            "namespace": "namespace",
            "cluster": "cluster",
        },
    }

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
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.stop_server()

    client_kwargs = {
        "id": "id",
        "namespace": "namespace",
        "cluster": "cluster",
    }

    request_kwargs = {
        "json": {
            "id": "id",
            "namespace": "namespace",
            "cluster": "cluster",
        },
    }

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
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.destroy_server()

    client_kwargs = {
        "id": "Id",
        "namespace": "Namespace",
        "cluster": "Cluster",
    }

    request_kwargs = {
        "params": {
            "Id": "Id",
            "Namespace": "Namespace",
            "Cluster": "Cluster",
        },
    }

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
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.get_configurations()

    client_kwargs = {}

    request_kwargs = {}

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
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.get_availability()

    client_kwargs = {
        "cluster": "cluster",
        "resource_pool": "resourcePool",
    }

    request_kwargs = {
        "params": {
            "cluster": "cluster",
            "resourcePool": "resourcePool",
        },
    }

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
    }

    client.get_availability(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.

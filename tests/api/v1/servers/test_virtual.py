from unittest.mock import Mock

from denvr.api.v1.servers.virtual import Client


def test_get_servers():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.get_servers()

    kwargs = {
        "params": {
            "cluster": None,
        },
    }

    client.get_servers(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "get",
        "/api/v1/servers/virtual/GetServers",
        **kwargs,
    )
    session.reset_mock()

    kwargs = {
        "params": {
            "cluster": "cluster",
        },
    }

    client.get_servers(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "get",
        "/api/v1/servers/virtual/GetServers",
        **kwargs,
    )


def test_get_server():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.get_server()

    kwargs = {
        "params": {
            "id": None,
            "namespace": None,
            "cluster": None,
        },
    }

    client.get_server(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "get",
        "/api/v1/servers/virtual/GetServer",
        **kwargs,
    )
    session.reset_mock()

    kwargs = {
        "params": {
            "id": "id",
            "namespace": "namespace",
            "cluster": "cluster",
        },
    }

    client.get_server(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "get",
        "/api/v1/servers/virtual/GetServer",
        **kwargs,
    )


def test_create_server():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.create_server()

    kwargs = {
        "json": {
            "name": None,
            "rpool": None,
            "vpc": None,
            "configuration": None,
            "cluster": None,
            "ssh_keys": None,
            "operating_system_image": None,
            "personal_storage_mount_path": None,
            "tenant_shared_additional_storage": None,
            "persist_storage": None,
            "direct_storage_mount_path": None,
            "root_disk_size": None,
        },
    }

    client.create_server(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "post",
        "/api/v1/servers/virtual/CreateServer",
        **kwargs,
    )
    session.reset_mock()

    kwargs = {
        "json": {
            "name": "name",
            "rpool": "rpool",
            "vpc": "vpc",
            "configuration": "configuration",
            "cluster": "cluster",
            "ssh_keys": [],
            "operating_system_image": "operating_system_image",
            "personal_storage_mount_path": "personal_storage_mount_path",
            "tenant_shared_additional_storage": "tenant_shared_additional_storage",
            "persist_storage": True,
            "direct_storage_mount_path": "direct_storage_mount_path",
            "root_disk_size": 1,
        },
    }

    client.create_server(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "post",
        "/api/v1/servers/virtual/CreateServer",
        **kwargs,
    )


def test_start_server():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.start_server()

    kwargs = {
        "json": {
            "id": None,
            "namespace": None,
            "cluster": None,
        },
    }

    client.start_server(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "post",
        "/api/v1/servers/virtual/StartServer",
        **kwargs,
    )
    session.reset_mock()

    kwargs = {
        "json": {
            "id": "id",
            "namespace": "namespace",
            "cluster": "cluster",
        },
    }

    client.start_server(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "post",
        "/api/v1/servers/virtual/StartServer",
        **kwargs,
    )


def test_stop_server():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.stop_server()

    kwargs = {
        "json": {
            "id": None,
            "namespace": None,
            "cluster": None,
        },
    }

    client.stop_server(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "post",
        "/api/v1/servers/virtual/StopServer",
        **kwargs,
    )
    session.reset_mock()

    kwargs = {
        "json": {
            "id": "id",
            "namespace": "namespace",
            "cluster": "cluster",
        },
    }

    client.stop_server(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "post",
        "/api/v1/servers/virtual/StopServer",
        **kwargs,
    )


def test_destroy_server():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.destroy_server()

    kwargs = {
        "params": {
            "id": None,
            "namespace": None,
            "cluster": None,
        },
    }

    client.destroy_server(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "delete",
        "/api/v1/servers/virtual/DestroyServer",
        **kwargs,
    )
    session.reset_mock()

    kwargs = {
        "params": {
            "id": "id",
            "namespace": "namespace",
            "cluster": "cluster",
        },
    }

    client.destroy_server(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "delete",
        "/api/v1/servers/virtual/DestroyServer",
        **kwargs,
    )


def test_get_configurations():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.get_configurations()

    kwargs = {}

    client.get_configurations(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "get",
        "/api/v1/servers/virtual/GetConfigurations",
        **kwargs,
    )
    session.reset_mock()

    kwargs = {}

    client.get_configurations(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "get",
        "/api/v1/servers/virtual/GetConfigurations",
        **kwargs,
    )


def test_get_availability():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.get_availability()

    kwargs = {
        "params": {
            "cluster": None,
            "resource_pool": None,
        },
    }

    client.get_availability(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "get",
        "/api/v1/servers/virtual/GetAvailability",
        **kwargs,
    )
    session.reset_mock()

    kwargs = {
        "params": {
            "cluster": "cluster",
            "resource_pool": "resource_pool",
        },
    }

    client.get_availability(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "get",
        "/api/v1/servers/virtual/GetAvailability",
        **kwargs,
    )

import pytest

from typing import Any, Dict

from unittest.mock import Mock
from pytest_httpserver import HTTPServer
from pytest_httpserver.httpserver import UNDEFINED

from denvr.config import Config
from denvr.session import Session
from denvr.api.v1.servers.virtual import Client
from denvr.validate import validate_kwargs


def test_get_servers():
    """
    Unit test default input/output behaviour when mocking the internal Session object.
    """
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    client.get_servers()

    client_kwargs: Dict[str, Any] = {
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


def test_get_servers_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(
        defaults={"server": httpserver.url_for("/")},
        auth=None,
    )

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {
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

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/servers/virtual/GetServers",
        method="get",
        query_string=request_kwargs.get("params", None),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.get_servers(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_get_servers_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {
        "cluster": "Cluster",
    }

    client.get_servers(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_get_server():
    """
    Unit test default input/output behaviour when mocking the internal Session object.
    """
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

    client_kwargs: Dict[str, Any] = {
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


def test_get_server_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(
        defaults={"server": httpserver.url_for("/")},
        auth=None,
    )

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {
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

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/servers/virtual/GetServer",
        method="get",
        query_string=request_kwargs.get("params", None),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.get_server(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_get_server_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {
        "id": "Id",
        "namespace": "Namespace",
        "cluster": "Cluster",
    }

    client.get_server(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_create_server():
    """
    Unit test default input/output behaviour when mocking the internal Session object.
    """
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    # Check that missing required arguments without a default should through a TypeError
    if any(
        getattr(config, k, None) is None
        for k in ["cluster", "configuration", "ssh_keys", "vpc"]
    ):
        with pytest.raises(TypeError, match=r"^Required"):
            client.create_server()
    else:
        client.create_server()

    client_kwargs: Dict[str, Any] = {
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


def test_create_server_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(
        defaults={"server": httpserver.url_for("/")},
        auth=None,
    )

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {
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

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/servers/virtual/CreateServer",
        method="post",
        query_string=request_kwargs.get("params", None),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.create_server(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_create_server_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {
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
    """
    Unit test default input/output behaviour when mocking the internal Session object.
    """
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

    client_kwargs: Dict[str, Any] = {
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


def test_start_server_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(
        defaults={"server": httpserver.url_for("/")},
        auth=None,
    )

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {
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

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/servers/virtual/StartServer",
        method="post",
        query_string=request_kwargs.get("params", None),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.start_server(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_start_server_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {
        "id": "id",
        "namespace": "namespace",
        "cluster": "cluster",
    }

    client.start_server(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_stop_server():
    """
    Unit test default input/output behaviour when mocking the internal Session object.
    """
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

    client_kwargs: Dict[str, Any] = {
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


def test_stop_server_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(
        defaults={"server": httpserver.url_for("/")},
        auth=None,
    )

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {
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

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/servers/virtual/StopServer",
        method="post",
        query_string=request_kwargs.get("params", None),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.stop_server(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_stop_server_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {
        "id": "id",
        "namespace": "namespace",
        "cluster": "cluster",
    }

    client.stop_server(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_destroy_server():
    """
    Unit test default input/output behaviour when mocking the internal Session object.
    """
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

    client_kwargs: Dict[str, Any] = {
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


def test_destroy_server_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(
        defaults={"server": httpserver.url_for("/")},
        auth=None,
    )

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {
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

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/servers/virtual/DestroyServer",
        method="delete",
        query_string=request_kwargs.get("params", None),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.destroy_server(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_destroy_server_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {
        "id": "Id",
        "namespace": "Namespace",
        "cluster": "Cluster",
    }

    client.destroy_server(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_get_configurations():
    """
    Unit test default input/output behaviour when mocking the internal Session object.
    """
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    client.get_configurations()

    client_kwargs: Dict[str, Any] = {}

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


def test_get_configurations_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(
        defaults={"server": httpserver.url_for("/")},
        auth=None,
    )

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {}

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/servers/virtual/GetConfigurations",
        {},
        {},
    )

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/servers/virtual/GetConfigurations",
        method="get",
        query_string=request_kwargs.get("params", None),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.get_configurations(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_get_configurations_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {}

    client.get_configurations(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_get_availability():
    """
    Unit test default input/output behaviour when mocking the internal Session object.
    """
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

    client_kwargs: Dict[str, Any] = {
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


def test_get_availability_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(
        defaults={"server": httpserver.url_for("/")},
        auth=None,
    )

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {
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

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/servers/virtual/GetAvailability",
        method="get",
        query_string=request_kwargs.get("params", None),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.get_availability(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_get_availability_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {
        "cluster": "cluster",
        "resource_pool": "resourcePool",
        "report_nodes": True,
    }

    client.get_availability(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.

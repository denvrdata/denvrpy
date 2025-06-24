import pytest

from typing import Any, Dict

from unittest.mock import Mock
from pytest_httpserver import HTTPServer
from pytest_httpserver.httpserver import UNDEFINED

from denvr.config import Config
from denvr.session import Session
from denvr.api.v1.servers.applications import Client
from denvr.validate import validate_kwargs


def test_get_applications():
    """
    Unit test default input/output behaviour when mocking the internal Session object.
    """
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    client.get_applications()

    client_kwargs: Dict[str, Any] = {}

    request_kwargs = validate_kwargs(
        "get", "/api/v1/servers/applications/GetApplications", {}, {}
    )

    client.get_applications(**client_kwargs)

    session.request.assert_called_with(
        "get", "/api/v1/servers/applications/GetApplications", **request_kwargs
    )


def test_get_applications_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(defaults={"server": httpserver.url_for("/")}, auth=None)

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {}

    request_kwargs = validate_kwargs(
        "get", "/api/v1/servers/applications/GetApplications", {}, {}
    )

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/servers/applications/GetApplications",
        method="get",
        query_string=request_kwargs.get("params", None),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.get_applications(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_get_applications_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {}

    client.get_applications(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_get_application_details():
    """
    Unit test default input/output behaviour when mocking the internal Session object.
    """
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    # Check that missing required arguments without a default should through a TypeError
    if any(getattr(config, k, None) is None for k in ["Id", "Cluster"]):
        with pytest.raises(TypeError, match=r"^Required"):
            client.get_application_details()
    else:
        client.get_application_details()

    client_kwargs: Dict[str, Any] = {"id": "my-jupyter-application", "cluster": "Msc1"}

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/servers/applications/GetApplicationDetails",
        {"params": {"Id": "my-jupyter-application", "Cluster": "Msc1"}},
        {"Id", "Cluster"},
    )

    client.get_application_details(**client_kwargs)

    session.request.assert_called_with(
        "get", "/api/v1/servers/applications/GetApplicationDetails", **request_kwargs
    )


def test_get_application_details_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(defaults={"server": httpserver.url_for("/")}, auth=None)

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {"id": "my-jupyter-application", "cluster": "Msc1"}

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/servers/applications/GetApplicationDetails",
        {"params": {"Id": "my-jupyter-application", "Cluster": "Msc1"}},
        {"Id", "Cluster"},
    )

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/servers/applications/GetApplicationDetails",
        method="get",
        query_string=request_kwargs.get("params", None),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.get_application_details(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_get_application_details_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {"id": "my-jupyter-application", "cluster": "Msc1"}

    client.get_application_details(**client_kwargs)
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
        "get", "/api/v1/servers/applications/GetConfigurations", {}, {}
    )

    client.get_configurations(**client_kwargs)

    session.request.assert_called_with(
        "get", "/api/v1/servers/applications/GetConfigurations", **request_kwargs
    )


def test_get_configurations_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(defaults={"server": httpserver.url_for("/")}, auth=None)

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {}

    request_kwargs = validate_kwargs(
        "get", "/api/v1/servers/applications/GetConfigurations", {}, {}
    )

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/servers/applications/GetConfigurations",
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
    if any(getattr(config, k, None) is None for k in ["cluster", "resourcePool"]):
        with pytest.raises(TypeError, match=r"^Required"):
            client.get_availability()
    else:
        client.get_availability()

    client_kwargs: Dict[str, Any] = {"cluster": "Msc1", "resource_pool": "on-demand"}

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/servers/applications/GetAvailability",
        {"params": {"cluster": "Msc1", "resourcePool": "on-demand"}},
        {"cluster", "resourcePool"},
    )

    client.get_availability(**client_kwargs)

    session.request.assert_called_with(
        "get", "/api/v1/servers/applications/GetAvailability", **request_kwargs
    )


def test_get_availability_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(defaults={"server": httpserver.url_for("/")}, auth=None)

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {"cluster": "Msc1", "resource_pool": "on-demand"}

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/servers/applications/GetAvailability",
        {"params": {"cluster": "Msc1", "resourcePool": "on-demand"}},
        {"cluster", "resourcePool"},
    )

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/servers/applications/GetAvailability",
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

    client_kwargs: Dict[str, Any] = {"cluster": "Msc1", "resource_pool": "on-demand"}

    client.get_availability(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_get_application_catalog_items():
    """
    Unit test default input/output behaviour when mocking the internal Session object.
    """
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    client.get_application_catalog_items()

    client_kwargs: Dict[str, Any] = {}

    request_kwargs = validate_kwargs(
        "get", "/api/v1/servers/applications/GetApplicationCatalogItems", {}, {}
    )

    client.get_application_catalog_items(**client_kwargs)

    session.request.assert_called_with(
        "get", "/api/v1/servers/applications/GetApplicationCatalogItems", **request_kwargs
    )


def test_get_application_catalog_items_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(defaults={"server": httpserver.url_for("/")}, auth=None)

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {}

    request_kwargs = validate_kwargs(
        "get", "/api/v1/servers/applications/GetApplicationCatalogItems", {}, {}
    )

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/servers/applications/GetApplicationCatalogItems",
        method="get",
        query_string=request_kwargs.get("params", None),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.get_application_catalog_items(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_get_application_catalog_items_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {}

    client.get_application_catalog_items(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_create_catalog_application():
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
        for k in [
            "applicationCatalogItemName",
            "applicationCatalogItemVersion",
            "cluster",
            "hardwarePackageName",
            "name",
        ]
    ):
        with pytest.raises(TypeError, match=r"^Required"):
            client.create_catalog_application()
    else:
        client.create_catalog_application()

    client_kwargs: Dict[str, Any] = {
        "name": "my-jupyter-application",
        "cluster": "Msc1",
        "hardware_package_name": "g-nvidia-1xa100-40gb-pcie-14vcpu-112gb",
        "application_catalog_item_name": "jupyter-notebook",
        "application_catalog_item_version": "python-3.11.9",
        "resource_pool": "on-demand",
        "ssh_keys": ["string"],
        "persist_direct_attached_storage": False,
        "personal_shared_storage": True,
        "tenant_shared_storage": True,
        "jupyter_token": "abc123",
    }

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/servers/applications/CreateCatalogApplication",
        {
            "json": {
                "name": "my-jupyter-application",
                "cluster": "Msc1",
                "hardwarePackageName": "g-nvidia-1xa100-40gb-pcie-14vcpu-112gb",
                "applicationCatalogItemName": "jupyter-notebook",
                "applicationCatalogItemVersion": "python-3.11.9",
                "resourcePool": "on-demand",
                "sshKeys": ["string"],
                "persistDirectAttachedStorage": False,
                "personalSharedStorage": True,
                "tenantSharedStorage": True,
                "jupyterToken": "abc123",
            }
        },
        {
            "applicationCatalogItemName",
            "applicationCatalogItemVersion",
            "cluster",
            "hardwarePackageName",
            "name",
        },
    )

    client.create_catalog_application(**client_kwargs)

    session.request.assert_called_with(
        "post", "/api/v1/servers/applications/CreateCatalogApplication", **request_kwargs
    )


def test_create_catalog_application_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(defaults={"server": httpserver.url_for("/")}, auth=None)

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {
        "name": "my-jupyter-application",
        "cluster": "Msc1",
        "hardware_package_name": "g-nvidia-1xa100-40gb-pcie-14vcpu-112gb",
        "application_catalog_item_name": "jupyter-notebook",
        "application_catalog_item_version": "python-3.11.9",
        "resource_pool": "on-demand",
        "ssh_keys": ["string"],
        "persist_direct_attached_storage": False,
        "personal_shared_storage": True,
        "tenant_shared_storage": True,
        "jupyter_token": "abc123",
    }

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/servers/applications/CreateCatalogApplication",
        {
            "json": {
                "name": "my-jupyter-application",
                "cluster": "Msc1",
                "hardwarePackageName": "g-nvidia-1xa100-40gb-pcie-14vcpu-112gb",
                "applicationCatalogItemName": "jupyter-notebook",
                "applicationCatalogItemVersion": "python-3.11.9",
                "resourcePool": "on-demand",
                "sshKeys": ["string"],
                "persistDirectAttachedStorage": False,
                "personalSharedStorage": True,
                "tenantSharedStorage": True,
                "jupyterToken": "abc123",
            }
        },
        {
            "applicationCatalogItemName",
            "applicationCatalogItemVersion",
            "cluster",
            "hardwarePackageName",
            "name",
        },
    )

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/servers/applications/CreateCatalogApplication",
        method="post",
        query_string=request_kwargs.get("params", None),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.create_catalog_application(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_create_catalog_application_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {
        "name": "my-jupyter-application",
        "cluster": "Msc1",
        "hardware_package_name": "g-nvidia-1xa100-40gb-pcie-14vcpu-112gb",
        "application_catalog_item_name": "jupyter-notebook",
        "application_catalog_item_version": "python-3.11.9",
        "resource_pool": "on-demand",
        "ssh_keys": ["string"],
        "persist_direct_attached_storage": False,
        "personal_shared_storage": True,
        "tenant_shared_storage": True,
        "jupyter_token": "abc123",
    }

    client.create_catalog_application(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_create_custom_application():
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
        for k in ["cluster", "hardwarePackageName", "imageRepository", "imageUrl", "name"]
    ):
        with pytest.raises(TypeError, match=r"^Required"):
            client.create_custom_application()
    else:
        client.create_custom_application()

    client_kwargs: Dict[str, Any] = {
        "name": "my-custom-application",
        "cluster": "Msc1",
        "hardware_package_name": "g-nvidia-1xa100-40gb-pcie-14vcpu-112gb",
        "image_url": "docker.io/{namespace}/{repository}:{tag}",
        "image_cmd_override": ["python", "train.py"],
        "environment_variables": {},
        "image_repository": {
            "hostname": "https://index.docker.io/v1/",
            "username": "your-docker-username",
            "password": "dckr_pat__xxx1234567890abcdef",
        },
        "resource_pool": "on-demand",
        "readiness_watcher_port": 443,
        "proxy_port": 8888,
        "persist_direct_attached_storage": False,
        "personal_shared_storage": True,
        "tenant_shared_storage": True,
        "user_scripts": {},
        "security_context": {"runAsRoot": False},
    }

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/servers/applications/CreateCustomApplication",
        {
            "json": {
                "name": "my-custom-application",
                "cluster": "Msc1",
                "hardwarePackageName": "g-nvidia-1xa100-40gb-pcie-14vcpu-112gb",
                "imageUrl": "docker.io/{namespace}/{repository}:{tag}",
                "imageCmdOverride": ["python", "train.py"],
                "environmentVariables": {},
                "imageRepository": {
                    "hostname": "https://index.docker.io/v1/",
                    "username": "your-docker-username",
                    "password": "dckr_pat__xxx1234567890abcdef",
                },
                "resourcePool": "on-demand",
                "readinessWatcherPort": 443,
                "proxyPort": 8888,
                "persistDirectAttachedStorage": False,
                "personalSharedStorage": True,
                "tenantSharedStorage": True,
                "userScripts": {},
                "securityContext": {"runAsRoot": False},
            }
        },
        {"cluster", "hardwarePackageName", "imageRepository", "imageUrl", "name"},
    )

    client.create_custom_application(**client_kwargs)

    session.request.assert_called_with(
        "post", "/api/v1/servers/applications/CreateCustomApplication", **request_kwargs
    )


def test_create_custom_application_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(defaults={"server": httpserver.url_for("/")}, auth=None)

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {
        "name": "my-custom-application",
        "cluster": "Msc1",
        "hardware_package_name": "g-nvidia-1xa100-40gb-pcie-14vcpu-112gb",
        "image_url": "docker.io/{namespace}/{repository}:{tag}",
        "image_cmd_override": ["python", "train.py"],
        "environment_variables": {},
        "image_repository": {
            "hostname": "https://index.docker.io/v1/",
            "username": "your-docker-username",
            "password": "dckr_pat__xxx1234567890abcdef",
        },
        "resource_pool": "on-demand",
        "readiness_watcher_port": 443,
        "proxy_port": 8888,
        "persist_direct_attached_storage": False,
        "personal_shared_storage": True,
        "tenant_shared_storage": True,
        "user_scripts": {},
        "security_context": {"runAsRoot": False},
    }

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/servers/applications/CreateCustomApplication",
        {
            "json": {
                "name": "my-custom-application",
                "cluster": "Msc1",
                "hardwarePackageName": "g-nvidia-1xa100-40gb-pcie-14vcpu-112gb",
                "imageUrl": "docker.io/{namespace}/{repository}:{tag}",
                "imageCmdOverride": ["python", "train.py"],
                "environmentVariables": {},
                "imageRepository": {
                    "hostname": "https://index.docker.io/v1/",
                    "username": "your-docker-username",
                    "password": "dckr_pat__xxx1234567890abcdef",
                },
                "resourcePool": "on-demand",
                "readinessWatcherPort": 443,
                "proxyPort": 8888,
                "persistDirectAttachedStorage": False,
                "personalSharedStorage": True,
                "tenantSharedStorage": True,
                "userScripts": {},
                "securityContext": {"runAsRoot": False},
            }
        },
        {"cluster", "hardwarePackageName", "imageRepository", "imageUrl", "name"},
    )

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/servers/applications/CreateCustomApplication",
        method="post",
        query_string=request_kwargs.get("params", None),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.create_custom_application(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_create_custom_application_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {
        "name": "my-custom-application",
        "cluster": "Msc1",
        "hardware_package_name": "g-nvidia-1xa100-40gb-pcie-14vcpu-112gb",
        "image_url": "docker.io/{namespace}/{repository}:{tag}",
        "image_cmd_override": ["python", "train.py"],
        "environment_variables": {},
        "image_repository": {
            "hostname": "https://index.docker.io/v1/",
            "username": "your-docker-username",
            "password": "dckr_pat__xxx1234567890abcdef",
        },
        "resource_pool": "on-demand",
        "readiness_watcher_port": 443,
        "proxy_port": 8888,
        "persist_direct_attached_storage": False,
        "personal_shared_storage": True,
        "tenant_shared_storage": True,
        "user_scripts": {},
        "security_context": {"runAsRoot": False},
    }

    client.create_custom_application(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_start_application():
    """
    Unit test default input/output behaviour when mocking the internal Session object.
    """
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    # Check that missing required arguments without a default should through a TypeError
    if any(getattr(config, k, None) is None for k in ["cluster", "id"]):
        with pytest.raises(TypeError, match=r"^Required"):
            client.start_application()
    else:
        client.start_application()

    client_kwargs: Dict[str, Any] = {"id": "my-jupyter-application", "cluster": "Msc1"}

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/servers/applications/StartApplication",
        {"json": {"id": "my-jupyter-application", "cluster": "Msc1"}},
        {"cluster", "id"},
    )

    client.start_application(**client_kwargs)

    session.request.assert_called_with(
        "post", "/api/v1/servers/applications/StartApplication", **request_kwargs
    )


def test_start_application_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(defaults={"server": httpserver.url_for("/")}, auth=None)

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {"id": "my-jupyter-application", "cluster": "Msc1"}

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/servers/applications/StartApplication",
        {"json": {"id": "my-jupyter-application", "cluster": "Msc1"}},
        {"cluster", "id"},
    )

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/servers/applications/StartApplication",
        method="post",
        query_string=request_kwargs.get("params", None),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.start_application(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_start_application_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {"id": "my-jupyter-application", "cluster": "Msc1"}

    client.start_application(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_stop_application():
    """
    Unit test default input/output behaviour when mocking the internal Session object.
    """
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    # Check that missing required arguments without a default should through a TypeError
    if any(getattr(config, k, None) is None for k in ["cluster", "id"]):
        with pytest.raises(TypeError, match=r"^Required"):
            client.stop_application()
    else:
        client.stop_application()

    client_kwargs: Dict[str, Any] = {"id": "my-jupyter-application", "cluster": "Msc1"}

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/servers/applications/StopApplication",
        {"json": {"id": "my-jupyter-application", "cluster": "Msc1"}},
        {"cluster", "id"},
    )

    client.stop_application(**client_kwargs)

    session.request.assert_called_with(
        "post", "/api/v1/servers/applications/StopApplication", **request_kwargs
    )


def test_stop_application_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(defaults={"server": httpserver.url_for("/")}, auth=None)

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {"id": "my-jupyter-application", "cluster": "Msc1"}

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/servers/applications/StopApplication",
        {"json": {"id": "my-jupyter-application", "cluster": "Msc1"}},
        {"cluster", "id"},
    )

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/servers/applications/StopApplication",
        method="post",
        query_string=request_kwargs.get("params", None),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.stop_application(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_stop_application_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {"id": "my-jupyter-application", "cluster": "Msc1"}

    client.stop_application(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_destroy_application():
    """
    Unit test default input/output behaviour when mocking the internal Session object.
    """
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    # Check that missing required arguments without a default should through a TypeError
    if any(getattr(config, k, None) is None for k in ["Id", "Cluster"]):
        with pytest.raises(TypeError, match=r"^Required"):
            client.destroy_application()
    else:
        client.destroy_application()

    client_kwargs: Dict[str, Any] = {"id": "my-jupyter-application", "cluster": "Msc1"}

    request_kwargs = validate_kwargs(
        "delete",
        "/api/v1/servers/applications/DestroyApplication",
        {"params": {"Id": "my-jupyter-application", "Cluster": "Msc1"}},
        {"Id", "Cluster"},
    )

    client.destroy_application(**client_kwargs)

    session.request.assert_called_with(
        "delete", "/api/v1/servers/applications/DestroyApplication", **request_kwargs
    )


def test_destroy_application_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(defaults={"server": httpserver.url_for("/")}, auth=None)

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {"id": "my-jupyter-application", "cluster": "Msc1"}

    request_kwargs = validate_kwargs(
        "delete",
        "/api/v1/servers/applications/DestroyApplication",
        {"params": {"Id": "my-jupyter-application", "Cluster": "Msc1"}},
        {"Id", "Cluster"},
    )

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/servers/applications/DestroyApplication",
        method="delete",
        query_string=request_kwargs.get("params", None),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.destroy_application(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_destroy_application_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {"id": "my-jupyter-application", "cluster": "Msc1"}

    client.destroy_application(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.

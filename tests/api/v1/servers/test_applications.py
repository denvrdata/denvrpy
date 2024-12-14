from unittest.mock import Mock

import pytest
from pytest_httpserver import HTTPServer
from pytest_httpserver.httpserver import UNDEFINED

from denvr.api.v1.servers.applications import Client
from denvr.config import Config
from denvr.session import Session
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

    client_kwargs = {}

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/servers/applications/GetApplications",
        {},
        {},
    )

    client.get_applications(**client_kwargs)

    session.request.assert_called_with(
        "get",
        "/api/v1/servers/applications/GetApplications",
        **request_kwargs,
    )


def test_get_applications_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(
        defaults={"server": httpserver.url_for("/")},
        auth=None,
    )

    session = Session(config)
    client = Client(session)

    client_kwargs = {}

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/servers/applications/GetApplications",
        {},
        {},
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

    client_kwargs = {}

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

    client_kwargs = {
        "id": "Id",
        "cluster": "Cluster",
    }

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/servers/applications/GetApplicationDetails",
        {
            "params": {
                "Id": "Id",
                "Cluster": "Cluster",
            },
        },
        {"Id", "Cluster"},
    )

    client.get_application_details(**client_kwargs)

    session.request.assert_called_with(
        "get",
        "/api/v1/servers/applications/GetApplicationDetails",
        **request_kwargs,
    )


def test_get_application_details_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(
        defaults={"server": httpserver.url_for("/")},
        auth=None,
    )

    session = Session(config)
    client = Client(session)

    client_kwargs = {
        "id": "Id",
        "cluster": "Cluster",
    }

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/servers/applications/GetApplicationDetails",
        {
            "params": {
                "Id": "Id",
                "Cluster": "Cluster",
            },
        },
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

    client_kwargs = {
        "id": "Id",
        "cluster": "Cluster",
    }

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

    client_kwargs = {}

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/servers/applications/GetConfigurations",
        {},
        {},
    )

    client.get_configurations(**client_kwargs)

    session.request.assert_called_with(
        "get",
        "/api/v1/servers/applications/GetConfigurations",
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

    client_kwargs = {}

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/servers/applications/GetConfigurations",
        {},
        {},
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

    client_kwargs = {}

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

    client_kwargs = {
        "cluster": "cluster",
        "resource_pool": "resourcePool",
    }

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/servers/applications/GetAvailability",
        {
            "params": {
                "cluster": "cluster",
                "resourcePool": "resourcePool",
            },
        },
        {"cluster", "resourcePool"},
    )

    client.get_availability(**client_kwargs)

    session.request.assert_called_with(
        "get",
        "/api/v1/servers/applications/GetAvailability",
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

    client_kwargs = {
        "cluster": "cluster",
        "resource_pool": "resourcePool",
    }

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/servers/applications/GetAvailability",
        {
            "params": {
                "cluster": "cluster",
                "resourcePool": "resourcePool",
            },
        },
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

    client_kwargs = {
        "cluster": "cluster",
        "resource_pool": "resourcePool",
    }

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

    client_kwargs = {}

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/servers/applications/GetApplicationCatalogItems",
        {},
        {},
    )

    client.get_application_catalog_items(**client_kwargs)

    session.request.assert_called_with(
        "get",
        "/api/v1/servers/applications/GetApplicationCatalogItems",
        **request_kwargs,
    )


def test_get_application_catalog_items_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(
        defaults={"server": httpserver.url_for("/")},
        auth=None,
    )

    session = Session(config)
    client = Client(session)

    client_kwargs = {}

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/servers/applications/GetApplicationCatalogItems",
        {},
        {},
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

    client_kwargs = {}

    client.get_application_catalog_items(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_create_application():
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
            client.create_application()
    else:
        client.create_application()

    client_kwargs = {
        "name": "name",
        "cluster": "cluster",
        "hardware_package_name": "hardwarePackageName",
        "application_catalog_item_name": "applicationCatalogItemName",
        "application_catalog_item_version": "applicationCatalogItemVersion",
        "resource_pool": "resourcePool",
        "ssh_keys": ["foo"],
        "persist_direct_attached_storage": True,
        "personal_shared_storage": True,
        "tenant_shared_storage": True,
        "jupyter_token": "jupyterToken",
    }

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/servers/applications/CreateApplication",
        {
            "json": {
                "name": "name",
                "cluster": "cluster",
                "hardwarePackageName": "hardwarePackageName",
                "applicationCatalogItemName": "applicationCatalogItemName",
                "applicationCatalogItemVersion": "applicationCatalogItemVersion",
                "resourcePool": "resourcePool",
                "sshKeys": ["foo"],
                "persistDirectAttachedStorage": True,
                "personalSharedStorage": True,
                "tenantSharedStorage": True,
                "jupyterToken": "jupyterToken",
            },
        },
        {"applicationCatalogItemName", "applicationCatalogItemVersion", "cluster", "hardwarePackageName", "name"},
    )

    client.create_application(**client_kwargs)

    session.request.assert_called_with(
        "post",
        "/api/v1/servers/applications/CreateApplication",
        **request_kwargs,
    )


def test_create_application_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(
        defaults={"server": httpserver.url_for("/")},
        auth=None,
    )

    session = Session(config)
    client = Client(session)

    client_kwargs = {
        "name": "name",
        "cluster": "cluster",
        "hardware_package_name": "hardwarePackageName",
        "application_catalog_item_name": "applicationCatalogItemName",
        "application_catalog_item_version": "applicationCatalogItemVersion",
        "resource_pool": "resourcePool",
        "ssh_keys": ["foo"],
        "persist_direct_attached_storage": True,
        "personal_shared_storage": True,
        "tenant_shared_storage": True,
        "jupyter_token": "jupyterToken",
    }

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/servers/applications/CreateApplication",
        {
            "json": {
                "name": "name",
                "cluster": "cluster",
                "hardwarePackageName": "hardwarePackageName",
                "applicationCatalogItemName": "applicationCatalogItemName",
                "applicationCatalogItemVersion": "applicationCatalogItemVersion",
                "resourcePool": "resourcePool",
                "sshKeys": ["foo"],
                "persistDirectAttachedStorage": True,
                "personalSharedStorage": True,
                "tenantSharedStorage": True,
                "jupyterToken": "jupyterToken",
            },
        },
        {"applicationCatalogItemName", "applicationCatalogItemVersion", "cluster", "hardwarePackageName", "name"},
    )

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/servers/applications/CreateApplication",
        method="post",
        query_string=request_kwargs.get("params", None),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.create_application(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_create_application_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs = {
        "name": "name",
        "cluster": "cluster",
        "hardware_package_name": "hardwarePackageName",
        "application_catalog_item_name": "applicationCatalogItemName",
        "application_catalog_item_version": "applicationCatalogItemVersion",
        "resource_pool": "resourcePool",
        "ssh_keys": ["foo"],
        "persist_direct_attached_storage": True,
        "personal_shared_storage": True,
        "tenant_shared_storage": True,
        "jupyter_token": "jupyterToken",
    }

    client.create_application(**client_kwargs)
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

    client_kwargs = {
        "id": "id",
        "cluster": "cluster",
    }

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/servers/applications/StartApplication",
        {
            "json": {
                "id": "id",
                "cluster": "cluster",
            },
        },
        {"cluster", "id"},
    )

    client.start_application(**client_kwargs)

    session.request.assert_called_with(
        "post",
        "/api/v1/servers/applications/StartApplication",
        **request_kwargs,
    )


def test_start_application_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(
        defaults={"server": httpserver.url_for("/")},
        auth=None,
    )

    session = Session(config)
    client = Client(session)

    client_kwargs = {
        "id": "id",
        "cluster": "cluster",
    }

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/servers/applications/StartApplication",
        {
            "json": {
                "id": "id",
                "cluster": "cluster",
            },
        },
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

    client_kwargs = {
        "id": "id",
        "cluster": "cluster",
    }

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

    client_kwargs = {
        "id": "id",
        "cluster": "cluster",
    }

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/servers/applications/StopApplication",
        {
            "json": {
                "id": "id",
                "cluster": "cluster",
            },
        },
        {"cluster", "id"},
    )

    client.stop_application(**client_kwargs)

    session.request.assert_called_with(
        "post",
        "/api/v1/servers/applications/StopApplication",
        **request_kwargs,
    )


def test_stop_application_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(
        defaults={"server": httpserver.url_for("/")},
        auth=None,
    )

    session = Session(config)
    client = Client(session)

    client_kwargs = {
        "id": "id",
        "cluster": "cluster",
    }

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/servers/applications/StopApplication",
        {
            "json": {
                "id": "id",
                "cluster": "cluster",
            },
        },
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

    client_kwargs = {
        "id": "id",
        "cluster": "cluster",
    }

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

    client_kwargs = {
        "id": "Id",
        "cluster": "Cluster",
    }

    request_kwargs = validate_kwargs(
        "delete",
        "/api/v1/servers/applications/DestroyApplication",
        {
            "params": {
                "Id": "Id",
                "Cluster": "Cluster",
            },
        },
        {"Id", "Cluster"},
    )

    client.destroy_application(**client_kwargs)

    session.request.assert_called_with(
        "delete",
        "/api/v1/servers/applications/DestroyApplication",
        **request_kwargs,
    )


def test_destroy_application_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(
        defaults={"server": httpserver.url_for("/")},
        auth=None,
    )

    session = Session(config)
    client = Client(session)

    client_kwargs = {
        "id": "Id",
        "cluster": "Cluster",
    }

    request_kwargs = validate_kwargs(
        "delete",
        "/api/v1/servers/applications/DestroyApplication",
        {
            "params": {
                "Id": "Id",
                "Cluster": "Cluster",
            },
        },
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

    client_kwargs = {
        "id": "Id",
        "cluster": "Cluster",
    }

    client.destroy_application(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.

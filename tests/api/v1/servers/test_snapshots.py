import pytest

from typing import Any, Dict

from unittest.mock import Mock
from pytest_httpserver import HTTPServer
from pytest_httpserver.httpserver import UNDEFINED
from werkzeug.datastructures import MultiDict

from denvr.config import Config
from denvr.session import Session
from denvr.api.v1.servers.snapshots import Client
from denvr.validate import validate_kwargs


def test_get_snapshots():
    """
    Unit test default input/output behaviour when mocking the internal Session object.
    """
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    client.get_snapshots()

    client_kwargs: Dict[str, Any] = {"cluster": "Cluster"}

    request_kwargs = validate_kwargs(
        "get", "/api/v1/servers/snapshots/GetSnapshots", {"params": {"Cluster": "Cluster"}}, {}
    )

    client.get_snapshots(**client_kwargs)

    session.request.assert_called_with(
        "get", "/api/v1/servers/snapshots/GetSnapshots", **request_kwargs
    )


def test_get_snapshots_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(defaults={"server": httpserver.url_for("/")}, auth=None)

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {"cluster": "Cluster"}

    request_kwargs = validate_kwargs(
        "get", "/api/v1/servers/snapshots/GetSnapshots", {"params": {"Cluster": "Cluster"}}, {}
    )

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/servers/snapshots/GetSnapshots",
        method="get",
        query_string=MultiDict(request_kwargs.get("params", {})),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.get_snapshots(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_get_snapshots_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {"cluster": "Cluster"}

    client.get_snapshots(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_get_snapshot():
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
            client.get_snapshot()
    else:
        client.get_snapshot()

    client_kwargs: Dict[str, Any] = {"id": "Id", "namespace": "Namespace", "cluster": "Cluster"}

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/servers/snapshots/GetSnapshot",
        {"params": {"Id": "Id", "Namespace": "Namespace", "Cluster": "Cluster"}},
        {"Id", "Namespace", "Cluster"},
    )

    client.get_snapshot(**client_kwargs)

    session.request.assert_called_with(
        "get", "/api/v1/servers/snapshots/GetSnapshot", **request_kwargs
    )


def test_get_snapshot_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(defaults={"server": httpserver.url_for("/")}, auth=None)

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {"id": "Id", "namespace": "Namespace", "cluster": "Cluster"}

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/servers/snapshots/GetSnapshot",
        {"params": {"Id": "Id", "Namespace": "Namespace", "Cluster": "Cluster"}},
        {"Id", "Namespace", "Cluster"},
    )

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/servers/snapshots/GetSnapshot",
        method="get",
        query_string=MultiDict(request_kwargs.get("params", {})),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.get_snapshot(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_get_snapshot_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {"id": "Id", "namespace": "Namespace", "cluster": "Cluster"}

    client.get_snapshot(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_create_snapshot():
    """
    Unit test default input/output behaviour when mocking the internal Session object.
    """
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    # Check that missing required arguments without a default should through a TypeError
    if any(getattr(config, k, None) is None for k in ["cluster", "namespace"]):
        with pytest.raises(TypeError, match=r"^Required"):
            client.create_snapshot()
    else:
        client.create_snapshot()

    client_kwargs: Dict[str, Any] = {
        "name": "string",
        "namespace": "string",
        "cluster": "string",
        "source_v_m_name": "string",
    }

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/servers/snapshots/CreateSnapshot",
        {
            "json": {
                "name": "string",
                "namespace": "string",
                "cluster": "string",
                "sourceVMName": "string",
            }
        },
        {"cluster", "namespace"},
    )

    client.create_snapshot(**client_kwargs)

    session.request.assert_called_with(
        "post", "/api/v1/servers/snapshots/CreateSnapshot", **request_kwargs
    )


def test_create_snapshot_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(defaults={"server": httpserver.url_for("/")}, auth=None)

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {
        "name": "string",
        "namespace": "string",
        "cluster": "string",
        "source_v_m_name": "string",
    }

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/servers/snapshots/CreateSnapshot",
        {
            "json": {
                "name": "string",
                "namespace": "string",
                "cluster": "string",
                "sourceVMName": "string",
            }
        },
        {"cluster", "namespace"},
    )

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/servers/snapshots/CreateSnapshot",
        method="post",
        query_string=MultiDict(request_kwargs.get("params", {})),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.create_snapshot(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_create_snapshot_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {
        "name": "string",
        "namespace": "string",
        "cluster": "string",
        "source_v_m_name": "string",
    }

    client.create_snapshot(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_delete_snapshot():
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
            client.delete_snapshot()
    else:
        client.delete_snapshot()

    client_kwargs: Dict[str, Any] = {"id": "Id", "namespace": "Namespace", "cluster": "Cluster"}

    request_kwargs = validate_kwargs(
        "delete",
        "/api/v1/servers/snapshots/DeleteSnapshot",
        {"params": {"Id": "Id", "Namespace": "Namespace", "Cluster": "Cluster"}},
        {"Id", "Namespace", "Cluster"},
    )

    client.delete_snapshot(**client_kwargs)

    session.request.assert_called_with(
        "delete", "/api/v1/servers/snapshots/DeleteSnapshot", **request_kwargs
    )


def test_delete_snapshot_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(defaults={"server": httpserver.url_for("/")}, auth=None)

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {"id": "Id", "namespace": "Namespace", "cluster": "Cluster"}

    request_kwargs = validate_kwargs(
        "delete",
        "/api/v1/servers/snapshots/DeleteSnapshot",
        {"params": {"Id": "Id", "Namespace": "Namespace", "Cluster": "Cluster"}},
        {"Id", "Namespace", "Cluster"},
    )

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/servers/snapshots/DeleteSnapshot",
        method="delete",
        query_string=MultiDict(request_kwargs.get("params", {})),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.delete_snapshot(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_delete_snapshot_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {"id": "Id", "namespace": "Namespace", "cluster": "Cluster"}

    client.delete_snapshot(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.

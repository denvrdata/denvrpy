import pytest

from pytest_httpserver import HTTPServer
from denvr.config import Config
from denvr.session import Session
from denvr.api.v1.servers import applications, virtual
from typing import Any, Dict
from denvr.waiters import waiter, Waiter


def test_waiter_timeout():
    log = []

    def cleanup(x):
        log.append(x)

    with pytest.raises(TimeoutError):
        Waiter(action=lambda: "Failed Action", check=lambda x: (False, x), cleanup=cleanup)(
            interval=0.01, timeout=0.5
        )

    assert log == ["Failed Action"]


def test_unknown_waiter_operation():
    x = "foo"

    with pytest.raises(ValueError, match="Operation must be a method of a client."):
        waiter(lambda x: x)

    with pytest.raises(ValueError, match="Unsupported operation:"):
        waiter(x.endswith)


def test_vm_start_server(httpserver: HTTPServer):
    config = Config(defaults={"server": httpserver.url_for("/")}, auth=None)
    session = Session(config)
    client = virtual.Client(session)

    kwargs: Dict[str, Any] = {
        "id": "vm-2024093009357617",
        "namespace": "denvr",
        "cluster": "Hou1",
    }

    httpserver.expect_ordered_request("/api/v1/servers/virtual/StartServer").respond_with_json(
        kwargs
    )
    httpserver.expect_ordered_request("/api/v1/servers/virtual/GetServer").respond_with_json(
        {"status": "PENDING"}
    )
    httpserver.expect_ordered_request("/api/v1/servers/virtual/GetServer").respond_with_json(
        {"status": "PENDING"}
    )
    httpserver.expect_ordered_request("/api/v1/servers/virtual/GetServer").respond_with_json(
        {"status": "ONLINE"}
    )

    start_server = waiter(client.start_server)
    result = start_server(interval=0.01, **kwargs)
    assert result["status"] == "ONLINE"


def test_vm_stop_server(httpserver: HTTPServer):
    config = Config(defaults={"server": httpserver.url_for("/")}, auth=None)
    session = Session(config)
    client = virtual.Client(session)

    kwargs: Dict[str, Any] = {
        "id": "vm-2024093009357617",
        "namespace": "denvr",
        "cluster": "Hou1",
    }

    httpserver.expect_ordered_request("/api/v1/servers/virtual/StopServer").respond_with_json(
        kwargs
    )
    httpserver.expect_ordered_request("/api/v1/servers/virtual/GetServer").respond_with_json(
        {"status": "PENDING"}
    )
    httpserver.expect_ordered_request("/api/v1/servers/virtual/GetServer").respond_with_json(
        {"status": "PENDING"}
    )
    httpserver.expect_ordered_request("/api/v1/servers/virtual/GetServer").respond_with_json(
        {"status": "OFFLINE"}
    )

    stop_server = waiter(client.stop_server)
    result = stop_server(interval=0.01, **kwargs)
    assert result["status"] == "OFFLINE"


def test_app_start_application(httpserver: HTTPServer):
    config = Config(defaults={"server": httpserver.url_for("/")}, auth=None)
    session = Session(config)
    client = applications.Client(session)

    kwargs: Dict[str, Any] = {"id": "app-2024093009357617", "cluster": "Hou1"}

    httpserver.expect_ordered_request(
        "/api/v1/servers/applications/StartApplication"
    ).respond_with_json(kwargs)
    httpserver.expect_ordered_request(
        "/api/v1/servers/applications/GetApplicationDetails"
    ).respond_with_json({"instance_details": {"status": "PENDING"}})
    httpserver.expect_ordered_request(
        "/api/v1/servers/applications/GetApplicationDetails"
    ).respond_with_json({"instance_details": {"status": "PENDING"}})
    httpserver.expect_ordered_request(
        "/api/v1/servers/applications/GetApplicationDetails"
    ).respond_with_json({"instance_details": {"status": "ONLINE"}})

    start_application = waiter(client.start_application)
    result = start_application(interval=0.01, **kwargs)
    assert result["instance_details"]["status"] == "ONLINE"


def test_app_stop_application(httpserver: HTTPServer):
    config = Config(defaults={"server": httpserver.url_for("/")}, auth=None)
    session = Session(config)
    client = applications.Client(session)

    kwargs: Dict[str, Any] = {"id": "vm-2024093009357617", "cluster": "Hou1"}

    httpserver.expect_ordered_request(
        "/api/v1/servers/applications/StopApplication"
    ).respond_with_json(kwargs)
    httpserver.expect_ordered_request(
        "/api/v1/servers/applications/GetApplicationDetails"
    ).respond_with_json({"instance_details": {"status": "PENDING"}})
    httpserver.expect_ordered_request(
        "/api/v1/servers/applications/GetApplicationDetails"
    ).respond_with_json({"instance_details": {"status": "PENDING"}})
    httpserver.expect_ordered_request(
        "/api/v1/servers/applications/GetApplicationDetails"
    ).respond_with_json({"instance_details": {"status": "OFFLINE"}})

    stop_application = waiter(client.stop_application)
    result = stop_application(interval=0.01, **kwargs)
    assert result["instance_details"]["status"] == "OFFLINE"

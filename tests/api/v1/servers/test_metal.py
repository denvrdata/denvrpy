import pytest

from typing import Any, Dict

from unittest.mock import Mock
from pytest_httpserver import HTTPServer
from pytest_httpserver.httpserver import UNDEFINED

from denvr.config import Config
from denvr.session import Session
from denvr.api.v1.servers.metal import Client
from denvr.validate import validate_kwargs


def test_get_host():
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
            client.get_host()
    else:
        client.get_host()

    client_kwargs: Dict[str, Any] = {"id": "Id", "cluster": "Hou1"}

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/servers/metal/GetHost",
        {"params": {"Id": "Id", "Cluster": "Hou1"}},
        {"Id", "Cluster"},
    )

    client.get_host(**client_kwargs)

    session.request.assert_called_with("get", "/api/v1/servers/metal/GetHost", **request_kwargs)


def test_get_host_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(defaults={"server": httpserver.url_for("/")}, auth=None)

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {"id": "Id", "cluster": "Hou1"}

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/servers/metal/GetHost",
        {"params": {"Id": "Id", "Cluster": "Hou1"}},
        {"Id", "Cluster"},
    )

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/servers/metal/GetHost",
        method="get",
        query_string=request_kwargs.get("params", None),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.get_host(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_get_host_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {"id": "Id", "cluster": "Hou1"}

    client.get_host(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_get_hosts():
    """
    Unit test default input/output behaviour when mocking the internal Session object.
    """
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    client.get_hosts()

    client_kwargs: Dict[str, Any] = {"cluster": "Hou1"}

    request_kwargs = validate_kwargs(
        "get", "/api/v1/servers/metal/GetHosts", {"params": {"Cluster": "Hou1"}}, {}
    )

    client.get_hosts(**client_kwargs)

    session.request.assert_called_with(
        "get", "/api/v1/servers/metal/GetHosts", **request_kwargs
    )


def test_get_hosts_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(defaults={"server": httpserver.url_for("/")}, auth=None)

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {"cluster": "Hou1"}

    request_kwargs = validate_kwargs(
        "get", "/api/v1/servers/metal/GetHosts", {"params": {"Cluster": "Hou1"}}, {}
    )

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/servers/metal/GetHosts",
        method="get",
        query_string=request_kwargs.get("params", None),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.get_hosts(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_get_hosts_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {"cluster": "Hou1"}

    client.get_hosts(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_reboot_host():
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
            client.reboot_host()
    else:
        client.reboot_host()

    client_kwargs: Dict[str, Any] = {"id": "string", "cluster": "Hou1"}

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/servers/metal/RebootHost",
        {"json": {"id": "string", "cluster": "Hou1"}},
        {"cluster", "id"},
    )

    client.reboot_host(**client_kwargs)

    session.request.assert_called_with(
        "post", "/api/v1/servers/metal/RebootHost", **request_kwargs
    )


def test_reboot_host_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(defaults={"server": httpserver.url_for("/")}, auth=None)

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {"id": "string", "cluster": "Hou1"}

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/servers/metal/RebootHost",
        {"json": {"id": "string", "cluster": "Hou1"}},
        {"cluster", "id"},
    )

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/servers/metal/RebootHost",
        method="post",
        query_string=request_kwargs.get("params", None),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.reboot_host(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_reboot_host_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {"id": "string", "cluster": "Hou1"}

    client.reboot_host(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_reprovision_host():
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
            client.reprovision_host()
    else:
        client.reprovision_host()

    client_kwargs: Dict[str, Any] = {
        "image_url": "https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64.img",
        "image_checksum": "https://cloud-images.ubuntu.com/jammy/current/MD5SUMS",
        "cloud_init_base64": "SGVsbG8sIFdvcmxkIQ==",
        "id": "string",
        "cluster": "Hou1",
    }

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/servers/metal/ReprovisionHost",
        {
            "json": {
                "imageUrl": "https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64.img",
                "imageChecksum": "https://cloud-images.ubuntu.com/jammy/current/MD5SUMS",
                "cloudInitBase64": "SGVsbG8sIFdvcmxkIQ==",
                "id": "string",
                "cluster": "Hou1",
            }
        },
        {"cluster", "id"},
    )

    client.reprovision_host(**client_kwargs)

    session.request.assert_called_with(
        "post", "/api/v1/servers/metal/ReprovisionHost", **request_kwargs
    )


def test_reprovision_host_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(defaults={"server": httpserver.url_for("/")}, auth=None)

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {
        "image_url": "https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64.img",
        "image_checksum": "https://cloud-images.ubuntu.com/jammy/current/MD5SUMS",
        "cloud_init_base64": "SGVsbG8sIFdvcmxkIQ==",
        "id": "string",
        "cluster": "Hou1",
    }

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/servers/metal/ReprovisionHost",
        {
            "json": {
                "imageUrl": "https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64.img",
                "imageChecksum": "https://cloud-images.ubuntu.com/jammy/current/MD5SUMS",
                "cloudInitBase64": "SGVsbG8sIFdvcmxkIQ==",
                "id": "string",
                "cluster": "Hou1",
            }
        },
        {"cluster", "id"},
    )

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/servers/metal/ReprovisionHost",
        method="post",
        query_string=request_kwargs.get("params", None),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.reprovision_host(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_reprovision_host_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {
        "image_url": "https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64.img",
        "image_checksum": "https://cloud-images.ubuntu.com/jammy/current/MD5SUMS",
        "cloud_init_base64": "SGVsbG8sIFdvcmxkIQ==",
        "id": "string",
        "cluster": "Hou1",
    }

    client.reprovision_host(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.

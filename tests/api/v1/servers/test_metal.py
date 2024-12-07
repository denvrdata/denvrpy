from unittest.mock import Mock

import pytest
from pytest_httpserver import HTTPServer
from pytest_httpserver.httpserver import UNDEFINED

from denvr.api.v1.servers.metal import Client
from denvr.config import Config
from denvr.session import Session
from denvr.validate import validate_kwargs


def test_get_hosts():
    """
    Unit test default input/output behaviour when mocking the internal Session object.
    """
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    client.get_hosts()

    client_kwargs = {
        "cluster": "Cluster",
    }

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/servers/metal/GetHosts",
        {
            "params": {
                "Cluster": "Cluster",
            },
        },
        {},
    )

    client.get_hosts(**client_kwargs)

    session.request.assert_called_with(
        "get",
        "/api/v1/servers/metal/GetHosts",
        **request_kwargs,
    )


def test_get_hosts_httpserver(httpserver: HTTPServer):
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
        "cluster": "Cluster",
    }

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/servers/metal/GetHosts",
        {
            "params": {
                "Cluster": "Cluster",
            },
        },
        {},
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

    client_kwargs = {
        "cluster": "Cluster",
    }

    client.get_hosts(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


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

    client_kwargs = {
        "id": "Id",
        "cluster": "Cluster",
    }

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/servers/metal/GetHost",
        {
            "params": {
                "Id": "Id",
                "Cluster": "Cluster",
            },
        },
        {"Id", "Cluster"},
    )

    client.get_host(**client_kwargs)

    session.request.assert_called_with(
        "get",
        "/api/v1/servers/metal/GetHost",
        **request_kwargs,
    )


def test_get_host_httpserver(httpserver: HTTPServer):
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
        "/api/v1/servers/metal/GetHost",
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

    client_kwargs = {
        "id": "Id",
        "cluster": "Cluster",
    }

    client.get_host(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_add_host_vpc():
    """
    Unit test default input/output behaviour when mocking the internal Session object.
    """
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

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/servers/metal/AddHostVpc",
        {
            "json": {
                "id": "id",
                "cluster": "cluster",
                "vpcId": "vpcId",
            },
        },
        {"cluster", "id", "vpcId"},
    )

    client.add_host_vpc(**client_kwargs)

    session.request.assert_called_with(
        "post",
        "/api/v1/servers/metal/AddHostVpc",
        **request_kwargs,
    )


def test_add_host_vpc_httpserver(httpserver: HTTPServer):
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
        "vpc_id": "vpcId",
    }

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/servers/metal/AddHostVpc",
        {
            "json": {
                "id": "id",
                "cluster": "cluster",
                "vpcId": "vpcId",
            },
        },
        {"cluster", "id", "vpcId"},
    )

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/servers/metal/AddHostVpc",
        method="post",
        query_string=request_kwargs.get("params", None),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.add_host_vpc(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_add_host_vpc_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
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
    """
    Unit test default input/output behaviour when mocking the internal Session object.
    """
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

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/servers/metal/RemoveHostVpc",
        {
            "json": {
                "id": "id",
                "cluster": "cluster",
                "vpcId": "vpcId",
            },
        },
        {"cluster", "id", "vpcId"},
    )

    client.remove_host_vpc(**client_kwargs)

    session.request.assert_called_with(
        "post",
        "/api/v1/servers/metal/RemoveHostVpc",
        **request_kwargs,
    )


def test_remove_host_vpc_httpserver(httpserver: HTTPServer):
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
        "vpc_id": "vpcId",
    }

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/servers/metal/RemoveHostVpc",
        {
            "json": {
                "id": "id",
                "cluster": "cluster",
                "vpcId": "vpcId",
            },
        },
        {"cluster", "id", "vpcId"},
    )

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/servers/metal/RemoveHostVpc",
        method="post",
        query_string=request_kwargs.get("params", None),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.remove_host_vpc(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_remove_host_vpc_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
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

    client_kwargs = {
        "id": "id",
        "cluster": "cluster",
    }

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/servers/metal/RebootHost",
        {
            "json": {
                "id": "id",
                "cluster": "cluster",
            },
        },
        {"cluster", "id"},
    )

    client.reboot_host(**client_kwargs)

    session.request.assert_called_with(
        "post",
        "/api/v1/servers/metal/RebootHost",
        **request_kwargs,
    )


def test_reboot_host_httpserver(httpserver: HTTPServer):
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
        "/api/v1/servers/metal/RebootHost",
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

    client_kwargs = {
        "id": "id",
        "cluster": "cluster",
    }

    client.reboot_host(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.

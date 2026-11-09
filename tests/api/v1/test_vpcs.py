import pytest

from typing import Any, Dict

from unittest.mock import Mock
from pytest_httpserver import HTTPServer
from pytest_httpserver.httpserver import UNDEFINED
from werkzeug.datastructures import MultiDict

from denvr.config import Config
from denvr.session import Session
from denvr.api.v1.vpcs import Client
from denvr.validate import validate_kwargs


def test_get_vpcs():
    """
    Unit test default input/output behaviour when mocking the internal Session object.
    """
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    client.get_vpcs()

    client_kwargs: Dict[str, Any] = {"cluster": "cluster"}

    request_kwargs = validate_kwargs(
        "get", "/api/v1/vpcs/GetVpcs", {"params": {"cluster": "cluster"}}, {}
    )

    client.get_vpcs(**client_kwargs)

    session.request.assert_called_with("get", "/api/v1/vpcs/GetVpcs", **request_kwargs)


def test_get_vpcs_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(defaults={"server": httpserver.url_for("/")}, auth=None)

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {"cluster": "cluster"}

    request_kwargs = validate_kwargs(
        "get", "/api/v1/vpcs/GetVpcs", {"params": {"cluster": "cluster"}}, {}
    )

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/vpcs/GetVpcs",
        method="get",
        query_string=MultiDict(request_kwargs.get("params", {})),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.get_vpcs(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_get_vpcs_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {"cluster": "cluster"}

    client.get_vpcs(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_get_vpc():
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
            client.get_vpc()
    else:
        client.get_vpc()

    client_kwargs: Dict[str, Any] = {"id": "Id", "cluster": "Msc1"}

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/vpcs/GetVpc",
        {"params": {"Id": "Id", "Cluster": "Msc1"}},
        {"Id", "Cluster"},
    )

    client.get_vpc(**client_kwargs)

    session.request.assert_called_with("get", "/api/v1/vpcs/GetVpc", **request_kwargs)


def test_get_vpc_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(defaults={"server": httpserver.url_for("/")}, auth=None)

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {"id": "Id", "cluster": "Msc1"}

    request_kwargs = validate_kwargs(
        "get",
        "/api/v1/vpcs/GetVpc",
        {"params": {"Id": "Id", "Cluster": "Msc1"}},
        {"Id", "Cluster"},
    )

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/vpcs/GetVpc",
        method="get",
        query_string=MultiDict(request_kwargs.get("params", {})),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.get_vpc(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_get_vpc_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {"id": "Id", "cluster": "Msc1"}

    client.get_vpc(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_create_vpc():
    """
    Unit test default input/output behaviour when mocking the internal Session object.
    """
    config = Config(defaults={}, auth=None)

    session = Mock()
    session.config = config
    client = Client(session)

    # Check that missing required arguments without a default should through a TypeError
    if any(getattr(config, k, None) is None for k in ["cluster", "name"]):
        with pytest.raises(TypeError, match=r"^Required"):
            client.create_vpc()
    else:
        client.create_vpc()

    client_kwargs: Dict[str, Any] = {
        "name": "string",
        "block_intra_vpc_comms": False,
        "is_default": False,
        "cluster": "Msc1",
    }

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/vpcs/CreateVpc",
        {
            "json": {
                "name": "string",
                "blockIntraVpcComms": False,
                "isDefault": False,
                "cluster": "Msc1",
            }
        },
        {"cluster", "name"},
    )

    client.create_vpc(**client_kwargs)

    session.request.assert_called_with("post", "/api/v1/vpcs/CreateVpc", **request_kwargs)


def test_create_vpc_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(defaults={"server": httpserver.url_for("/")}, auth=None)

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {
        "name": "string",
        "block_intra_vpc_comms": False,
        "is_default": False,
        "cluster": "Msc1",
    }

    request_kwargs = validate_kwargs(
        "post",
        "/api/v1/vpcs/CreateVpc",
        {
            "json": {
                "name": "string",
                "blockIntraVpcComms": False,
                "isDefault": False,
                "cluster": "Msc1",
            }
        },
        {"cluster", "name"},
    )

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/vpcs/CreateVpc",
        method="post",
        query_string=MultiDict(request_kwargs.get("params", {})),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.create_vpc(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_create_vpc_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {
        "name": "string",
        "block_intra_vpc_comms": False,
        "is_default": False,
        "cluster": "Msc1",
    }

    client.create_vpc(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.


def test_destroy_vpc():
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
            client.destroy_vpc()
    else:
        client.destroy_vpc()

    client_kwargs: Dict[str, Any] = {"id": "Id", "cluster": "Msc1"}

    request_kwargs = validate_kwargs(
        "delete",
        "/api/v1/vpcs/DestroyVpc",
        {"params": {"Id": "Id", "Cluster": "Msc1"}},
        {"Id", "Cluster"},
    )

    client.destroy_vpc(**client_kwargs)

    session.request.assert_called_with("delete", "/api/v1/vpcs/DestroyVpc", **request_kwargs)


def test_destroy_vpc_httpserver(httpserver: HTTPServer):
    """
    Test we're producing valid session HTTP requests
    """
    config = Config(defaults={"server": httpserver.url_for("/")}, auth=None)

    session = Session(config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {"id": "Id", "cluster": "Msc1"}

    request_kwargs = validate_kwargs(
        "delete",
        "/api/v1/vpcs/DestroyVpc",
        {"params": {"Id": "Id", "Cluster": "Msc1"}},
        {"Id", "Cluster"},
    )

    # TODO: The request_kwargs response may break if we add schema validation on results.
    httpserver.expect_request(
        "/api/v1/vpcs/DestroyVpc",
        method="delete",
        query_string=MultiDict(request_kwargs.get("params", {})),
        json=request_kwargs.get("json", UNDEFINED),
    ).respond_with_json(request_kwargs)
    assert client.destroy_vpc(**client_kwargs) == request_kwargs


@pytest.mark.integration
def test_destroy_vpc_mockserver(mock_config):
    """
    Test our requests/responses match the open api spec with mockserver.
    """
    session = Session(mock_config)
    client = Client(session)

    client_kwargs: Dict[str, Any] = {"id": "Id", "cluster": "Msc1"}

    client.destroy_vpc(**client_kwargs)
    # TODO: Test return type once we add support for that in our genapi script.

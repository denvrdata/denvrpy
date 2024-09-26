from unittest.mock import Mock

from denvr.api.v1.servers.metal import Client


def test_get_hosts():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.get_hosts()

    kwargs = {
        "params": {
            "cluster": None,
        },
    }

    client.get_hosts(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "get",
        "/api/v1/servers/metal/GetHosts",
        **kwargs,
    )
    session.reset_mock()

    kwargs = {
        "params": {
            "cluster": "cluster",
        },
    }

    client.get_hosts(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "get",
        "/api/v1/servers/metal/GetHosts",
        **kwargs,
    )


def test_get_host():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.get_host()

    kwargs = {
        "params": {
            "id": None,
            "cluster": None,
        },
    }

    client.get_host(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "get",
        "/api/v1/servers/metal/GetHost",
        **kwargs,
    )
    session.reset_mock()

    kwargs = {
        "params": {
            "id": "id",
            "cluster": "cluster",
        },
    }

    client.get_host(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "get",
        "/api/v1/servers/metal/GetHost",
        **kwargs,
    )


def test_add_host_vpc():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.add_host_vpc()

    kwargs = {
        "json": {
            "id": None,
            "cluster": None,
            "vpc_id": None,
        },
    }

    client.add_host_vpc(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "post",
        "/api/v1/servers/metal/AddHostVpc",
        **kwargs,
    )
    session.reset_mock()

    kwargs = {
        "json": {
            "id": "id",
            "cluster": "cluster",
            "vpc_id": "vpc_id",
        },
    }

    client.add_host_vpc(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "post",
        "/api/v1/servers/metal/AddHostVpc",
        **kwargs,
    )


def test_remove_host_vpc():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.remove_host_vpc()

    kwargs = {
        "json": {
            "id": None,
            "cluster": None,
            "vpc_id": None,
        },
    }

    client.remove_host_vpc(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "post",
        "/api/v1/servers/metal/RemoveHostVpc",
        **kwargs,
    )
    session.reset_mock()

    kwargs = {
        "json": {
            "id": "id",
            "cluster": "cluster",
            "vpc_id": "vpc_id",
        },
    }

    client.remove_host_vpc(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "post",
        "/api/v1/servers/metal/RemoveHostVpc",
        **kwargs,
    )


def test_reboot_host():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.reboot_host()

    kwargs = {
        "json": {
            "id": None,
            "cluster": None,
        },
    }

    client.reboot_host(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "post",
        "/api/v1/servers/metal/RebootHost",
        **kwargs,
    )
    session.reset_mock()

    kwargs = {
        "json": {
            "id": "id",
            "cluster": "cluster",
        },
    }

    client.reboot_host(
        **kwargs.get("params", {}),
        **kwargs.get("json", {}),
    )

    session.request.assert_called_with(
        "post",
        "/api/v1/servers/metal/RebootHost",
        **kwargs,
    )

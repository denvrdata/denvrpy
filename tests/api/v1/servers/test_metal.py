from unittest.mock import Mock

from denvr.api.v1.servers.metal import Client


def test_get_hosts():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.get_hosts()

    client_kwargs = {
        "cluster": None,
    }
    request_kwargs = {
        "params": {
            "Cluster": None,
        },
    }

    client.get_hosts(**client_kwargs)

    session.request.assert_called_with("get", "/api/v1/servers/metal/GetHosts", **request_kwargs)
    session.reset_mock()

    client_kwargs = {
        "cluster": "Cluster",
    }

    request_kwargs = {
        "params": {
            "Cluster": "Cluster",
        },
    }

    client.get_hosts(**client_kwargs)

    session.request.assert_called_with(
        "get",
        "/api/v1/servers/metal/GetHosts",
        **request_kwargs,
    )


def test_get_host():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.get_host()

    client_kwargs = {
        "id": None,
        "cluster": None,
    }
    request_kwargs = {
        "params": {
            "Id": None,
            "Cluster": None,
        },
    }

    client.get_host(**client_kwargs)

    session.request.assert_called_with("get", "/api/v1/servers/metal/GetHost", **request_kwargs)
    session.reset_mock()

    client_kwargs = {
        "id": "Id",
        "cluster": "Cluster",
    }

    request_kwargs = {
        "params": {
            "Id": "Id",
            "Cluster": "Cluster",
        },
    }

    client.get_host(**client_kwargs)

    session.request.assert_called_with(
        "get",
        "/api/v1/servers/metal/GetHost",
        **request_kwargs,
    )


def test_add_host_vpc():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.add_host_vpc()

    client_kwargs = {
        "id": None,
        "cluster": None,
        "vpc_id": None,
    }
    request_kwargs = {
        "json": {
            "id": None,
            "cluster": None,
            "vpcId": None,
        },
    }

    client.add_host_vpc(**client_kwargs)

    session.request.assert_called_with("post", "/api/v1/servers/metal/AddHostVpc", **request_kwargs)
    session.reset_mock()

    client_kwargs = {
        "id": "id",
        "cluster": "cluster",
        "vpc_id": "vpcId",
    }

    request_kwargs = {
        "json": {
            "id": "id",
            "cluster": "cluster",
            "vpcId": "vpcId",
        },
    }

    client.add_host_vpc(**client_kwargs)

    session.request.assert_called_with(
        "post",
        "/api/v1/servers/metal/AddHostVpc",
        **request_kwargs,
    )


def test_remove_host_vpc():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.remove_host_vpc()

    client_kwargs = {
        "id": None,
        "cluster": None,
        "vpc_id": None,
    }
    request_kwargs = {
        "json": {
            "id": None,
            "cluster": None,
            "vpcId": None,
        },
    }

    client.remove_host_vpc(**client_kwargs)

    session.request.assert_called_with("post", "/api/v1/servers/metal/RemoveHostVpc", **request_kwargs)
    session.reset_mock()

    client_kwargs = {
        "id": "id",
        "cluster": "cluster",
        "vpc_id": "vpcId",
    }

    request_kwargs = {
        "json": {
            "id": "id",
            "cluster": "cluster",
            "vpcId": "vpcId",
        },
    }

    client.remove_host_vpc(**client_kwargs)

    session.request.assert_called_with(
        "post",
        "/api/v1/servers/metal/RemoveHostVpc",
        **request_kwargs,
    )


def test_reboot_host():
    session = Mock()
    client = Client(session)

    # This case will fail for a real session, but
    # might as well test that it doesn't fail on the generated
    # code.
    client.reboot_host()

    client_kwargs = {
        "id": None,
        "cluster": None,
    }
    request_kwargs = {
        "json": {
            "id": None,
            "cluster": None,
        },
    }

    client.reboot_host(**client_kwargs)

    session.request.assert_called_with("post", "/api/v1/servers/metal/RebootHost", **request_kwargs)
    session.reset_mock()

    client_kwargs = {
        "id": "id",
        "cluster": "cluster",
    }

    request_kwargs = {
        "json": {
            "id": "id",
            "cluster": "cluster",
        },
    }

    client.reboot_host(**client_kwargs)

    session.request.assert_called_with(
        "post",
        "/api/v1/servers/metal/RebootHost",
        **request_kwargs,
    )

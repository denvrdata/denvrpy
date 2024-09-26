from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from denvr.session import Session


class Client:
    def __init__(self, session: Session):
        self.session = session

    def get_hosts(
        self,
        cluster: str | None = None,
    ):
        """Get a list of metal hosts"""
        kwargs = {
            "params": {
                "cluster": cluster,
            },
        }

        return self.session.request(
            "get",
            "/api/v1/servers/metal/GetHosts",
            **kwargs,
        )

    def get_host(
        self,
        id: str | None = None,
        cluster: str | None = None,
    ):
        """Get detailed information about a specific metal host"""
        kwargs = {
            "params": {
                "id": id,
                "cluster": cluster,
            },
        }

        return self.session.request(
            "get",
            "/api/v1/servers/metal/GetHost",
            **kwargs,
        )

    def add_host_vpc(
        self,
        id: str | None = None,
        cluster: str | None = None,
        vpc_id: str | None = None,
    ):
        """Add metal host to VPC"""
        kwargs = {
            "json": {
                "id": id,
                "cluster": cluster,
                "vpc_id": vpc_id,
            },
        }

        return self.session.request(
            "post",
            "/api/v1/servers/metal/AddHostVpc",
            **kwargs,
        )

    def remove_host_vpc(
        self,
        id: str | None = None,
        cluster: str | None = None,
        vpc_id: str | None = None,
    ):
        """Remove metal host from VPC"""
        kwargs = {
            "json": {
                "id": id,
                "cluster": cluster,
                "vpc_id": vpc_id,
            },
        }

        return self.session.request(
            "post",
            "/api/v1/servers/metal/RemoveHostVpc",
            **kwargs,
        )

    def reboot_host(
        self,
        id: str | None = None,
        cluster: str | None = None,
    ):
        """Reboot the metal host"""
        kwargs = {
            "json": {
                "id": id,
                "cluster": cluster,
            },
        }

        return self.session.request(
            "post",
            "/api/v1/servers/metal/RebootHost",
            **kwargs,
        )
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from denvr.session import Session


class Client:
    def __init__(self, session: Session):
        self.session = session

    def get_vpcs(
        self,
        cluster: str | None = None,
    ):
        """Get a list of VPCs"""
        kwargs = {
            "params": {
                "Cluster": cluster,
            },
        }

        return self.session.request(
            "get",
            "/api/v1/vpcs/GetVpcs",
            **kwargs,
        )

    def get_vpc(
        self,
        id: str | None = None,
        cluster: str | None = None,
    ):
        """Get detailed information about a specific VPC"""
        kwargs = {
            "params": {
                "Id": id,
                "Cluster": cluster,
            },
        }

        return self.session.request(
            "get",
            "/api/v1/vpcs/GetVpc",
            **kwargs,
        )

    def create_vpc(
        self,
        id: str | None = None,
        cluster: str | None = None,
    ):
        """Create a new VPC"""
        kwargs = {
            "json": {
                "id": id,
                "cluster": cluster,
            },
        }

        return self.session.request(
            "post",
            "/api/v1/vpcs/CreateVpc",
            **kwargs,
        )

    def destroy_vpc(
        self,
        id: str | None = None,
        cluster: str | None = None,
    ):
        """Destroy a VPC"""
        kwargs = {
            "params": {
                "Id": id,
                "Cluster": cluster,
            },
        }

        return self.session.request(
            "delete",
            "/api/v1/vpcs/DestroyVpc",
            **kwargs,
        )

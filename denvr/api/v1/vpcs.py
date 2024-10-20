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
        """
        Get a list of VPCs

        Keyword Arguments:
            cluster (str)
        """
        kwargs = {
            "params": {
                "Cluster": cluster if cluster else getattr(self.session.config, "cluster", None),
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
        """
        Get detailed information about a specific VPC

        Keyword Arguments:
            id (str): Unique identifier for a resource within the cluster (ex: vm-2024093009357617)
            cluster (str): The cluster you're operating on (ex: Msc1)
        """
        kwargs = {
            "params": {
                "Id": id if id else getattr(self.session.config, "id", None),
                "Cluster": cluster if cluster else getattr(self.session.config, "cluster", None),
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
        """
        Create a new VPC

        Keyword Arguments:
            id (str): Unique identifier for a resource within the cluster (ex: vm-2024093009357617)
            cluster (str): The cluster you're operating on (ex: Msc1)
        """
        kwargs = {
            "json": {
                "id": id if id else getattr(self.session.config, "id", None),
                "cluster": cluster if cluster else getattr(self.session.config, "cluster", None),
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
        """
        Destroy a VPC

        Keyword Arguments:
            id (str): Unique identifier for a resource within the cluster (ex: vm-2024093009357617)
            cluster (str): The cluster you're operating on (ex: Msc1)
        """
        kwargs = {
            "params": {
                "Id": id if id else getattr(self.session.config, "id", None),
                "Cluster": cluster if cluster else getattr(self.session.config, "cluster", None),
            },
        }

        return self.session.request(
            "delete",
            "/api/v1/vpcs/DestroyVpc",
            **kwargs,
        )

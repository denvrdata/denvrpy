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
        """
        Get a list of bare metal hosts in a cluster

        Keyword Arguments:
            cluster (str)

        Returns:
            (dict):
                id (str)
                cluster (str)
                hostType (str)
                username (str)
                tenancyName (str)
                gpuType (str)
                gpus (int)
                vcpus (int)
                vcpuType (str)
                memory (int)
                ip (str)
                privateIp (str)
                imageId (str)
                image (str)
                storage (int)
                storageClass (str)
                vpcId (str)
                reservation (str)
                reservationExpiry (str)
                status (str)
        """
        kwargs = {
            "params": {
                "Cluster": cluster if cluster else getattr(self.session.config, "cluster", None),
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
        """
        Get detailed information about a specific metal host

        Keyword Arguments:
            id (str): Unique identifier for a resource within the cluster (ex: vm-2024093009357617)
            cluster (str): The cluster you're operating on (ex: Msc1)

        Returns:
            (dict):
                id (str)
                cluster (str)
                hostType (str)
                username (str)
                tenancyName (str)
                gpuType (str)
                gpus (int)
                vcpus (int)
                vcpuType (str)
                memory (int)
                ip (str)
                privateIp (str)
                imageId (str)
                image (str)
                storage (int)
                storageClass (str)
                vpcId (str)
                reservation (str)
                reservationExpiry (str)
                status (str)
        """
        kwargs = {
            "params": {
                "Id": id if id else getattr(self.session.config, "id", None),
                "Cluster": cluster if cluster else getattr(self.session.config, "cluster", None),
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
        """
        Add metal host to VPC

        Keyword Arguments:
            id (str): The bare metal node id (ex: denvrbm-128)
            cluster (str): The cluster where the bare metal node and vpc live (ex: Hou1)
            vpc_id (str): The id of the VPC (ex: denvr-vpc)

        Returns:
            (dict):
                id (str)
                cluster (str)
                hostType (str)
                username (str)
                tenancyName (str)
                gpuType (str)
                gpus (int)
                vcpus (int)
                vcpuType (str)
                memory (int)
                ip (str)
                privateIp (str)
                imageId (str)
                image (str)
                storage (int)
                storageClass (str)
                vpcId (str)
                reservation (str)
                reservationExpiry (str)
                status (str)
        """
        kwargs = {
            "json": {
                "id": id if id else getattr(self.session.config, "id", None),
                "cluster": cluster if cluster else getattr(self.session.config, "cluster", None),
                "vpcId": vpc_id if vpc_id else getattr(self.session.config, "vpc_id", None),
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
        """
        Remove metal host from VPC

        Keyword Arguments:
            id (str): The bare metal node id (ex: denvrbm-128)
            cluster (str): The cluster where the bare metal node and vpc live (ex: Hou1)
            vpc_id (str): The id of the VPC (ex: denvr-vpc)

        Returns:
            (dict):
                id (str)
                cluster (str)
                hostType (str)
                username (str)
                tenancyName (str)
                gpuType (str)
                gpus (int)
                vcpus (int)
                vcpuType (str)
                memory (int)
                ip (str)
                privateIp (str)
                imageId (str)
                image (str)
                storage (int)
                storageClass (str)
                vpcId (str)
                reservation (str)
                reservationExpiry (str)
                status (str)
        """
        kwargs = {
            "json": {
                "id": id if id else getattr(self.session.config, "id", None),
                "cluster": cluster if cluster else getattr(self.session.config, "cluster", None),
                "vpcId": vpc_id if vpc_id else getattr(self.session.config, "vpc_id", None),
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
        """
        Reboot the metal host

        Keyword Arguments:
            id (str): Unique identifier for a resource within the cluster (ex: vm-2024093009357617)
            cluster (str): The cluster you're operating on (ex: Msc1)

        Returns:
            (dict):
                id (str)
                cluster (str)
                hostType (str)
                username (str)
                tenancyName (str)
                gpuType (str)
                gpus (int)
                vcpus (int)
                vcpuType (str)
                memory (int)
                ip (str)
                privateIp (str)
                imageId (str)
                image (str)
                storage (int)
                storageClass (str)
                vpcId (str)
                reservation (str)
                reservationExpiry (str)
                status (str)
        """
        kwargs = {
            "json": {
                "id": id if id else getattr(self.session.config, "id", None),
                "cluster": cluster if cluster else getattr(self.session.config, "cluster", None),
            },
        }

        return self.session.request(
            "post",
            "/api/v1/servers/metal/RebootHost",
            **kwargs,
        )

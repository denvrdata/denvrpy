from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from denvr.session import Session


class Client:
    def __init__(self, session: Session):
        self.session = session

    def get_hosts(
        self,
        *,
        cluster: str | None = None,
    ):
        """
        Get a list of bare metal hosts in a cluster

        Keyword Arguments:
            cluster (str)

        Returns:
            (dict):
                id (str): The bare metal node id (ex: denvrbm-128)
                cluster (str): The cluster where the bare metal host is allocated (ex: Msc1)
                hostType (str): The specific host node type (ex: nvidia.com/A100PCIE40GB)
                username (str): The username tied to the host (ex: admin)
                tenancyName (str): Name of the tenant where the node has been allocated (ex: denvr)
                gpuType (str)
                gpus (int): Number of GPUs attached to the host (ex: 8)
                vcpus (int): Number of vCPUs on the host (ex: 120)
                vcpuType (str)
                memory (int): Amount of system memory available in GB (ex: 940)
                ip (str): The public IP address of the host (ex: 123.45.67.89)
                privateIp (str): The private IP address of the host (ex: 120.77.3.21)
                imageId (str)
                image (str)
                storage (int): The amount of storage attached to the host in GB (ex: 13600)
                storageClass (str)
                vpcId (str)
                reservation (str)
                reservationExpiry (str)
                status (str): The host status code (e.g., 'offline', 'pending', 'online'
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
        *,
        id: str,
        cluster: str,
    ):
        """
        Get detailed information about a specific metal host

        Keyword Arguments:
            id (str): Unique identifier for a resource within the cluster (ex: vm-2024093009357617)
            cluster (str): The cluster you're operating on (ex: Msc1)

        Returns:
            (dict):
                id (str): The bare metal node id (ex: denvrbm-128)
                cluster (str): The cluster where the bare metal host is allocated (ex: Msc1)
                hostType (str): The specific host node type (ex: nvidia.com/A100PCIE40GB)
                username (str): The username tied to the host (ex: admin)
                tenancyName (str): Name of the tenant where the node has been allocated (ex: denvr)
                gpuType (str)
                gpus (int): Number of GPUs attached to the host (ex: 8)
                vcpus (int): Number of vCPUs on the host (ex: 120)
                vcpuType (str)
                memory (int): Amount of system memory available in GB (ex: 940)
                ip (str): The public IP address of the host (ex: 123.45.67.89)
                privateIp (str): The private IP address of the host (ex: 120.77.3.21)
                imageId (str)
                image (str)
                storage (int): The amount of storage attached to the host in GB (ex: 13600)
                storageClass (str)
                vpcId (str)
                reservation (str)
                reservationExpiry (str)
                status (str): The host status code (e.g., 'offline', 'pending', 'online'
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
        *,
        id: str,
        cluster: str,
        vpc_id: str,
    ):
        """
        Add metal host to VPC

        Keyword Arguments:
            id (str): The bare metal node id (ex: denvrbm-128)
            cluster (str): The cluster where the bare metal node and vpc live (ex: Hou1)
            vpc_id (str): The id of the VPC (ex: denvr-vpc)

        Returns:
            (dict):
                id (str): The bare metal node id (ex: denvrbm-128)
                cluster (str): The cluster where the bare metal host is allocated (ex: Msc1)
                hostType (str): The specific host node type (ex: nvidia.com/A100PCIE40GB)
                username (str): The username tied to the host (ex: admin)
                tenancyName (str): Name of the tenant where the node has been allocated (ex: denvr)
                gpuType (str)
                gpus (int): Number of GPUs attached to the host (ex: 8)
                vcpus (int): Number of vCPUs on the host (ex: 120)
                vcpuType (str)
                memory (int): Amount of system memory available in GB (ex: 940)
                ip (str): The public IP address of the host (ex: 123.45.67.89)
                privateIp (str): The private IP address of the host (ex: 120.77.3.21)
                imageId (str)
                image (str)
                storage (int): The amount of storage attached to the host in GB (ex: 13600)
                storageClass (str)
                vpcId (str)
                reservation (str)
                reservationExpiry (str)
                status (str): The host status code (e.g., 'offline', 'pending', 'online'
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
        *,
        id: str,
        cluster: str,
        vpc_id: str,
    ):
        """
        Remove metal host from VPC

        Keyword Arguments:
            id (str): The bare metal node id (ex: denvrbm-128)
            cluster (str): The cluster where the bare metal node and vpc live (ex: Hou1)
            vpc_id (str): The id of the VPC (ex: denvr-vpc)

        Returns:
            (dict):
                id (str): The bare metal node id (ex: denvrbm-128)
                cluster (str): The cluster where the bare metal host is allocated (ex: Msc1)
                hostType (str): The specific host node type (ex: nvidia.com/A100PCIE40GB)
                username (str): The username tied to the host (ex: admin)
                tenancyName (str): Name of the tenant where the node has been allocated (ex: denvr)
                gpuType (str)
                gpus (int): Number of GPUs attached to the host (ex: 8)
                vcpus (int): Number of vCPUs on the host (ex: 120)
                vcpuType (str)
                memory (int): Amount of system memory available in GB (ex: 940)
                ip (str): The public IP address of the host (ex: 123.45.67.89)
                privateIp (str): The private IP address of the host (ex: 120.77.3.21)
                imageId (str)
                image (str)
                storage (int): The amount of storage attached to the host in GB (ex: 13600)
                storageClass (str)
                vpcId (str)
                reservation (str)
                reservationExpiry (str)
                status (str): The host status code (e.g., 'offline', 'pending', 'online'
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
        *,
        id: str,
        cluster: str,
    ):
        """
        Reboot the metal host

        Keyword Arguments:
            id (str): Unique identifier for a resource within the cluster (ex: vm-2024093009357617)
            cluster (str): The cluster you're operating on (ex: Msc1)

        Returns:
            (dict):
                id (str): The bare metal node id (ex: denvrbm-128)
                cluster (str): The cluster where the bare metal host is allocated (ex: Msc1)
                hostType (str): The specific host node type (ex: nvidia.com/A100PCIE40GB)
                username (str): The username tied to the host (ex: admin)
                tenancyName (str): Name of the tenant where the node has been allocated (ex: denvr)
                gpuType (str)
                gpus (int): Number of GPUs attached to the host (ex: 8)
                vcpus (int): Number of vCPUs on the host (ex: 120)
                vcpuType (str)
                memory (int): Amount of system memory available in GB (ex: 940)
                ip (str): The public IP address of the host (ex: 123.45.67.89)
                privateIp (str): The private IP address of the host (ex: 120.77.3.21)
                imageId (str)
                image (str)
                storage (int): The amount of storage attached to the host in GB (ex: 13600)
                storageClass (str)
                vpcId (str)
                reservation (str)
                reservationExpiry (str)
                status (str): The host status code (e.g., 'offline', 'pending', 'online'
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

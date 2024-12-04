from __future__ import annotations

from typing import TYPE_CHECKING

from denvr.validate import validate_kwargs

if TYPE_CHECKING:
    from denvr.session import Session


class Client:
    def __init__(self, session: Session):
        self.session = session

    def get_hosts(
        self,
        cluster: str | None = None,
    ) -> dict:
        """
        Get a list of bare metal hosts in a cluster

        Keyword Arguments:
            cluster (str)

        Returns:
            id (str): The bare metal node id (ex: denvrbm-128)
            cluster (str): The cluster where the bare metal host is allocated (ex: Msc1)
            host_type (str): The specific host node type (ex: nvidia.com/A100PCIE40GB)
            username (str): The username tied to the host (ex: admin)
            tenancy_name (str): Name of the tenant where the node has been allocated (ex: denvr)
            gpu_type (str):
            gpus (int): Number of GPUs attached to the host (ex: 8)
            vcpus (int): Number of vCPUs on the host (ex: 120)
            vcpu_type (str):
            memory (int): Amount of system memory available in GB (ex: 940)
            ip (str): The public IP address of the host (ex: 123.45.67.89)
            private_ip (str): The private IP address of the host (ex: 120.77.3.21)
            image_id (str):
            image (str):
            storage (int): The amount of storage attached to the host in GB (ex: 13600)
            storage_class (str):
            vpc_id (str):
            reservation (str):
            reservation_expiry (str):
            status (str): The host status code (e.g., 'offline', 'pending', 'online'
        """
        config = self.session.config

        parameters = {
            "params": {
                "Cluster": config.getkwarg("cluster", cluster),
            },
        }

        kwargs = validate_kwargs(
            "get",
            "/api/v1/servers/metal/GetHosts",
            parameters,
            {},
        )

        return self.session.request(
            "get",
            "/api/v1/servers/metal/GetHosts",
            **kwargs,
        )

    def get_host(
        self,
        id: str | None = None,
        cluster: str | None = None,
    ) -> dict:
        """
        Get detailed information about a specific metal host

        Keyword Arguments:
            id (str): Unique identifier for a resource within the cluster (ex: vm-2024093009357617)
            cluster (str): The cluster you're operating on (ex: Msc1)

        Returns:
            id (str): The bare metal node id (ex: denvrbm-128)
            cluster (str): The cluster where the bare metal host is allocated (ex: Msc1)
            host_type (str): The specific host node type (ex: nvidia.com/A100PCIE40GB)
            username (str): The username tied to the host (ex: admin)
            tenancy_name (str): Name of the tenant where the node has been allocated (ex: denvr)
            gpu_type (str):
            gpus (int): Number of GPUs attached to the host (ex: 8)
            vcpus (int): Number of vCPUs on the host (ex: 120)
            vcpu_type (str):
            memory (int): Amount of system memory available in GB (ex: 940)
            ip (str): The public IP address of the host (ex: 123.45.67.89)
            private_ip (str): The private IP address of the host (ex: 120.77.3.21)
            image_id (str):
            image (str):
            storage (int): The amount of storage attached to the host in GB (ex: 13600)
            storage_class (str):
            vpc_id (str):
            reservation (str):
            reservation_expiry (str):
            status (str): The host status code (e.g., 'offline', 'pending', 'online'
        """
        config = self.session.config

        parameters = {
            "params": {
                "Id": config.getkwarg("id", id),
                "Cluster": config.getkwarg("cluster", cluster),
            },
        }

        kwargs = validate_kwargs(
            "get",
            "/api/v1/servers/metal/GetHost",
            parameters,
            {"Id", "Cluster"},
        )

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
    ) -> dict:
        """
        Add metal host to VPC

        Keyword Arguments:
            id (str): The bare metal node id (ex: denvrbm-128)
            cluster (str): The cluster where the bare metal node and vpc live (ex: Hou1)
            vpc_id (str): The id of the VPC (ex: denvr-vpc)

        Returns:
            id (str): The bare metal node id (ex: denvrbm-128)
            cluster (str): The cluster where the bare metal host is allocated (ex: Msc1)
            host_type (str): The specific host node type (ex: nvidia.com/A100PCIE40GB)
            username (str): The username tied to the host (ex: admin)
            tenancy_name (str): Name of the tenant where the node has been allocated (ex: denvr)
            gpu_type (str):
            gpus (int): Number of GPUs attached to the host (ex: 8)
            vcpus (int): Number of vCPUs on the host (ex: 120)
            vcpu_type (str):
            memory (int): Amount of system memory available in GB (ex: 940)
            ip (str): The public IP address of the host (ex: 123.45.67.89)
            private_ip (str): The private IP address of the host (ex: 120.77.3.21)
            image_id (str):
            image (str):
            storage (int): The amount of storage attached to the host in GB (ex: 13600)
            storage_class (str):
            vpc_id (str):
            reservation (str):
            reservation_expiry (str):
            status (str): The host status code (e.g., 'offline', 'pending', 'online'
        """
        config = self.session.config

        parameters = {
            "json": {
                "id": config.getkwarg("id", id),
                "cluster": config.getkwarg("cluster", cluster),
                "vpcId": config.getkwarg("vpc_id", vpc_id),
            },
        }

        kwargs = validate_kwargs(
            "post",
            "/api/v1/servers/metal/AddHostVpc",
            parameters,
            {"cluster", "id", "vpcId"},
        )

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
    ) -> dict:
        """
        Remove metal host from VPC

        Keyword Arguments:
            id (str): The bare metal node id (ex: denvrbm-128)
            cluster (str): The cluster where the bare metal node and vpc live (ex: Hou1)
            vpc_id (str): The id of the VPC (ex: denvr-vpc)

        Returns:
            id (str): The bare metal node id (ex: denvrbm-128)
            cluster (str): The cluster where the bare metal host is allocated (ex: Msc1)
            host_type (str): The specific host node type (ex: nvidia.com/A100PCIE40GB)
            username (str): The username tied to the host (ex: admin)
            tenancy_name (str): Name of the tenant where the node has been allocated (ex: denvr)
            gpu_type (str):
            gpus (int): Number of GPUs attached to the host (ex: 8)
            vcpus (int): Number of vCPUs on the host (ex: 120)
            vcpu_type (str):
            memory (int): Amount of system memory available in GB (ex: 940)
            ip (str): The public IP address of the host (ex: 123.45.67.89)
            private_ip (str): The private IP address of the host (ex: 120.77.3.21)
            image_id (str):
            image (str):
            storage (int): The amount of storage attached to the host in GB (ex: 13600)
            storage_class (str):
            vpc_id (str):
            reservation (str):
            reservation_expiry (str):
            status (str): The host status code (e.g., 'offline', 'pending', 'online'
        """
        config = self.session.config

        parameters = {
            "json": {
                "id": config.getkwarg("id", id),
                "cluster": config.getkwarg("cluster", cluster),
                "vpcId": config.getkwarg("vpc_id", vpc_id),
            },
        }

        kwargs = validate_kwargs(
            "post",
            "/api/v1/servers/metal/RemoveHostVpc",
            parameters,
            {"cluster", "id", "vpcId"},
        )

        return self.session.request(
            "post",
            "/api/v1/servers/metal/RemoveHostVpc",
            **kwargs,
        )

    def reboot_host(
        self,
        id: str | None = None,
        cluster: str | None = None,
    ) -> dict:
        """
        Reboot the metal host

        Keyword Arguments:
            id (str): Unique identifier for a resource within the cluster (ex: vm-2024093009357617)
            cluster (str): The cluster you're operating on (ex: Msc1)

        Returns:
            id (str): The bare metal node id (ex: denvrbm-128)
            cluster (str): The cluster where the bare metal host is allocated (ex: Msc1)
            host_type (str): The specific host node type (ex: nvidia.com/A100PCIE40GB)
            username (str): The username tied to the host (ex: admin)
            tenancy_name (str): Name of the tenant where the node has been allocated (ex: denvr)
            gpu_type (str):
            gpus (int): Number of GPUs attached to the host (ex: 8)
            vcpus (int): Number of vCPUs on the host (ex: 120)
            vcpu_type (str):
            memory (int): Amount of system memory available in GB (ex: 940)
            ip (str): The public IP address of the host (ex: 123.45.67.89)
            private_ip (str): The private IP address of the host (ex: 120.77.3.21)
            image_id (str):
            image (str):
            storage (int): The amount of storage attached to the host in GB (ex: 13600)
            storage_class (str):
            vpc_id (str):
            reservation (str):
            reservation_expiry (str):
            status (str): The host status code (e.g., 'offline', 'pending', 'online'
        """
        config = self.session.config

        parameters = {
            "json": {
                "id": config.getkwarg("id", id),
                "cluster": config.getkwarg("cluster", cluster),
            },
        }

        kwargs = validate_kwargs(
            "post",
            "/api/v1/servers/metal/RebootHost",
            parameters,
            {"cluster", "id"},
        )

        return self.session.request(
            "post",
            "/api/v1/servers/metal/RebootHost",
            **kwargs,
        )

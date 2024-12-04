from __future__ import annotations

from typing import TYPE_CHECKING

from denvr.validate import validate_kwargs

if TYPE_CHECKING:
    from denvr.session import Session


class Client:
    def __init__(self, session: Session):
        self.session = session

    def get_servers(
        self,
        cluster: str | None = None,
    ) -> dict:
        """
        Get a list of virtual machines

        Keyword Arguments:
            cluster (str)

        Returns:
            items (list):
        """
        config = self.session.config

        parameters = {
            "params": {
                "Cluster": config.getkwarg("cluster", cluster),
            },
        }

        kwargs = validate_kwargs(
            "get",
            "/api/v1/servers/virtual/GetServers",
            parameters,
            {},
        )

        return self.session.request(
            "get",
            "/api/v1/servers/virtual/GetServers",
            **kwargs,
        )

    def get_server(
        self,
        id: str | None = None,
        namespace: str | None = None,
        cluster: str | None = None,
    ) -> dict:
        """
        Get detailed information about a specific virtual machine

        Keyword Arguments:
            id (str): The virtual machine id (ex: vm-2024093009357617)
            namespace (str): The namespace where the virtual machine lives. This is usually just the tenant name. (ex: denvr)
            cluster (str): The cluster you're operating on (ex: Hou1)

        Returns:
            username (str): The user that creatd the vm (ex: john@acme.com)
            tenancy_name (str): Name of the tenant where the VM has been created (ex: denvr)
            rpool (str): Resource pool where the VM has been created (ex: on-demand)
            direct_attached_storage_persisted (bool):
            id (str): The name of the virtual machine (ex: my-denvr-vm)
            namespace (str):
            configuration (str): A VM configuration ID (ex: 15)
            storage (int): The amount of storage attached to the VM in GB (ex: 13600)
            gpu_type (str): The specific host GPU type (ex: nvidia.com/A100PCIE40GB)
            gpus (int): Number of GPUs attached to the VM (ex: 8)
            vcpus (int): Number of vCPUs available to the VM (ex: 120)
            memory (int): Amount of system memory available in GB (ex: 940)
            ip (str): The public IP address of the VM (ex: 123.45.67.89)
            private_ip (str): The private IP address of the VM (ex: 120.77.3.21)
            image (str): Name of the VM image used (ex: Ubuntu_22.04.4_LTS)
            cluster (str): The cluster where the VM is allocated (ex: Msc1)
            status (str): The status of the VM (e.g. 'PLANNED', 'PENDING' 'PENDING_RESOURCES', 'PENDING_READINESS', 'ONLINE', 'OFFLINE') (ex: ONLINE)
            storage_type (str):
        """
        config = self.session.config

        parameters = {
            "params": {
                "Id": config.getkwarg("id", id),
                "Namespace": config.getkwarg("namespace", namespace),
                "Cluster": config.getkwarg("cluster", cluster),
            },
        }

        kwargs = validate_kwargs(
            "get",
            "/api/v1/servers/virtual/GetServer",
            parameters,
            {"Id", "Namespace", "Cluster"},
        )

        return self.session.request(
            "get",
            "/api/v1/servers/virtual/GetServer",
            **kwargs,
        )

    def create_server(
        self,
        name: str | None = None,
        rpool: str | None = None,
        vpc: str | None = None,
        configuration: str | None = None,
        cluster: str | None = None,
        ssh_keys: list | None = None,
        operating_system_image: str | None = None,
        personal_storage_mount_path: str | None = None,
        tenant_shared_additional_storage: str | None = None,
        persist_storage: bool | None = None,
        direct_storage_mount_path: str | None = None,
        root_disk_size: int | None = None,
    ) -> dict:
        """
        Create a new virtual machine using a pre-defined configuration

        Keyword Arguments:
            name (str): Name of virtual server to be created. If not provided, name will be auto-generated. (ex: my-denvr-vm)
            rpool (str): Name of the pool to be used. If not provided, first pool assigned to a tenant will be used. In case of no pool assigned, 'on-demand' will be used. (ex: reserved-denvr)
            vpc (str): Name of the VPC to be used. Usually this will match the tenant name. (ex: denvr-vpc)
            configuration (str): Name of the configuration to be used. For possible values, refer to the otput of api/v1/servers/virtual/GetConfigurations, field 'name' DenvrDashboard.Servers.Dtos.ServerConfiguration.Name (ex: A100_40GB_PCIe_1x)
            cluster (str): Cluster to be used. For possible values, refer to the otput of api/v1/clusters/GetAll"/> (ex: Hou1)
            ssh_keys (list)
            operating_system_image (str): Name of the Operating System image to be used. (ex: Ubuntu 22.04.4 LTS)
            personal_storage_mount_path (str): Personal storage file system mount path. (ex: /home/ubuntu/personal)
            tenant_shared_additional_storage (str): Tenant shared storage file system mount path. (ex: /home/ubuntu/tenant-shared)
            persist_storage (bool): Whether direct attached storage should be persistant or ephemeral.
            direct_storage_mount_path (str): Direct attached storage mount path. (ex: /home/ubuntu/direct-attached)
            root_disk_size (int): Size of root disk to be created (Gi). (ex: 500)

        Returns:
            username (str): The user that creatd the vm (ex: john@acme.com)
            tenancy_name (str): Name of the tenant where the VM has been created (ex: denvr)
            rpool (str): Resource pool where the VM has been created (ex: on-demand)
            direct_attached_storage_persisted (bool):
            id (str): The name of the virtual machine (ex: my-denvr-vm)
            namespace (str):
            configuration (str): A VM configuration ID (ex: 15)
            storage (int): The amount of storage attached to the VM in GB (ex: 13600)
            gpu_type (str): The specific host GPU type (ex: nvidia.com/A100PCIE40GB)
            gpus (int): Number of GPUs attached to the VM (ex: 8)
            vcpus (int): Number of vCPUs available to the VM (ex: 120)
            memory (int): Amount of system memory available in GB (ex: 940)
            ip (str): The public IP address of the VM (ex: 123.45.67.89)
            private_ip (str): The private IP address of the VM (ex: 120.77.3.21)
            image (str): Name of the VM image used (ex: Ubuntu_22.04.4_LTS)
            cluster (str): The cluster where the VM is allocated (ex: Msc1)
            status (str): The status of the VM (e.g. 'PLANNED', 'PENDING' 'PENDING_RESOURCES', 'PENDING_READINESS', 'ONLINE', 'OFFLINE') (ex: ONLINE)
            storage_type (str):
        """
        config = self.session.config

        parameters = {
            "json": {
                "name": config.getkwarg("name", name),
                "rpool": config.getkwarg("rpool", rpool),
                "vpc": config.getkwarg("vpc", vpc),
                "configuration": config.getkwarg("configuration", configuration),
                "cluster": config.getkwarg("cluster", cluster),
                "ssh_keys": config.getkwarg("ssh_keys", ssh_keys),
                "operatingSystemImage": config.getkwarg("operating_system_image", operating_system_image),
                "personalStorageMountPath": config.getkwarg("personal_storage_mount_path", personal_storage_mount_path),
                "tenantSharedAdditionalStorage": config.getkwarg(
                    "tenant_shared_additional_storage", tenant_shared_additional_storage
                ),
                "persistStorage": config.getkwarg("persist_storage", persist_storage),
                "directStorageMountPath": config.getkwarg("direct_storage_mount_path", direct_storage_mount_path),
                "rootDiskSize": config.getkwarg("root_disk_size", root_disk_size),
            },
        }

        kwargs = validate_kwargs(
            "post",
            "/api/v1/servers/virtual/CreateServer",
            parameters,
            {"cluster", "configuration", "ssh_keys", "vpc"},
        )

        return self.session.request(
            "post",
            "/api/v1/servers/virtual/CreateServer",
            **kwargs,
        )

    def start_server(
        self,
        id: str | None = None,
        namespace: str | None = None,
        cluster: str | None = None,
    ) -> dict:
        """
        Start a virtual machine that has been previously set up and provisioned, but is currently OFFLINE

        Keyword Arguments:
            id (str): The virtual machine id (ex: vm-2024093009357617)
            namespace (str): The namespace where the virtual machine lives. This is usually just the tenant name. (ex: denvr)
            cluster (str): The cluster you're operating on (ex: Hou1)

        Returns:
            username (str): The user that creatd the vm (ex: john@acme.com)
            tenancy_name (str): Name of the tenant where the VM has been created (ex: denvr)
            rpool (str): Resource pool where the VM has been created (ex: on-demand)
            direct_attached_storage_persisted (bool):
            id (str): The name of the virtual machine (ex: my-denvr-vm)
            namespace (str):
            configuration (str): A VM configuration ID (ex: 15)
            storage (int): The amount of storage attached to the VM in GB (ex: 13600)
            gpu_type (str): The specific host GPU type (ex: nvidia.com/A100PCIE40GB)
            gpus (int): Number of GPUs attached to the VM (ex: 8)
            vcpus (int): Number of vCPUs available to the VM (ex: 120)
            memory (int): Amount of system memory available in GB (ex: 940)
            ip (str): The public IP address of the VM (ex: 123.45.67.89)
            private_ip (str): The private IP address of the VM (ex: 120.77.3.21)
            image (str): Name of the VM image used (ex: Ubuntu_22.04.4_LTS)
            cluster (str): The cluster where the VM is allocated (ex: Msc1)
            status (str): The status of the VM (e.g. 'PLANNED', 'PENDING' 'PENDING_RESOURCES', 'PENDING_READINESS', 'ONLINE', 'OFFLINE') (ex: ONLINE)
            storage_type (str):
        """
        config = self.session.config

        parameters = {
            "json": {
                "id": config.getkwarg("id", id),
                "namespace": config.getkwarg("namespace", namespace),
                "cluster": config.getkwarg("cluster", cluster),
            },
        }

        kwargs = validate_kwargs(
            "post",
            "/api/v1/servers/virtual/StartServer",
            parameters,
            {"cluster", "id", "namespace"},
        )

        return self.session.request(
            "post",
            "/api/v1/servers/virtual/StartServer",
            **kwargs,
        )

    def stop_server(
        self,
        id: str | None = None,
        namespace: str | None = None,
        cluster: str | None = None,
    ) -> dict:
        """
        Stop a virtual machine, ensuring a secure and orderly shutdown of its operations within the cloud environment

        Keyword Arguments:
            id (str): The virtual machine id (ex: vm-2024093009357617)
            namespace (str): The namespace where the virtual machine lives. This is usually just the tenant name. (ex: denvr)
            cluster (str): The cluster you're operating on (ex: Hou1)

        Returns:
            username (str): The user that creatd the vm (ex: john@acme.com)
            tenancy_name (str): Name of the tenant where the VM has been created (ex: denvr)
            rpool (str): Resource pool where the VM has been created (ex: on-demand)
            direct_attached_storage_persisted (bool):
            id (str): The name of the virtual machine (ex: my-denvr-vm)
            namespace (str):
            configuration (str): A VM configuration ID (ex: 15)
            storage (int): The amount of storage attached to the VM in GB (ex: 13600)
            gpu_type (str): The specific host GPU type (ex: nvidia.com/A100PCIE40GB)
            gpus (int): Number of GPUs attached to the VM (ex: 8)
            vcpus (int): Number of vCPUs available to the VM (ex: 120)
            memory (int): Amount of system memory available in GB (ex: 940)
            ip (str): The public IP address of the VM (ex: 123.45.67.89)
            private_ip (str): The private IP address of the VM (ex: 120.77.3.21)
            image (str): Name of the VM image used (ex: Ubuntu_22.04.4_LTS)
            cluster (str): The cluster where the VM is allocated (ex: Msc1)
            status (str): The status of the VM (e.g. 'PLANNED', 'PENDING' 'PENDING_RESOURCES', 'PENDING_READINESS', 'ONLINE', 'OFFLINE') (ex: ONLINE)
            storage_type (str):
        """
        config = self.session.config

        parameters = {
            "json": {
                "id": config.getkwarg("id", id),
                "namespace": config.getkwarg("namespace", namespace),
                "cluster": config.getkwarg("cluster", cluster),
            },
        }

        kwargs = validate_kwargs(
            "post",
            "/api/v1/servers/virtual/StopServer",
            parameters,
            {"cluster", "id", "namespace"},
        )

        return self.session.request(
            "post",
            "/api/v1/servers/virtual/StopServer",
            **kwargs,
        )

    def destroy_server(
        self,
        id: str | None = None,
        namespace: str | None = None,
        cluster: str | None = None,
    ) -> dict:
        """
        Permanently delete a specified virtual machine, effectively wiping all its data and freeing up resources for other uses

        Keyword Arguments:
            id (str): The virtual machine id (ex: vm-2024093009357617)
            namespace (str): The namespace where the virtual machine lives. This is usually just the tenant name. (ex: denvr)
            cluster (str): The cluster you're operating on (ex: Hou1)

        Returns:
            username (str): The user that creatd the vm (ex: john@acme.com)
            tenancy_name (str): Name of the tenant where the VM has been created (ex: denvr)
            rpool (str): Resource pool where the VM has been created (ex: on-demand)
            direct_attached_storage_persisted (bool):
            id (str): The name of the virtual machine (ex: my-denvr-vm)
            namespace (str):
            configuration (str): A VM configuration ID (ex: 15)
            storage (int): The amount of storage attached to the VM in GB (ex: 13600)
            gpu_type (str): The specific host GPU type (ex: nvidia.com/A100PCIE40GB)
            gpus (int): Number of GPUs attached to the VM (ex: 8)
            vcpus (int): Number of vCPUs available to the VM (ex: 120)
            memory (int): Amount of system memory available in GB (ex: 940)
            ip (str): The public IP address of the VM (ex: 123.45.67.89)
            private_ip (str): The private IP address of the VM (ex: 120.77.3.21)
            image (str): Name of the VM image used (ex: Ubuntu_22.04.4_LTS)
            cluster (str): The cluster where the VM is allocated (ex: Msc1)
            status (str): The status of the VM (e.g. 'PLANNED', 'PENDING' 'PENDING_RESOURCES', 'PENDING_READINESS', 'ONLINE', 'OFFLINE') (ex: ONLINE)
            storage_type (str):
        """
        config = self.session.config

        parameters = {
            "params": {
                "Id": config.getkwarg("id", id),
                "Namespace": config.getkwarg("namespace", namespace),
                "Cluster": config.getkwarg("cluster", cluster),
            },
        }

        kwargs = validate_kwargs(
            "delete",
            "/api/v1/servers/virtual/DestroyServer",
            parameters,
            {"Id", "Namespace", "Cluster"},
        )

        return self.session.request(
            "delete",
            "/api/v1/servers/virtual/DestroyServer",
            **kwargs,
        )

    def get_configurations(
        self,
    ) -> dict:
        """
        Get detailed information on available configurations for virtual machines


        Returns:
            items (list):
        """
        config = self.session.config  # noqa: F841

        parameters = {}

        kwargs = validate_kwargs(
            "get",
            "/api/v1/servers/virtual/GetConfigurations",
            parameters,
            {},
        )

        return self.session.request(
            "get",
            "/api/v1/servers/virtual/GetConfigurations",
            **kwargs,
        )

    def get_availability(
        self,
        cluster: str | None = None,
        resource_pool: str | None = None,
        report_nodes: bool | None = None,
    ) -> dict:
        """
        Get information about the current availability of different virtual machine configurations

        Keyword Arguments:
            cluster (str)
            resource_pool (str)
            report_nodes (bool): controls if nodes_available and nodes_max_capacity is calculated and returned in the response. If they are not needed, use 'false' to improve response time of thie endpoint.

        Returns:
            items (list):
        """
        config = self.session.config

        parameters = {
            "params": {
                "cluster": config.getkwarg("cluster", cluster),
                "resourcePool": config.getkwarg("resource_pool", resource_pool),
                "reportNodes": config.getkwarg("report_nodes", report_nodes),
            },
        }

        kwargs = validate_kwargs(
            "get",
            "/api/v1/servers/virtual/GetAvailability",
            parameters,
            {"cluster"},
        )

        return self.session.request(
            "get",
            "/api/v1/servers/virtual/GetAvailability",
            **kwargs,
        )

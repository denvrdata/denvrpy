from __future__ import annotations

from denvr.validate import validate_kwargs

from typing import TYPE_CHECKING, Any  # noqa: F401

if TYPE_CHECKING:
    from denvr.session import Session


class Client:
    def __init__(self, session: Session):
        self.session = session

    def get_servers(self, cluster: str | None = None) -> dict:
        """
        Get a list of virtual machines ::

            client.get_servers(cluster="Cluster")

        Keyword Arguments:
            cluster (str):

        Returns:
            items (list):
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {
            "params": {"Cluster": config.getkwarg("cluster", cluster)}
        }

        kwargs = validate_kwargs("get", "/api/v1/servers/virtual/GetServers", parameters, {})

        return self.session.request("get", "/api/v1/servers/virtual/GetServers", **kwargs)

    def get_server(
        self, id: str | None = None, namespace: str | None = None, cluster: str | None = None
    ) -> dict:
        """
        Get detailed information about a specific virtual machine ::

            client.get_server(id="vm-2024093009357617", namespace="denvr", cluster="Hou1")

        Keyword Arguments:
            id (str): The virtual machine id
            namespace (str): The namespace/vpc where the virtual machine lives. Default one is same as tenant name.
            cluster (str): The cluster you're operating on

        Returns:
            username (str): The user that creatd the vm
            tenancy_name (str): Name of the tenant where the VM has been created
            rpool (str): Resource pool where the VM has been created
            direct_attached_storage_persisted (bool):
            id (str): The name of the virtual machine
            namespace (str):
            configuration (str): A VM configuration ID
            storage (int): The amount of storage attached to the VM in GB
            gpu_type (str): The specific host GPU type
            gpus (int): Number of GPUs attached to the VM
            vcpus (int): Number of vCPUs available to the VM
            memory (int): Amount of system memory available in GB
            ip (str): The public IP address of the VM
            private_ip (str): The private IP address of the VM
            image (str): Name of the VM image used
            cluster (str): The cluster where the VM is allocated
            status (str): The status of the VM (e.g. 'PLANNED', 'PENDING' 'PENDING_RESOURCES', 'PENDING_READINESS',...
            storage_type (str):
            root_disk_size (str):
            last_updated (str):
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {
            "params": {
                "Id": config.getkwarg("id", id),
                "Namespace": config.getkwarg("namespace", namespace),
                "Cluster": config.getkwarg("cluster", cluster),
            }
        }

        kwargs = validate_kwargs(
            "get",
            "/api/v1/servers/virtual/GetServer",
            parameters,
            {"Id", "Namespace", "Cluster"},
        )

        return self.session.request("get", "/api/v1/servers/virtual/GetServer", **kwargs)

    def create_server(
        self,
        name: str | None = None,
        rpool: str | None = None,
        vpc: str | None = None,
        configuration: str | None = None,
        cluster: str | None = None,
        ssh_keys: list | None = None,
        snapshot_name: str | None = None,
        operating_system_image: str | None = None,
        personal_storage_mount_path: str | None = None,
        tenant_shared_additional_storage: str | None = None,
        persist_storage: bool | None = None,
        direct_storage_mount_path: str | None = None,
        root_disk_size: int | None = None,
    ) -> dict:
        """
        Create a new virtual machine using a pre-defined configuration ::

            client.create_server(
                name="my-denvr-vm",
                rpool="reserved-denvr",
                vpc="denvr-vpc",
                configuration="A100_40GB_PCIe_1x",
                cluster="Hou1",
                ssh_keys=["string"],
                snapshot_name="string",
                operating_system_image="Ubuntu 22.04.4 LTS",
                personal_storage_mount_path="/home/ubuntu/personal",
                tenant_shared_additional_storage="/home/ubuntu/tenant-shared",
                persist_storage=False,
                direct_storage_mount_path="/home/ubuntu/direct-attached",
                root_disk_size=500,
            )

        Keyword Arguments:
            name (str): Name of virtual server to be created. If not provided, name will be auto-generated.
            rpool (str): Name of the pool to be used. If not provided, first pool assigned to a tenant will be used. In...
            vpc (str): Name of the VPC to be used. Usually this will match the tenant name.
            configuration (str): Name of the configuration to be used. For possible values, refer to the otput of...
            cluster (str): Cluster to be used. For possible values, refer to the otput of api/v1/clusters/GetAll"/>
            ssh_keys (list):
            snapshot_name (str): Snapshot name.
            operating_system_image (str): Name of the Operating System image to be used.
            personal_storage_mount_path (str): Personal storage file system mount path.
            tenant_shared_additional_storage (str): Tenant shared storage file system mount path.
            persist_storage (bool): Whether direct attached storage should be persistant or ephemeral.
            direct_storage_mount_path (str): Direct attached storage mount path.
            root_disk_size (int): Size of root disk to be created (Gi).

        Returns:
            username (str): The user that creatd the vm
            tenancy_name (str): Name of the tenant where the VM has been created
            rpool (str): Resource pool where the VM has been created
            direct_attached_storage_persisted (bool):
            id (str): The name of the virtual machine
            namespace (str):
            configuration (str): A VM configuration ID
            storage (int): The amount of storage attached to the VM in GB
            gpu_type (str): The specific host GPU type
            gpus (int): Number of GPUs attached to the VM
            vcpus (int): Number of vCPUs available to the VM
            memory (int): Amount of system memory available in GB
            ip (str): The public IP address of the VM
            private_ip (str): The private IP address of the VM
            image (str): Name of the VM image used
            cluster (str): The cluster where the VM is allocated
            status (str): The status of the VM (e.g. 'PLANNED', 'PENDING' 'PENDING_RESOURCES', 'PENDING_READINESS',...
            storage_type (str):
            root_disk_size (str):
            last_updated (str):
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {
            "json": {
                "name": config.getkwarg("name", name),
                "rpool": config.getkwarg("rpool", rpool),
                "vpc": config.getkwarg("vpc", vpc),
                "configuration": config.getkwarg("configuration", configuration),
                "cluster": config.getkwarg("cluster", cluster),
                "ssh_keys": config.getkwarg("ssh_keys", ssh_keys),
                "snapshotName": config.getkwarg("snapshot_name", snapshot_name),
                "operatingSystemImage": config.getkwarg(
                    "operating_system_image", operating_system_image
                ),
                "personalStorageMountPath": config.getkwarg(
                    "personal_storage_mount_path", personal_storage_mount_path
                ),
                "tenantSharedAdditionalStorage": config.getkwarg(
                    "tenant_shared_additional_storage", tenant_shared_additional_storage
                ),
                "persistStorage": config.getkwarg("persist_storage", persist_storage),
                "directStorageMountPath": config.getkwarg(
                    "direct_storage_mount_path", direct_storage_mount_path
                ),
                "rootDiskSize": config.getkwarg("root_disk_size", root_disk_size),
            }
        }

        kwargs = validate_kwargs(
            "post",
            "/api/v1/servers/virtual/CreateServer",
            parameters,
            {"cluster", "configuration", "ssh_keys", "vpc"},
        )

        return self.session.request("post", "/api/v1/servers/virtual/CreateServer", **kwargs)

    def start_server(
        self, id: str | None = None, namespace: str | None = None, cluster: str | None = None
    ) -> dict:
        """
        Start a virtual machine that has been previously set up and provisioned, but is currently OFFLINE ::

            client.start_server(id="vm-2024093009357617", namespace="denvr", cluster="Hou1")

        Keyword Arguments:
            id (str): The virtual machine id
            namespace (str): The namespace/vpc where the virtual machine lives. Default one is same as tenant name.
            cluster (str): The cluster you're operating on

        Returns:
            id (str):
            cluster (str):
            status (str):
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {
            "json": {
                "id": config.getkwarg("id", id),
                "namespace": config.getkwarg("namespace", namespace),
                "cluster": config.getkwarg("cluster", cluster),
            }
        }

        kwargs = validate_kwargs(
            "post",
            "/api/v1/servers/virtual/StartServer",
            parameters,
            {"cluster", "id", "namespace"},
        )

        return self.session.request("post", "/api/v1/servers/virtual/StartServer", **kwargs)

    def stop_server(
        self, id: str | None = None, namespace: str | None = None, cluster: str | None = None
    ) -> dict:
        """
        Stop a virtual machine, ensuring a secure and orderly shutdown of its operations within the cloud environment ::

            client.stop_server(id="vm-2024093009357617", namespace="denvr", cluster="Hou1")

        Keyword Arguments:
            id (str): The virtual machine id
            namespace (str): The namespace/vpc where the virtual machine lives. Default one is same as tenant name.
            cluster (str): The cluster you're operating on

        Returns:
            id (str):
            cluster (str):
            status (str):
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {
            "json": {
                "id": config.getkwarg("id", id),
                "namespace": config.getkwarg("namespace", namespace),
                "cluster": config.getkwarg("cluster", cluster),
            }
        }

        kwargs = validate_kwargs(
            "post",
            "/api/v1/servers/virtual/StopServer",
            parameters,
            {"cluster", "id", "namespace"},
        )

        return self.session.request("post", "/api/v1/servers/virtual/StopServer", **kwargs)

    def destroy_server(
        self,
        delete_snapshots: bool | None = None,
        id: str | None = None,
        namespace: str | None = None,
        cluster: str | None = None,
    ) -> dict:
        """
        Permanently delete a specified virtual machine, effectively wiping all its data and freeing up resources for other uses ::

            client.destroy_server(
                delete_snapshots=True, id="vm-2024093009357617", namespace="denvr", cluster="Hou1"
            )

        Keyword Arguments:
            delete_snapshots (bool): Should also delete snapshots with virtual machine.
            id (str): The virtual machine id
            namespace (str): The namespace/vpc where the virtual machine lives. Default one is same as tenant name.
            cluster (str): The cluster you're operating on

        Returns:
            id (str):
            cluster (str):
            status (str):
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {
            "params": {
                "DeleteSnapshots": config.getkwarg("delete_snapshots", delete_snapshots),
                "Id": config.getkwarg("id", id),
                "Namespace": config.getkwarg("namespace", namespace),
                "Cluster": config.getkwarg("cluster", cluster),
            }
        }

        kwargs = validate_kwargs(
            "delete",
            "/api/v1/servers/virtual/DestroyServer",
            parameters,
            {"Id", "Namespace", "Cluster"},
        )

        return self.session.request("delete", "/api/v1/servers/virtual/DestroyServer", **kwargs)

    def get_configurations(self) -> dict:
        """
        Get detailed information on available configurations for virtual machines ::

            client.get_configurations()


        Returns:
            items (list):
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {}

        kwargs = validate_kwargs(
            "get", "/api/v1/servers/virtual/GetConfigurations", parameters, {}
        )

        return self.session.request(
            "get", "/api/v1/servers/virtual/GetConfigurations", **kwargs
        )

    def get_availability(
        self,
        cluster: str | None = None,
        resource_pool: str | None = None,
        report_nodes: bool | None = None,
    ) -> dict:
        """
        Get information about the current availability of different virtual machine configurations ::

            client.get_availability(cluster="Hou1", resource_pool="reserved-denvr", report_nodes=True)

        Keyword Arguments:
            cluster (str):
            resource_pool (str):
            report_nodes (bool): controls if Count and MaxCount is calculated and returned in the response. If they are not...

        Returns:
            items (list):
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {
            "params": {
                "cluster": config.getkwarg("cluster", cluster),
                "resourcePool": config.getkwarg("resource_pool", resource_pool),
                "reportNodes": config.getkwarg("report_nodes", report_nodes),
            }
        }

        kwargs = validate_kwargs(
            "get", "/api/v1/servers/virtual/GetAvailability", parameters, {"cluster"}
        )

        return self.session.request("get", "/api/v1/servers/virtual/GetAvailability", **kwargs)

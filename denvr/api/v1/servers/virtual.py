from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from denvr.session import Session


class Client:
    def __init__(self, session: Session):
        self.session = session

    def get_servers(
        self,
        cluster: str | None = None,
    ):
        """
        Get a list of virtual machines

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
            "/api/v1/servers/virtual/GetServers",
            **kwargs,
        )

    def get_server(
        self,
        id: str | None = None,
        namespace: str | None = None,
        cluster: str | None = None,
    ):
        """
        Get detailed information about a specific virtual machine

        Keyword Arguments:
            id (str): The virtual machine id (ex: vm-2024093009357617)
            namespace (str): The namespace where the virtual machine lives. This is usually just the tenant name. (ex: denvr)
            cluster (str): The cluster you're operating on (ex: Hou1)
        """
        kwargs = {
            "params": {
                "Id": id if id else getattr(self.session.config, "id", None),
                "Namespace": namespace if namespace else getattr(self.session.config, "namespace", None),
                "Cluster": cluster if cluster else getattr(self.session.config, "cluster", None),
            },
        }

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
    ):
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
        """
        kwargs = {
            "json": {
                "name": name if name else getattr(self.session.config, "name", None),
                "rpool": rpool if rpool else getattr(self.session.config, "rpool", None),
                "vpc": vpc if vpc else getattr(self.session.config, "vpc", None),
                "configuration": configuration
                if configuration
                else getattr(self.session.config, "configuration", None),
                "cluster": cluster if cluster else getattr(self.session.config, "cluster", None),
                "ssh_keys": ssh_keys if ssh_keys else getattr(self.session.config, "ssh_keys", None),
                "operatingSystemImage": operating_system_image
                if operating_system_image
                else getattr(self.session.config, "operating_system_image", None),
                "personalStorageMountPath": personal_storage_mount_path
                if personal_storage_mount_path
                else getattr(self.session.config, "personal_storage_mount_path", None),
                "tenantSharedAdditionalStorage": tenant_shared_additional_storage
                if tenant_shared_additional_storage
                else getattr(self.session.config, "tenant_shared_additional_storage", None),
                "persistStorage": persist_storage
                if persist_storage
                else getattr(self.session.config, "persist_storage", None),
                "directStorageMountPath": direct_storage_mount_path
                if direct_storage_mount_path
                else getattr(self.session.config, "direct_storage_mount_path", None),
                "rootDiskSize": root_disk_size
                if root_disk_size
                else getattr(self.session.config, "root_disk_size", None),
            },
        }

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
    ):
        """
        Start a virtual machine that has been previously set up and provisioned, but is currently OFFLINE

        Keyword Arguments:
            id (str): The virtual machine id (ex: vm-2024093009357617)
            namespace (str): The namespace where the virtual machine lives. This is usually just the tenant name. (ex: denvr)
            cluster (str): The cluster you're operating on (ex: Hou1)
        """
        kwargs = {
            "json": {
                "id": id if id else getattr(self.session.config, "id", None),
                "namespace": namespace if namespace else getattr(self.session.config, "namespace", None),
                "cluster": cluster if cluster else getattr(self.session.config, "cluster", None),
            },
        }

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
    ):
        """
        Stop a virtual machine, ensuring a secure and orderly shutdown of its operations within the cloud environment

        Keyword Arguments:
            id (str): The virtual machine id (ex: vm-2024093009357617)
            namespace (str): The namespace where the virtual machine lives. This is usually just the tenant name. (ex: denvr)
            cluster (str): The cluster you're operating on (ex: Hou1)
        """
        kwargs = {
            "json": {
                "id": id if id else getattr(self.session.config, "id", None),
                "namespace": namespace if namespace else getattr(self.session.config, "namespace", None),
                "cluster": cluster if cluster else getattr(self.session.config, "cluster", None),
            },
        }

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
    ):
        """
        Permanently delete a specified virtual machine, effectively wiping all its data and freeing up resources for other uses

        Keyword Arguments:
            id (str): The virtual machine id (ex: vm-2024093009357617)
            namespace (str): The namespace where the virtual machine lives. This is usually just the tenant name. (ex: denvr)
            cluster (str): The cluster you're operating on (ex: Hou1)
        """
        kwargs = {
            "params": {
                "Id": id if id else getattr(self.session.config, "id", None),
                "Namespace": namespace if namespace else getattr(self.session.config, "namespace", None),
                "Cluster": cluster if cluster else getattr(self.session.config, "cluster", None),
            },
        }

        return self.session.request(
            "delete",
            "/api/v1/servers/virtual/DestroyServer",
            **kwargs,
        )

    def get_configurations(
        self,
    ):
        """
        Get detailed information on available configurations for virtual machines

        Keyword Arguments:
        """
        kwargs = {}

        return self.session.request(
            "get",
            "/api/v1/servers/virtual/GetConfigurations",
            **kwargs,
        )

    def get_availability(
        self,
        cluster: str | None = None,
        resource_pool: str | None = None,
    ):
        """
        Get information about the current availability of different virtual machine configurations

        Keyword Arguments:
            cluster (str)
            resource_pool (str)
        """
        kwargs = {
            "params": {
                "cluster": cluster if cluster else getattr(self.session.config, "cluster", None),
                "resourcePool": resource_pool if resource_pool else getattr(self.session.config, "resource_pool", None),
            },
        }

        return self.session.request(
            "get",
            "/api/v1/servers/virtual/GetAvailability",
            **kwargs,
        )

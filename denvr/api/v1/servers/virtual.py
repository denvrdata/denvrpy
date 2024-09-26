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
        """Get a list of virtual machines"""
        kwargs = {
            "params": {
                "Cluster": cluster,
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
        """Get detailed information about a specific virtual machine"""
        kwargs = {
            "params": {
                "Id": id,
                "Namespace": namespace,
                "Cluster": cluster,
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
        """Create a new virtual machine using pre-defined configuration"""
        kwargs = {
            "json": {
                "name": name,
                "rpool": rpool,
                "vpc": vpc,
                "configuration": configuration,
                "cluster": cluster,
                "ssh_keys": ssh_keys,
                "operatingSystemImage": operating_system_image,
                "personalStorageMountPath": personal_storage_mount_path,
                "tenantSharedAdditionalStorage": tenant_shared_additional_storage,
                "persistStorage": persist_storage,
                "directStorageMountPath": direct_storage_mount_path,
                "rootDiskSize": root_disk_size,
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
        """Start a virtual machine that has been previously set up and provisioned, but is currently OFFLINE"""
        kwargs = {
            "json": {
                "id": id,
                "namespace": namespace,
                "cluster": cluster,
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
        """Stop a virtual machine, ensuring a secure and orderly shutdown of its operations within the cloud environment"""
        kwargs = {
            "json": {
                "id": id,
                "namespace": namespace,
                "cluster": cluster,
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
        """Permanently delete a specified virtual machine, effectively wiping all its data and freeing up resources for other uses"""
        kwargs = {
            "params": {
                "Id": id,
                "Namespace": namespace,
                "Cluster": cluster,
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
        """Get detailed information on available configurations for virtual machines"""
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
        """Get information about the current availability of different virtual machine configurations"""
        kwargs = {
            "params": {
                "cluster": cluster,
                "resourcePool": resource_pool,
            },
        }

        return self.session.request(
            "get",
            "/api/v1/servers/virtual/GetAvailability",
            **kwargs,
        )

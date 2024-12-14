from __future__ import annotations

from typing import TYPE_CHECKING

from denvr.validate import validate_kwargs

if TYPE_CHECKING:
    from denvr.session import Session


class Client:
    def __init__(self, session: Session):
        self.session = session

    def get_applications(
        self,
    ) -> dict:
        """
        List all running applications


        Returns:
            items (list):
        """
        config = self.session.config  # noqa: F841

        parameters = {}

        kwargs = validate_kwargs(
            "get",
            "/api/v1/servers/applications/GetApplications",
            parameters,
            {},
        )

        return self.session.request(
            "get",
            "/api/v1/servers/applications/GetApplications",
            **kwargs,
        )

    def get_application_details(
        self,
        id: str | None = None,
        cluster: str | None = None,
    ) -> dict:
        """
        Get detailed information about a specific application

        Keyword Arguments:
            id (str): The application name (ex: my-jupyter-application)
            cluster (str): The cluster you're operating on (ex: Msc1)

        Returns:
            name (str):
            cluster (str):
            status (str):
            private_ip (str):
            public_ip (str):
            created_by (str):
            tenant (str):
            resource_pool (str):
            application_catalog_item (dict):
            hardware_package (dict):
            image_url (str):
            creation_time (str):
            last_updated (str):
            image_repository_hostname (str):
            image_repository_username (str):
            image_repository_password (str):
            ssh_username (str):
            ssh_keys (list):
            command_override (str):
            ports (list):
            environment_variables (dict):
            dns (str):
            created_by_tenant_id (str):
            created_by_user_id (str):
            application_catalog_item_type (str):
            readiness_watcher_port (str):
            persisted_direct_attached_storage (bool):
            personal_shared_storage (bool):
            tenant_shared_storage (bool):
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
            "/api/v1/servers/applications/GetApplicationDetails",
            parameters,
            {"Id", "Cluster"},
        )

        return self.session.request(
            "get",
            "/api/v1/servers/applications/GetApplicationDetails",
            **kwargs,
        )

    def get_configurations(
        self,
    ) -> dict:
        """
        List all application hardware configurations


        Returns:
            items (list):
        """
        config = self.session.config  # noqa: F841

        parameters = {}

        kwargs = validate_kwargs(
            "get",
            "/api/v1/servers/applications/GetConfigurations",
            parameters,
            {},
        )

        return self.session.request(
            "get",
            "/api/v1/servers/applications/GetConfigurations",
            **kwargs,
        )

    def get_availability(
        self,
        cluster: str | None = None,
        resource_pool: str | None = None,
    ) -> dict:
        """
        Get application hardware configuration availability

        Keyword Arguments:
            cluster (str)
            resource_pool (str)

        Returns:
            items (list):
        """
        config = self.session.config

        parameters = {
            "params": {
                "cluster": config.getkwarg("cluster", cluster),
                "resourcePool": config.getkwarg("resource_pool", resource_pool),
            },
        }

        kwargs = validate_kwargs(
            "get",
            "/api/v1/servers/applications/GetAvailability",
            parameters,
            {"cluster", "resourcePool"},
        )

        return self.session.request(
            "get",
            "/api/v1/servers/applications/GetAvailability",
            **kwargs,
        )

    def get_application_catalog_items(
        self,
    ) -> dict:
        """
        Get application catalog items


        Returns:
            items (list):
        """
        config = self.session.config  # noqa: F841

        parameters = {}

        kwargs = validate_kwargs(
            "get",
            "/api/v1/servers/applications/GetApplicationCatalogItems",
            parameters,
            {},
        )

        return self.session.request(
            "get",
            "/api/v1/servers/applications/GetApplicationCatalogItems",
            **kwargs,
        )

    def create_application(
        self,
        name: str | None = None,
        cluster: str | None = None,
        hardware_package_name: str | None = None,
        application_catalog_item_name: str | None = None,
        application_catalog_item_version: str | None = None,
        resource_pool: str | None = None,
        ssh_keys: list | None = None,
        persist_direct_attached_storage: bool | None = None,
        personal_shared_storage: bool | None = None,
        tenant_shared_storage: bool | None = None,
        jupyter_token: str | None = None,
    ) -> dict:
        """
        Create a new application

        Keyword Arguments:
            name (str): The application name (ex: my-jupyter-application)
            cluster (str): The cluster you're operating on (ex: Msc1)
            hardware_package_name (str): The name or unique identifier of the hardware package to use for the application. (ex: g-nvidia-1xa100-40gb-pcie-14vcpu-112gb)
            application_catalog_item_name (str): The name of the application catalog item. (ex: jupyter-notebook)
            application_catalog_item_version (str): The version name of the application catalog item. (ex: python-3.11.9)
            resource_pool (str): The resource pool to use for the application (ex: on-demand)
            ssh_keys (list): The SSH keys for accessing the application
            persist_direct_attached_storage (bool): Indicates whether to persist direct attached storage (if resource pool is reserved)
            personal_shared_storage (bool): Enable personal shared storage for the application (ex: True)
            tenant_shared_storage (bool): Enable tenant shared storage for the application (ex: True)
            jupyter_token (str): An authentication token for accessing Jupyter Notebook enabled applications (ex: abc123)

        Returns:
            id (str):
            cluster (str):
            status (str):
            tenant (str):
            created_by (str):
            private_ip (str):
            public_ip (str):
            resource_pool (str):
            dns (str):
            ssh_username (str):
            application_catalog_item_name (str):
            application_catalog_item_version_name (str):
            hardware_package_name (str):
            persisted_direct_attached_storage (bool):
            personal_shared_storage (bool):
            tenant_shared_storage (bool):
        """
        config = self.session.config

        parameters = {
            "json": {
                "name": config.getkwarg("name", name),
                "cluster": config.getkwarg("cluster", cluster),
                "hardwarePackageName": config.getkwarg("hardware_package_name", hardware_package_name),
                "applicationCatalogItemName": config.getkwarg(
                    "application_catalog_item_name", application_catalog_item_name
                ),
                "applicationCatalogItemVersion": config.getkwarg(
                    "application_catalog_item_version", application_catalog_item_version
                ),
                "resourcePool": config.getkwarg("resource_pool", resource_pool),
                "sshKeys": config.getkwarg("ssh_keys", ssh_keys),
                "persistDirectAttachedStorage": config.getkwarg(
                    "persist_direct_attached_storage", persist_direct_attached_storage
                ),
                "personalSharedStorage": config.getkwarg("personal_shared_storage", personal_shared_storage),
                "tenantSharedStorage": config.getkwarg("tenant_shared_storage", tenant_shared_storage),
                "jupyterToken": config.getkwarg("jupyter_token", jupyter_token),
            },
        }

        kwargs = validate_kwargs(
            "post",
            "/api/v1/servers/applications/CreateApplication",
            parameters,
            {"applicationCatalogItemName", "applicationCatalogItemVersion", "cluster", "hardwarePackageName", "name"},
        )

        return self.session.request(
            "post",
            "/api/v1/servers/applications/CreateApplication",
            **kwargs,
        )

    def start_application(
        self,
        id: str | None = None,
        cluster: str | None = None,
    ) -> dict:
        """
        Start an application

        Keyword Arguments:
            id (str): The application name (ex: my-jupyter-application)
            cluster (str): The cluster you're operating on (ex: Msc1)

        Returns:
            id (str): The application name (ex: my-jupyter-application)
            cluster (str): The cluster you're operating on (ex: Hou1)
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
            "/api/v1/servers/applications/StartApplication",
            parameters,
            {"cluster", "id"},
        )

        return self.session.request(
            "post",
            "/api/v1/servers/applications/StartApplication",
            **kwargs,
        )

    def stop_application(
        self,
        id: str | None = None,
        cluster: str | None = None,
    ) -> dict:
        """
        Stop an application

        Keyword Arguments:
            id (str): The application name (ex: my-jupyter-application)
            cluster (str): The cluster you're operating on (ex: Msc1)

        Returns:
            id (str): The application name (ex: my-jupyter-application)
            cluster (str): The cluster you're operating on (ex: Hou1)
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
            "/api/v1/servers/applications/StopApplication",
            parameters,
            {"cluster", "id"},
        )

        return self.session.request(
            "post",
            "/api/v1/servers/applications/StopApplication",
            **kwargs,
        )

    def destroy_application(
        self,
        id: str | None = None,
        cluster: str | None = None,
    ) -> dict:
        """
        Permanently delete an application

        Keyword Arguments:
            id (str): The application name (ex: my-jupyter-application)
            cluster (str): The cluster you're operating on (ex: Msc1)

        Returns:
            id (str): The application name (ex: my-jupyter-application)
            cluster (str): The cluster you're operating on (ex: Hou1)
        """
        config = self.session.config

        parameters = {
            "params": {
                "Id": config.getkwarg("id", id),
                "Cluster": config.getkwarg("cluster", cluster),
            },
        }

        kwargs = validate_kwargs(
            "delete",
            "/api/v1/servers/applications/DestroyApplication",
            parameters,
            {"Id", "Cluster"},
        )

        return self.session.request(
            "delete",
            "/api/v1/servers/applications/DestroyApplication",
            **kwargs,
        )

from __future__ import annotations

from denvr.validate import validate_kwargs

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from denvr.session import Session


class Client:
    def __init__(self, session: Session):
        self.session = session

    def get_applications(
        self,
    ) -> dict:
        """
        Get a list of applications


        Returns:
            items (list):
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {}

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
            instance_details (dict):
            application_catalog_item (dict):
            hardware_package (dict):
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {
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
        Get a list of application configurations


        Returns:
            items (list):
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {}

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
        Get detailed information on available configurations for applications

        Keyword Arguments:
            cluster (str)
            resource_pool (str)

        Returns:
            items (list):
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {
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
        Get a list of application catalog items


        Returns:
            items (list):
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {}

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

    def create_catalog_application(
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
        Create a new application using a pre-defined configuration and application catalog item

        Keyword Arguments:
            name (str): The application name (ex: my-jupyter-application)
            cluster (str): The cluster you're operating on (ex: Msc1)
            hardware_package_name (str): The name or unique identifier of the application hardware configuration to use for the application. (ex: g-nvidia-1xa100-40gb-pcie-14vcpu-112gb)
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
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {
            "json": {
                "name": config.getkwarg("name", name),
                "cluster": config.getkwarg("cluster", cluster),
                "hardwarePackageName": config.getkwarg(
                    "hardware_package_name", hardware_package_name
                ),
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
                "personalSharedStorage": config.getkwarg(
                    "personal_shared_storage", personal_shared_storage
                ),
                "tenantSharedStorage": config.getkwarg(
                    "tenant_shared_storage", tenant_shared_storage
                ),
                "jupyterToken": config.getkwarg("jupyter_token", jupyter_token),
            },
        }

        kwargs = validate_kwargs(
            "post",
            "/api/v1/servers/applications/CreateCatalogApplication",
            parameters,
            {
                "applicationCatalogItemName",
                "applicationCatalogItemVersion",
                "cluster",
                "hardwarePackageName",
                "name",
            },
        )

        return self.session.request(
            "post",
            "/api/v1/servers/applications/CreateCatalogApplication",
            **kwargs,
        )

    def start_application(
        self,
        id: str | None = None,
        cluster: str | None = None,
    ) -> dict:
        """
        Start an application that has been previously set up and provisioned, but is currently OFFLINE

        Keyword Arguments:
            id (str): The application name (ex: my-jupyter-application)
            cluster (str): The cluster you're operating on (ex: Msc1)

        Returns:
            id (str): The application name (ex: my-jupyter-application)
            cluster (str): The cluster you're operating on (ex: Msc1)
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {
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
        Stop an application that has been previously set up and provisioned, but is currently ONLINE

        Keyword Arguments:
            id (str): The application name (ex: my-jupyter-application)
            cluster (str): The cluster you're operating on (ex: Msc1)

        Returns:
            id (str): The application name (ex: my-jupyter-application)
            cluster (str): The cluster you're operating on (ex: Msc1)
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {
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
        Permanently delete a specified application, effectively wiping all its data and freeing up resources for other uses

        Keyword Arguments:
            id (str): The application name (ex: my-jupyter-application)
            cluster (str): The cluster you're operating on (ex: Msc1)

        Returns:
            id (str): The application name (ex: my-jupyter-application)
            cluster (str): The cluster you're operating on (ex: Msc1)
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {
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

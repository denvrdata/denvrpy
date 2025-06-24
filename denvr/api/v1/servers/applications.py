from __future__ import annotations

from denvr.validate import validate_kwargs

from typing import TYPE_CHECKING, Any  # noqa: F401

if TYPE_CHECKING:
    from denvr.session import Session


class Client:
    def __init__(self, session: Session):
        self.session = session

    def get_applications(self) -> dict:
        """
        Get a list of applications ::

            client.get_applications()


        Returns:
            items (list):
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {}

        kwargs = validate_kwargs(
            "get", "/api/v1/servers/applications/GetApplications", parameters, {}
        )

        return self.session.request(
            "get", "/api/v1/servers/applications/GetApplications", **kwargs
        )

    def get_application_details(
        self, id: str | None = None, cluster: str | None = None
    ) -> dict:
        """
        Get detailed information about a specific application ::

            client.get_application_details(id="my-jupyter-application", cluster="Msc1")

        Keyword Arguments:
            id (str): The application name
            cluster (str): The cluster you're operating on

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
            }
        }

        kwargs = validate_kwargs(
            "get",
            "/api/v1/servers/applications/GetApplicationDetails",
            parameters,
            {"Id", "Cluster"},
        )

        return self.session.request(
            "get", "/api/v1/servers/applications/GetApplicationDetails", **kwargs
        )

    def get_configurations(self) -> dict:
        """
        Get a list of application configurations ::

            client.get_configurations()


        Returns:
            items (list):
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {}

        kwargs = validate_kwargs(
            "get", "/api/v1/servers/applications/GetConfigurations", parameters, {}
        )

        return self.session.request(
            "get", "/api/v1/servers/applications/GetConfigurations", **kwargs
        )

    def get_availability(
        self, cluster: str | None = None, resource_pool: str | None = None
    ) -> dict:
        """
        Get detailed information on available configurations for applications ::

            client.get_availability(cluster="Msc1", resource_pool="on-demand")

        Keyword Arguments:
            cluster (str):
            resource_pool (str):

        Returns:
            items (list):
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {
            "params": {
                "cluster": config.getkwarg("cluster", cluster),
                "resourcePool": config.getkwarg("resource_pool", resource_pool),
            }
        }

        kwargs = validate_kwargs(
            "get",
            "/api/v1/servers/applications/GetAvailability",
            parameters,
            {"cluster", "resourcePool"},
        )

        return self.session.request(
            "get", "/api/v1/servers/applications/GetAvailability", **kwargs
        )

    def get_application_catalog_items(self) -> dict:
        """
        Get a list of application catalog items ::

            client.get_application_catalog_items()


        Returns:
            items (list):
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {}

        kwargs = validate_kwargs(
            "get", "/api/v1/servers/applications/GetApplicationCatalogItems", parameters, {}
        )

        return self.session.request(
            "get", "/api/v1/servers/applications/GetApplicationCatalogItems", **kwargs
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
        Create a new application using a pre-defined configuration and application catalog item ::

            client.create_catalog_application(
                name="my-jupyter-application",
                cluster="Msc1",
                hardware_package_name="g-nvidia-1xa100-40gb-pcie-14vcpu-112gb",
                application_catalog_item_name="jupyter-notebook",
                application_catalog_item_version="python-3.11.9",
                resource_pool="on-demand",
                ssh_keys=["string"],
                persist_direct_attached_storage=False,
                personal_shared_storage=True,
                tenant_shared_storage=True,
                jupyter_token="abc123",
            )

        Keyword Arguments:
            name (str): The application name
            cluster (str): The cluster you're operating on
            hardware_package_name (str): The name or unique identifier of the application hardware configuration to use for the application.
            application_catalog_item_name (str): The name of the application catalog item.
            application_catalog_item_version (str): The version name of the application catalog item.
            resource_pool (str): The resource pool to use for the application
            ssh_keys (list): The SSH keys for accessing the application
            persist_direct_attached_storage (bool): Indicates whether to persist direct attached storage (if resource pool is reserved)
            personal_shared_storage (bool): Enable personal shared storage for the application
            tenant_shared_storage (bool): Enable tenant shared storage for the application
            jupyter_token (str): An authentication token for accessing Jupyter Notebook enabled applications

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
            }
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
            "post", "/api/v1/servers/applications/CreateCatalogApplication", **kwargs
        )

    def create_custom_application(
        self,
        name: str | None = None,
        cluster: str | None = None,
        hardware_package_name: str | None = None,
        image_url: str | None = None,
        image_cmd_override: list | None = None,
        environment_variables: dict | None = None,
        image_repository: dict | None = None,
        resource_pool: str | None = None,
        readiness_watcher_port: int | None = None,
        proxy_port: int | None = None,
        persist_direct_attached_storage: bool | None = None,
        personal_shared_storage: bool | None = None,
        tenant_shared_storage: bool | None = None,
        user_scripts: dict | None = None,
        security_context: dict | None = None,
    ) -> dict:
        """
        Create a new custom application using a pre-defined configuration and user-defined container image. ::

            client.create_custom_application(
                name="my-custom-application",
                cluster="Msc1",
                hardware_package_name="g-nvidia-1xa100-40gb-pcie-14vcpu-112gb",
                image_url="docker.io/{namespace}/{repository}:{tag}",
                image_cmd_override=["python", "train.py"],
                environment_variables={},
                image_repository={
                    "hostname": "https://index.docker.io/v1/",
                    "username": "your-docker-username",
                    "password": "dckr_pat__xxx1234567890abcdef",
                },
                resource_pool="on-demand",
                readiness_watcher_port=443,
                proxy_port=8888,
                persist_direct_attached_storage=False,
                personal_shared_storage=True,
                tenant_shared_storage=True,
                user_scripts={},
                security_context={"runAsRoot": False},
            )

        Keyword Arguments:
            name (str): The application name
            cluster (str): The cluster you're operating on
            hardware_package_name (str): The name or unique identifier of the application hardware configuration to use for the application.
            image_url (str): Image URL for the custom application.
            image_cmd_override (list): Optional Image CMD override allows users to specify a custom command to run in the container....
            environment_variables (dict): Environment variables for the application. Names must start with a letter or underscore and...
            image_repository (dict):
            resource_pool (str): The resource pool to use for the application
            readiness_watcher_port (int): The port used for monitoring application readiness and status. Common examples:  - 443...
            proxy_port (int): The port your application uses to receive HTTPS traffic.   Port 443 is reserved for the reverse...
            persist_direct_attached_storage (bool): Indicates whether to persist direct attached storage (if resource pool is reserved)
            personal_shared_storage (bool): Enable personal shared storage for the application
            tenant_shared_storage (bool): Enable tenant shared storage for the application
            user_scripts (dict): Dictionary of script filenames to script content. Each scripts to be mounted at...
            security_context (dict):

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
                "imageUrl": config.getkwarg("image_url", image_url),
                "imageCmdOverride": config.getkwarg("image_cmd_override", image_cmd_override),
                "environmentVariables": config.getkwarg(
                    "environment_variables", environment_variables
                ),
                "imageRepository": config.getkwarg("image_repository", image_repository),
                "resourcePool": config.getkwarg("resource_pool", resource_pool),
                "readinessWatcherPort": config.getkwarg(
                    "readiness_watcher_port", readiness_watcher_port
                ),
                "proxyPort": config.getkwarg("proxy_port", proxy_port),
                "persistDirectAttachedStorage": config.getkwarg(
                    "persist_direct_attached_storage", persist_direct_attached_storage
                ),
                "personalSharedStorage": config.getkwarg(
                    "personal_shared_storage", personal_shared_storage
                ),
                "tenantSharedStorage": config.getkwarg(
                    "tenant_shared_storage", tenant_shared_storage
                ),
                "userScripts": config.getkwarg("user_scripts", user_scripts),
                "securityContext": config.getkwarg("security_context", security_context),
            }
        }

        kwargs = validate_kwargs(
            "post",
            "/api/v1/servers/applications/CreateCustomApplication",
            parameters,
            {"cluster", "hardwarePackageName", "imageRepository", "imageUrl", "name"},
        )

        return self.session.request(
            "post", "/api/v1/servers/applications/CreateCustomApplication", **kwargs
        )

    def start_application(self, id: str | None = None, cluster: str | None = None) -> dict:
        """
        Start an application that has been previously set up and provisioned, but is currently OFFLINE ::

            client.start_application(id="my-jupyter-application", cluster="Msc1")

        Keyword Arguments:
            id (str): The application name
            cluster (str): The cluster you're operating on

        Returns:
            id (str): The application name
            cluster (str): The cluster you're operating on
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {
            "json": {
                "id": config.getkwarg("id", id),
                "cluster": config.getkwarg("cluster", cluster),
            }
        }

        kwargs = validate_kwargs(
            "post",
            "/api/v1/servers/applications/StartApplication",
            parameters,
            {"cluster", "id"},
        )

        return self.session.request(
            "post", "/api/v1/servers/applications/StartApplication", **kwargs
        )

    def stop_application(self, id: str | None = None, cluster: str | None = None) -> dict:
        """
        Stop an application that has been previously set up and provisioned, but is currently ONLINE ::

            client.stop_application(id="my-jupyter-application", cluster="Msc1")

        Keyword Arguments:
            id (str): The application name
            cluster (str): The cluster you're operating on

        Returns:
            id (str): The application name
            cluster (str): The cluster you're operating on
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {
            "json": {
                "id": config.getkwarg("id", id),
                "cluster": config.getkwarg("cluster", cluster),
            }
        }

        kwargs = validate_kwargs(
            "post",
            "/api/v1/servers/applications/StopApplication",
            parameters,
            {"cluster", "id"},
        )

        return self.session.request(
            "post", "/api/v1/servers/applications/StopApplication", **kwargs
        )

    def destroy_application(self, id: str | None = None, cluster: str | None = None) -> dict:
        """
        Permanently delete a specified application, effectively wiping all its data and freeing up resources for other uses ::

            client.destroy_application(id="my-jupyter-application", cluster="Msc1")

        Keyword Arguments:
            id (str): The application name
            cluster (str): The cluster you're operating on

        Returns:
            id (str): The application name
            cluster (str): The cluster you're operating on
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {
            "params": {
                "Id": config.getkwarg("id", id),
                "Cluster": config.getkwarg("cluster", cluster),
            }
        }

        kwargs = validate_kwargs(
            "delete",
            "/api/v1/servers/applications/DestroyApplication",
            parameters,
            {"Id", "Cluster"},
        )

        return self.session.request(
            "delete", "/api/v1/servers/applications/DestroyApplication", **kwargs
        )

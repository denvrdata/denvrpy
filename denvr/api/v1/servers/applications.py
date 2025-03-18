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
            instance_details (dict):
            application_catalog_item (dict):
            hardware_package (dict):
        """
        config = self.session.config  # noqa: F841

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
        Get a list of application configurations


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
        Get detailed information on available configurations for applications

        Keyword Arguments:
            cluster (str)
            resource_pool (str)

        Returns:
            items (list):
        """
        config = self.session.config  # noqa: F841

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
        Get a list of application catalog items


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
        Stop an application that has been previously set up and provisioned, but is currently ONLINE

        Keyword Arguments:
            id (str): The application name (ex: my-jupyter-application)
            cluster (str): The cluster you're operating on (ex: Msc1)

        Returns:
            id (str): The application name (ex: my-jupyter-application)
            cluster (str): The cluster you're operating on (ex: Msc1)
        """
        config = self.session.config  # noqa: F841

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
        Permanently delete a specified application, effectively wiping all its data and freeing up resources for other uses

        Keyword Arguments:
            id (str): The application name (ex: my-jupyter-application)
            cluster (str): The cluster you're operating on (ex: Msc1)

        Returns:
            id (str): The application name (ex: my-jupyter-application)
            cluster (str): The cluster you're operating on (ex: Msc1)
        """
        config = self.session.config  # noqa: F841

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

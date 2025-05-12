from __future__ import annotations

from denvr.validate import validate_kwargs

from typing import TYPE_CHECKING, Any  # noqa: F401

if TYPE_CHECKING:
    from denvr.session import Session


class Client:
    def __init__(self, session: Session):
        self.session = session

    def get_host(self, id: str | None = None, cluster: str | None = None) -> dict:
        """
        Get detailed information about a specific metal host ::

            client.get_host(id="Id", cluster="Hou1")

        Keyword Arguments:
            id (str): Unique identifier for a resource within the cluster
            cluster (str): The cluster you're operating on

        Returns:
            id (str): The bare metal id, unique identifier
            cluster (str): The cluster where the bare metal host is allocated
            tenancy_name (str): Name of the tenant where the node has been allocated
            node_type (str): The specific host node type
            image (str): The image used to provision the host
            private_ip (str): private IP address of the host
            provisioned_hostname (str): host name provisioned by the system
            operational_status (str): operational status of the host
            powered_on (bool): true if the host is powered on
            provisioning_state (str): provisioning status of the host
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {
            "params": {
                "Id": config.getkwarg("id", id),
                "Cluster": config.getkwarg("cluster", cluster),
            }
        }

        kwargs = validate_kwargs(
            "get", "/api/v1/servers/metal/GetHost", parameters, {"Id", "Cluster"}
        )

        return self.session.request("get", "/api/v1/servers/metal/GetHost", **kwargs)

    def get_hosts(self, cluster: str | None = None) -> dict:
        """
        Get a list of bare metal hosts in a cluster ::

            client.get_hosts(cluster="Hou1")

        Keyword Arguments:
            cluster (str):

        Returns:
            items (list):
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {
            "params": {"Cluster": config.getkwarg("cluster", cluster)}
        }

        kwargs = validate_kwargs("get", "/api/v1/servers/metal/GetHosts", parameters, {})

        return self.session.request("get", "/api/v1/servers/metal/GetHosts", **kwargs)

    def reboot_host(self, id: str | None = None, cluster: str | None = None) -> dict:
        """
        Reboot the bare metal host ::

            client.reboot_host(id="string", cluster="Hou1")

        Keyword Arguments:
            id (str): Unique identifier for a resource within the cluster
            cluster (str): The cluster you're operating on

        Returns:
            id (str): The bare metal id, unique identifier
            cluster (str): The cluster where the bare metal host is allocated
            tenancy_name (str): Name of the tenant where the node has been allocated
            node_type (str): The specific host node type
            image (str): The image used to provision the host
            private_ip (str): private IP address of the host
            provisioned_hostname (str): host name provisioned by the system
            operational_status (str): operational status of the host
            powered_on (bool): true if the host is powered on
            provisioning_state (str): provisioning status of the host
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {
            "json": {
                "id": config.getkwarg("id", id),
                "cluster": config.getkwarg("cluster", cluster),
            }
        }

        kwargs = validate_kwargs(
            "post", "/api/v1/servers/metal/RebootHost", parameters, {"cluster", "id"}
        )

        return self.session.request("post", "/api/v1/servers/metal/RebootHost", **kwargs)

    def reprovision_host(
        self,
        image_url: str | None = None,
        image_checksum: str | None = None,
        cloud_init_base64: str | None = None,
        id: str | None = None,
        cluster: str | None = None,
    ) -> dict:
        """
        Reprovision the bare metal host ::

            client.reprovision_host(
                image_url="https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64.img",
                image_checksum="https://cloud-images.ubuntu.com/jammy/current/MD5SUMS",
                cloud_init_base64="SGVsbG8sIFdvcmxkIQ==",
                id="string",
                cluster="Hou1",
            )

        Keyword Arguments:
            image_url (str): The URL to the image to use for the host
            image_checksum (str): The checksum url of the image to use for the host
            cloud_init_base64 (str): Base64 encoded cloud-init data yaml file to use for the host
            id (str): Unique identifier for a resource within the cluster
            cluster (str): The cluster you're operating on

        Returns:
            id (str): The bare metal id, unique identifier
            cluster (str): The cluster where the bare metal host is allocated
            tenancy_name (str): Name of the tenant where the node has been allocated
            node_type (str): The specific host node type
            image (str): The image used to provision the host
            private_ip (str): private IP address of the host
            provisioned_hostname (str): host name provisioned by the system
            operational_status (str): operational status of the host
            powered_on (bool): true if the host is powered on
            provisioning_state (str): provisioning status of the host
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {
            "json": {
                "imageUrl": config.getkwarg("image_url", image_url),
                "imageChecksum": config.getkwarg("image_checksum", image_checksum),
                "cloudInitBase64": config.getkwarg("cloud_init_base64", cloud_init_base64),
                "id": config.getkwarg("id", id),
                "cluster": config.getkwarg("cluster", cluster),
            }
        }

        kwargs = validate_kwargs(
            "post", "/api/v1/servers/metal/ReprovisionHost", parameters, {"cluster", "id"}
        )

        return self.session.request("post", "/api/v1/servers/metal/ReprovisionHost", **kwargs)

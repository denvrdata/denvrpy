from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from denvr.session import Session


class Client:
    def __init__(self, session: Session):
        self.session = session

    def get_operating_system_images(
        self,
    ):
        """
        Get a list of operating sytem images available for the tenant

        Keyword Arguments:
        """
        kwargs = {}

        return self.session.request(
            "get",
            "/api/v1/servers/images/GetOperatingSystemImages",
            **kwargs,
        )

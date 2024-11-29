from __future__ import annotations

from typing import TYPE_CHECKING

from denvr.validate import validate_kwargs

if TYPE_CHECKING:
    from denvr.session import Session


class Client:
    def __init__(self, session: Session):
        self.session = session

    def get_operating_system_images(
        self,
    ) -> dict:
        """
        Get a list of operating sytem images available for the tenant


        Returns:
            items (list):
        """
        config = self.session.config  # noqa: F841

        parameters = {}

        kwargs = validate_kwargs(
            "get",
            "/api/v1/servers/images/GetOperatingSystemImages",
            parameters,
            {},
        )

        return self.session.request(
            "get",
            "/api/v1/servers/images/GetOperatingSystemImages",
            **kwargs,
        )

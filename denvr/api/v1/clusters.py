from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from denvr.session import Session


class Client:
    def __init__(self, session: Session):
        self.session = session

    def get_all(
        self,
    ):
        """
        Get a list of allocated clusters


        Returns:
            (list):
        """
        kwargs = {}

        return self.session.request(
            "get",
            "/api/v1/clusters/GetAll",
            **kwargs,
        )

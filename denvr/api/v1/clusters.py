from __future__ import annotations

from denvr.validate import validate_kwargs

from typing import TYPE_CHECKING, Any  # noqa: F401

if TYPE_CHECKING:
    from denvr.session import Session


class Client:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list:
        """
        Get a list of allocated clusters ::

            client.get_all()


        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {}

        kwargs = validate_kwargs("get", "/api/v1/clusters/GetAll", parameters, {})

        return self.session.request("get", "/api/v1/clusters/GetAll", **kwargs)

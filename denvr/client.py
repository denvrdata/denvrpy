from __future__ import annotations

import importlib

from denvr.config import Config, config
from denvr.session import Session


def client(name: str, conf: Config | None = None):
    """
    client("servers/virtual", config=None)

    A shorthand for loading a specific client with a default session/config.
    Optionally, a Config object can be supplied as a keyword.
    """
    _config = conf if conf else config()

    # TODO: Better vetting of `name` for cross-platform paths
    mod = importlib.import_module(
        "denvr.api.{}.{}".format(_config.api, ".".join(name.split("/")))
    )

    return mod.Client(Session(_config))

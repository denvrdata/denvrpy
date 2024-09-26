import denvr
import importlib

from denvr.config import Config
from denvr.session import Session


def client(name):
    """
    client("servers/virtual")

    A shorthand for loading a specific client with a default session/config.
    """
    config = Config()

    # TODO: Better vetting of `name` for cross-platform paths
    mod = importlib.import_module("denvr.api.{}.{}".format(config.api, ".".join(name.split("/"))))

    return mod.Client(Session(config))

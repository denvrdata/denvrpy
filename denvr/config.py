from __future__ import annotations

import os

import toml

from requests.auth import AuthBase

from denvr.auth import auth

DEFAULT_CONFIG_PATH = os.path.join(os.path.expanduser("~"), ".config", "denvr.toml")


class Config:
    """
    Stores the auth and defaults.
    """

    def __init__(self, defaults: dict, auth: AuthBase | None):
        self.defaults = defaults
        self.auth = auth

    @property
    def server(self):
        return self.defaults.get("server", "https://api.cloud.denvrdata.com")

    @property
    def api(self):
        return self.defaults.get("api", "v1")

    @property
    def cluster(self):
        return self.defaults.get("cluster", "Msc1")

    @property
    def tenant(self):
        return self.defaults.get("tenant", None)

    @property
    def vpcid(self):
        return self.defaults.get("vpcid", self.tenant)

    @property
    def rpool(self):
        return self.defaults.get("rpool", "on-demand")

    @property
    def retries(self):
        return self.defaults.get("retries", 3)

    def getkwarg(self, name, val):
        """
        Uses default value for the provided `name` if `val` is `None`.
        """
        if val is None:
            return getattr(self, name, None)

        return val


def config(path=None):
    """
    Construct a Config object from the provide config file path.
    """
    config_path = path if path else os.getenv("DENVR_CONFIG", DEFAULT_CONFIG_PATH)
    config = toml.load(config_path) if os.path.exists(config_path) else {}
    defaults = config.get("defaults", {})
    server = defaults.get("server", "https://api.cloud.denvrdata.com")

    return Config(
        defaults=defaults,
        auth=auth(
            config_path, config.get("credentials", {}), server, defaults.get("retries", 3)
        ),
    )

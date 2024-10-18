from __future__ import annotations

import os

import toml

from denvr.auth import Auth

DEFAULT_CONFIG_PATH = os.path.join(os.path.expanduser("~"), ".config", "denvr.toml")


class Config:
    """
    Stores the auth and defaults.
    """

    def __init__(self, defaults: dict, auth: Auth | None):
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


def config(path=None):
    """
    Construct a Config object from the provide config file path.
    """
    config_path = path if path else os.getenv("DENVR_CONFIG", DEFAULT_CONFIG_PATH)
    config = toml.load(config_path)
    defaults = config["defaults"]
    credentials = config["credentials"]
    server = defaults.get("server", "https://api.cloud.denvrdata.com")

    username = os.getenv("DENVR_USERNAME", credentials["username"])
    if "DENVR_PASSWORD" in os.environ:
        password = os.getenv("DENVR_PASSWORD")
    elif "password" in credentials:
        password = credentials["password"]
    else:
        raise Exception('Could not find password in "DENVR_PASSWORD", keyring or ' + config_path)

    # NOTE: We're intentionally letting the loaded username/password go out of scope for security reasons.
    # The auth object should be able to handle everything from here onward.
    return Config(defaults=config["defaults"], auth=Auth(server, username, password))

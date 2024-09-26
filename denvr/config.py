import os
import toml

from denvr.auth import Auth


class Config:
    """
    Load the Denvr config and stores the auth and defaults.
    """

    def __init__(self):
        config_path = os.getenv(
            "DENVR_CONFIG",
            os.path.join(
                os.path.expanduser("~"),
                ".config",
                "denvr.toml",
            ),
        )

        config = toml.load(config_path)
        self.defaults = config["defaults"]

        # TODO: Move this logic to a separate function for easier unit testing
        username = os.getenv("DENVR_USERNAME", config["credentials"]["username"])
        if "DENVR_PASSWORD" in os.environ:
            password = os.getenv("DENVR_PASSWORD")
        elif "keyring" in config["credentials"] and config["credentials"]["keyring"]:
            import keyring

            password = keyring.get_password("denvyrpy - " + self.defaults["server"], username)
        elif "password" in config["credentials"]:
            password = config["credentials"]["password"]
        else:
            raise Exception('Could not find password in "DENVR_PASSWORD", keyring or ' + config_path)

        # NOTE: We're intentionally letting the loaded username/password go out of scope for security reasons.
        # The auth object should be able to handle everything from here onward.
        self.auth = Auth(
            self.defaults.get("server", "https://api.cloud.denvrdata.com"),
            username,
            password,
        )

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

# Configuration

## Config File

Most of the client configuration is done with a single tomle file.
This file contains sensitive information and should be locked down with `chmod 600 denvr.toml`.

- `~/.config/denvr.toml`: A centralized location for config information
    - `[defaults]`
      - `server`: A specific server to hit (e.g., `https://api.cloud.denvrdata.com`)
      - `api`: The version of the api to use
      - `cluster`: The default cluster to use (e.g., `Msc1`, `Hou1`)
      - `tenant`: The tenant/account name (e.g. `denvr`)
      - `vpcid`: The default vpc name to use (e.g., `denvr`)
      - `rpool`: The default rpool to use (e.g., `on-demand`, `reserved-denvr`)
      - `retries`: The number of retries to use when making requests
    - `[credentials]`
      - `username`: The users email address
      - `password`: The users password

## Environment Variables

These environment variables take priority over any values in the config if they exist.

- `DENVR_CONFIG`: Alternative location of the `denvr.toml` file
- `DENVR_USERNAME`: The users email address
- `DENVR_PASSWORD`: The users password

# denvr

![CI](https://github.com/denvrdata/denvrpy/actions/workflows/CI.yml/badge.svg?branch=main)

-----

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [License](#license)

## Installation

```console
pip install -e git+https://github.com/denvrdata/denvrpy.git
```

## Configuration

Most of the client configuration is done with a single tomle file.
This file contains sensitive information and should be locked down with `chmod 600 denvr.toml`.
TODO: Replace the username and password with a personal access token.

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

## Usage

Getting started with the `denvr` python sdk just involves loading and calling the `client` builder function, which returns a `Client` object for each denvr service (e.g., `clusters`, `vpcs`, `servers/virtual`).

```python
>>> import json
>>> from denvr.client import client
>>> virtual = client('servers/virtual')
```

Lets start by fetching some of Denvr's VM configurations.
We'll use `json.dumps` to make the output a bit easier to read.
```python
>>> print(json.dumps(virtual.get_configurations(), indent=2))
{
  "items": [
    {
      "id": 5,
      "user_friendly_name": "A100_40GB_PCIe_1x",
      "name": "A100_40GB_PCIe_1x",
      "description": null,
      "os_version": "20.04",
      "os_type": "Ubuntu",
      "storage": 1700,
      "gpu_type": "nvidia.com/A100PCIE40GB",
      "gpu_family": "NVIDIA A100",
      "gpu_brand": "Nvidia",
      "gpu_name": "A100 40GB PCIe",
      "type": "nvidia.com/A100PCIE40GB",
      "brand_family": "NVIDIA A100",
      "brand": "Nvidia",
      "text_name": "A100 40GB PCIe",
      "gpus": 1,
      "vcpus": 14,
      "memory": 112,
      "price": 2.05,
      "compute_network": null,
      "is_gpu_platform": true,
      "clusters": [
        "Hou1",
        "Msc1"
      ]
    },
    {
      "id": 6,
      "user_friendly_name": "A100_40GB_PCIe_2x",
      "name": "A100_40GB_PCIe_2x",
      "description": null,
      "os_version": "20.04",
      "os_type": "Ubuntu",
      "storage": 3400,
      "gpu_type": "nvidia.com/A100PCIE40GB",
      "gpu_family": "NVIDIA A100",
      "gpu_brand": "Nvidia",
      "gpu_name": "A100 40GB PCIe",
      "type": "nvidia.com/A100PCIE40GB",
      "brand_family": "NVIDIA A100",
      "brand": "Nvidia",
      "text_name": "A100 40GB PCIe",
      "gpus": 2,
      "vcpus": 28,
      "memory": 224,
      "price": 4.1,
      "compute_network": null,
      "is_gpu_platform": true,
      "clusters": [
        "Hou1",
        "Msc1"
      ]
    },
    ...
```

We can also get info about a specific vm.
```python
>>> print(json.dumps(virtual.get_server(id='rofinn-intel-dev', namespace='denvr', cluster='Hou1'), indent=2))
{
  "username": "rory@denvrdata.com",
  "tenancy_name": "denvr",
  "rpool": "reserved-denvr",
  "id": "rofinn-intel-dev",
  "namespace": "denvr",
  "configuration": "15",
  "storage": 27000,
  "gpu_type": "intel/GAUDI2",
  "gpus": 8,
  "vcpus": 152,
  "memory": 940,
  ...
  "image": "habana-1.16.2",
  "cluster": "Hou1",
  "status": "ONLINE",
  "storageType": "na"
}
```

## Environment Variables

These environment variables take priority over any values in the config if they exist.

- `DENVR_CONFIG`: Alternative location of the `denvr.toml` file
- `DENVR_USERNAME`: The users email address
- `DENVR_PASSWORD`: The users password

## Design

### Goals

Before we dig into the specific architecture we should discuss the guiding principles that impact our architecture.

Dos:
1. **Consistent** - Be predictable, using the same naming conventions as our REST API whenever possible
2. **Simple** - Most simple operation should only require 2-3 short lines of python code.
3. **Portable** - Apart from syntax and code styling, components should be transferable to other languages.
  - Stick to simple/ubiquitous constructs like structs, functions and namespaces with broad support across languages
4. **Pythonic** - While the names should match our API spec, we do still want the produced code to be pythonic.

Don'ts:
1. **Verbosity** - We don't want to overwhelm users with complicated object and function names.
  - Context and namespaces can go a long way in differentiating implementations of the same shared concept
  - Users already know how standard collection types like `dict` and `list` work

### client (Client)

Ideally, the `client` builder function is the only thing most users will need to import.
This function should handle constructing the necessary `Config`, `Auth` and `Session` objects used
to instantiate the `Client` for the requested service name (e.g., `clusters`, `vpcs`, `servers/virtual`).

Each service currently has an autogenerated `Client` class which wraps a `Session` object and provides methods for all the included paths (e.g., `GetAll`, `CreateServer`).

NOTES:

- All function and argument names are converted to the more pythonic snakecase format (e.g., `GetAll` -> `get_all`, `vpcId` -> `vpc_id`)
- We currently gatekeep which paths are include in our `scripts/apigen.py` file.
- Composition over inheritance as that seemed easier to implement across languages.
  - We're passing a shared `Session` object into each generated independent `Client` object rather than having shared logic in an `AbstractClient` parent.
- Namespacing over unique object names
  - Rather than having complicated names you should be able to just load the service you care about
  - We don't wrap method input / outputs in custom object types since folks already know how `list`, `dict`, etc work.

### Session

The Session object wraps all API requests calls, including any config defaults and passing the `Auth` object.
The goal of this object is limit the complexity of the generated `Client` objects for each service.

NOTES:

- All requests have the content type set to "application/json"`
- Any common error handling occurs in one place
- We just auto-extract the `json` and return the `results` item.

### Config

The config handles loading values from `~/.config/denvr.toml`, or the location of the `DENVR_CONFIG` environment variable.
An `Auth` object is created from either:

- `DENVR_USERNAME` and `DENVR_PASSWOR`
- The `username` and `password` values in the `credentials` section of the `denvr.toml` file.

### Auth

An object for handling requesting and refreshing access tokens given an initial username and password.
It is callable and subtypes `requests.auth.AuthBase` so that we can pass it as the `auth` keyword to `requests`

NOTE: The password isn't stored in the object and will be deleted when it goes out of scope in the `Auth` and `Config` constructors.

## License

`denvr` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

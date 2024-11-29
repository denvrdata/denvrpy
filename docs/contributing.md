# Contributing

[![License](https://img.shields.io/badge/License-MIT-%234493c5?style=flat)](LICENSE.txt)
[![Contributor Covenant](https://img.shields.io/badge/Contributor_Covenant-2.1-%234493c5?style=flat)](CODEOFCONDUCT.md)

Requirements:

- [GitHub Account](https://github.com/join)
- [Python](https://wiki.python.org/moin/BeginnersGuide/Download)
- [Git]()
- [denvrpy](https://github.com/denvrdata/denvrpy)

The [GitHub docs](https://docs.github.com/en/get-started) already have a lot of useful info to help you get started
creating an account, using `git`, and making issues/pull requests.

## Issues

The easiest way to help the denvrpy project is to open [issues](https://github.com/denvrdata/denvrpy/issues/new/choose).
That being said, here is a list of common details we recommend including:

- Objective
- Code snippets
- Logs
- Stacktrace
- Settings
- Environments (e.g., docker container)

## Pull Requests (PRs)

Our primary workflow for making changes to `denvrpy` is with pull requests (PRs).
This process involves:

1. Forking the original repo (from the browser)
2. Clone your fork with `git clone`
3. Make your changes locally
4. Add your modified files with `git add`
5. Commit your changes with a descriptive message `git commit`
6. Push your change back up to your fork `git push`
7. Open a pull request on the original repository (from the browser)

Again, the [GitHub docs](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) already have a detailed summary of this workflow.

When opening a pull request it's best to:

1. Summarize what you're changing and why
2. Keep you changes minimial
2. Include any needed tests and docs
3. Ensure all tests, linting and coverage checks pass

## Development

We currently use [hatch](https://hatch.pypa.io/1.12/) as our Python project manager.
This one tool serves as our:

1. Build and publishing system
2. Environment manager (ie: virtualenv)
3. Shared env aware runner for tests, docs and scripts

### Environment

To get started with the default development virtualenv just run:
```shell
hatch shell
```
This will sync all the dependencies for you.
You can just type `exit` to return to your default shell environment.

### Debugging

This SDK is still in beta as we're still iterating on our REST API. Apart from loading up `pdb` we also provide some debug logs.

```python
>>> import json
>>> import logging
>>> from denvr.client import client
>>> logging.basicConfig(level=logging.DEBUG)
>>> virtual = client('servers/virtual')
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): api.cloud.denvrdata.com:443
DEBUG:urllib3.connectionpool:https://api.cloud.denvrdata.com:443 "POST /api/TokenAuth/Authenticate HTTP/11" 200 None
...
>>> print(json.dumps(
    virtual.create_server(
        name="api-test",
        rpool="on-demand",
        vpc="denvr",
        configuration="H100_80GB_SXM_8x",
        cluster="Hou1",
        ssh_keys=["ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAA..."],
        operating_system_image="Ubuntu 22.04.4 LTS",
        root_disk_size=500,
    ),
    indent=2
))
DEBUG:denvr.session:Dropping missing json argument personalStorageMountPath
DEBUG:denvr.session:Dropping missing json argument tenantSharedAdditionalStorage
DEBUG:denvr.session:Dropping missing json argument persistStorage
DEBUG:denvr.session:Dropping missing json argument directStorageMountPath
DEBUG:denvr.session:Request: self.session.request(post, https://api.cloud.denvrdata.com/api/v1/servers/virtual/CreateServer, **{'json': {'name': 'api-test', 'rpool': 'on-dema
nd', 'vpc': 'denvr', 'configuration': 'H100_80GB_SXM_8x', 'cluster': 'Hou1', 'ssh_keys': ['ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAA...'], 'operatingSystemImage': 'Ubuntu 22.04.4 L
TS', 'rootDiskSize': 500}}
DEBUG:urllib3.connectionpool:https://api.cloud.denvrdata.com:443 "POST /api/v1/servers/virtual/CreateServer HTTP/11" 202 482
{
  "username": "rory@denvrdata.com",
  "tenancy_name": "denvr",
  "rpool": "on-demand",
  "directAttachedStoragePersisted": false,
  "id": "api-test",
  "namespace": "denvr",
  "configuration": "H100_80GB_SXM_8x",
  "storage": 20000,
  "gpu_type": "nvidia.com/H100SXM480GB",
  "gpus": 8,
  "vcpus": 200,
  "memory": 940,
  "ip": "",
  "privateIp": "172.16.0.2",
  "image": "Ubuntu_22.04.4_LTS",
  "cluster": "Hou1",
  "status": "na",
  "storageType": "na"
}
```

### Testing

For quickly running unit tests you can just use:

```shell
> hatch test
```

However, for full integration tests we run mockserver against our open api spec.

```shell
> docker run -d --rm -p 1080:1080 mockserver/mockserver
> hatch run integration:test
```

### Docs

To run the local mkdocs server:

```shell
> hatch run docs:serve
```

### Linting

To help keep our code well formatted and following best practices we use [ruff](https://docs.astral.sh/ruff/formatter/).

To just check for issues run:
```shell
> hatch fmt --check
```

However, to fix the issues and format your code run:
```shell
> hatch fmt
```

If you disagree with `ruff` you can choose to either globally add the exception to the `pyproject.toml`:
```toml
...
[tool.ruff.lint.per-file-ignores]
"denvr/api/*" = ["A002"] # shadowing likely in generated code
...
```
or preferably specific inline instances with a `# noqa: ...` comment:
```python
...
config = self.session.config  # noqa: F841

parameters = {}
...
```

### API Generation

To make changes to any files within the `api/` directory you'll need to modify the files in `scripts/`.
The `apigen.py` pulls down and processes our open api spec.
The `client.py.jinja2` and `test_client.py.jinja2` files are used to populate the API service clients and corresponding tests.

To regenerate the `api/` and `tests/api/` files run:

```shell
> hatch run scripts/apigen.py
```

You'll also want to rerun the formatter to fix any consistency or linting issues in the generated files.
```shell
> hatch fmt
```

TODO: Run the linter inside `apigen.py`
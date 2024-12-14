"""
This file only exists to generate the other modules in this SDK.

WARNING: May not work correctly on Windows.
"""

# /// script
# requires-python = ">=3.12"
# dependencies = ["jinja2", "requests"]
# ///
from __future__ import annotations

import json
import logging
import os
import sys
from collections import defaultdict

import jinja2
import requests

# Define a few filepath constants we'll use in our script
SCRIPTS_PATH = os.path.dirname(os.path.abspath(__file__))
DENVR_PATH = os.path.join(os.path.dirname(SCRIPTS_PATH), "denvr")
TESTS_PATH = os.path.join(os.path.dirname(SCRIPTS_PATH), "tests")
API_SPEC_LOCATION = "https://api.cloud.denvrdata.dev/swagger/v1/swagger.json"

# Add the denvr module to our search path, so we can load a few utility functions from it.
sys.path.append(DENVR_PATH)
from utils import snakecase  # noqa: E402

# Paths to include in our SDK to identify breaking changes,
# but supporting feature gating.
# TODO: Template the paths rather than hardcode
INCLUDED_PATHS = [
    "/api/v1/clusters/GetAll",
    "/api/v1/servers/images/GetOperatingSystemImages",
    "/api/v1/servers/applications/GetApplications",
    "/api/v1/servers/applications/GetApplicationDetails",
    "/api/v1/servers/applications/GetConfigurations",
    "/api/v1/servers/applications/GetAvailability",
    "/api/v1/servers/applications/GetApplicationCatalogItems",
    "/api/v1/servers/applications/CreateApplication",
    "/api/v1/servers/applications/StartApplication",
    "/api/v1/servers/applications/StopApplication",
    "/api/v1/servers/applications/DestroyApplication",
    "/api/v1/servers/metal/GetHosts",
    "/api/v1/servers/metal/GetHost",
    "/api/v1/servers/metal/AddHostVpc",
    "/api/v1/servers/metal/RemoveHostVpc",
    "/api/v1/servers/metal/RebootHost",
    "/api/v1/servers/virtual/GetServers",
    "/api/v1/servers/virtual/GetServer",
    "/api/v1/servers/virtual/CreateServer",
    "/api/v1/servers/virtual/StartServer",
    "/api/v1/servers/virtual/StopServer",
    "/api/v1/servers/virtual/DestroyServer",
    "/api/v1/servers/virtual/GetConfigurations",
    "/api/v1/servers/virtual/GetAvailability",
    # "/api/v1/vpcs/GetVpcs",
    # "/api/v1/vpcs/GetVpc",
    # "/api/v1/vpcs/CreateVpc",
    # "/api/v1/vpcs/DestroyVpc",
]

TYPE_MAP = {
    "string": "str",
    "boolean": "bool",
    "integer": "int",
    "array": "list",
    "object": "dict",
}

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def getapi(url=API_SPEC_LOCATION):
    """
    Fetch the API spec and extracts the JSON object.
    """
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()


def splitpaths(paths: list[str]) -> defaultdict[str, list]:
    """
    Split a list of paths into modules and methods.

    Args:
        paths (list[str]): The list of paths to split.

    Returns:
        defaultdict[str, list]: A dictionary where the keys are module names and the values are lists of method names.
    """
    result = defaultdict(list)
    for path in paths:
        k, v = os.path.split(path)
        result[k].append(v)

    return result


def makepaths(path: str):
    """
    Create the module directory and any necessary subdirectories, include __init__.py files.

    Args:
        path (str): The path to create.
    """
    os.makedirs(path, exist_ok=True)
    for root, _, files in os.walk(path):
        if "__init__.py" not in files:
            with open(os.path.join(root, "__init__.py"), "w") as fobj:
                fobj.write("")


def testval(name, typ):
    """
    Given a dict of name -> type, return simple test values to use.
    """
    if typ == "str":
        return f'"{name}"'
    elif typ == "bool":
        return "True"
    elif typ == "int":
        return "1"
    elif typ == "list":
        return '["foo"]'
    elif typ == "dict":
        return '{"foo": "bar"}'
    else:
        raise Exception(f"Type {typ} is not supported")


def generate(included=INCLUDED_PATHS):
    # Load our jinja2 templates
    template_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(SCRIPTS_PATH),
        autoescape=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    client_template = template_env.get_template("client.py.jinja2")
    test_template = template_env.get_template("test_client.py.jinja2")

    api = getapi()

    # Pull out the main components we're gonna care about
    paths = {k: v for (k, v) in api["paths"].items() if k in included}
    schemas = api["components"]["schemas"]

    # Start generating each new module
    for module, methods in splitpaths(list(paths.keys())).items():
        # Split the module directory and module .py name
        modsplit = os.path.split(module)

        # Create the module directory
        moddir = os.path.join(DENVR_PATH, os.path.splitroot(modsplit[0])[-1])
        makepaths(moddir)

        # Create the test directory
        testsdir = os.path.join(TESTS_PATH, os.path.splitroot(modsplit[0])[-1])
        makepaths(testsdir)

        # Specify the module path
        modpath = os.path.join(moddir, f"{modsplit[1]}.py")
        testspath = os.path.join(testsdir, f"test_{modsplit[1]}.py")

        # Start building our context for the client template
        context = {
            "module": os.path.splitroot(module)[-1].replace("/", "."),
            "methods": [],
        }
        logger.debug("Context: %s", context)
        for methodname in methods:
            # The dict where we'll store the current method context
            # to be inserted
            method = {}

            # Extract the entry for a given path
            # i.e. {module}/{methodname}
            method_path = os.path.join(module, methodname)
            path_entry = paths[method_path]

            # Currently only supports 1 http method per entry
            # TODO: Add a better error message
            assert len(path_entry) == 1
            http_method = next(iter(path_entry))
            path_vals = path_entry[http_method]
            method["method"] = http_method
            method["path"] = method_path
            method["description"] = path_vals["summary"]
            method["name"] = snakecase(methodname)
            method["params"] = []
            method["json"] = []
            method["rprops"] = []
            method["required"] = []

            logger.debug("%s(%s) -> %s", methodname, http_method, json.dumps(path_vals))

            # Collect the argument names and types
            # TODO: These should also have descriptions for the docstrings
            if "parameters" in path_vals:
                for param in path_vals["parameters"]:
                    method["params"].append(
                        {
                            "param": param["name"],
                            "kwarg": snakecase(param["name"]),
                            "type": TYPE_MAP[param["schema"]["type"]],
                            "val": testval(param["name"], TYPE_MAP[param["schema"]["type"]]),
                            "desc": param.get("description", ""),
                            "example": param.get("example", ""),
                            "required": param.get("required", False),
                        }
                    )
                    if param.get("required", False):
                        method["required"].append(param["name"])

            if "requestBody" in path_vals:
                # TODO: Technically we should test for the '$ref' case first
                schema_ref = os.path.basename(path_vals["requestBody"]["content"]["application/json"]["schema"]["$ref"])
                schema = schemas[schema_ref]
                assert schema["type"] == "object"
                method["required"].extend(schema.get("required", []))
                for name, val in schema["properties"].items():
                    method["json"].append(
                        {
                            "param": name,
                            "kwarg": snakecase(name),
                            "type": TYPE_MAP[val["type"]],
                            "val": testval(name, TYPE_MAP[val.get("type", "object")]),
                            "desc": val.get("description", ""),
                            "example": val.get("example", ""),
                        }
                    )

            # TODO: Wrap this schema processing in an object which support generic path based indexing and
            # automatic dereferencing for templates.
            assert "responses" in path_vals
            success = [v for (k, v) in path_vals["responses"].items() if "200" <= k < "300"]
            assert len(success) == 1
            assert "content" in success[0]
            assert "application/json" in success[0]["content"]
            assert "schema" in success[0]["content"]["application/json"]
            resp = success[0]["content"]["application/json"]["schema"]

            # TODO: Return schemas should have a description
            if len(resp) == 1 and "$ref" in resp:
                schema = schemas[os.path.basename(resp["$ref"])]
                assert "type" in schema
                assert schema["type"] == "object"
                method["rtype"] = "dict"
                for name, val in schema["properties"].items():
                    logger.debug("%s : %s", name, val)
                    method["rprops"].append(
                        {
                            "name": snakecase(name),
                            "type": TYPE_MAP[val.get("type", "object")],
                            "desc": val.get("description", ""),
                            "example": val.get("example", ""),
                        }
                    )

            elif "type" in resp and resp["type"] == "array":
                method["rtype"] = "list"

            # Add our method to
            context["methods"].append(method)

        # Generate our client text
        # The snippet below can be helpful for debugging
        # contextpath = os.path.join(moddir, "{}.json".format(modsplit[1]))
        # with open(contextpath, 'w') as fobj:
        #     fobj.write(json.dumps(context, indent=2))

        content = client_template.render(context)
        with open(modpath, "w") as fobj:
            fobj.write(content)

        content = test_template.render(context)
        with open(testspath, "w") as fobj:
            fobj.write(content)


if __name__ == "__main__":
    generate()

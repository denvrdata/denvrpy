"""
This file only exists to generate the other modules in this SDK.

WARNING: May not work correctly on Windows.
"""

# /// script
# requires-python = ">=3.12"
# dependencies = ["glom", "jinja2", "openapi-spec-validator", "requests"]
# ///
from __future__ import annotations

import copy
import json
import logging
import os
import random
import sys
from collections import defaultdict
from typing import Any

import jinja2
import openapi_spec_validator
import requests

from glom import glom

# Define a few filepath constants we'll use in our script
SCRIPTS_PATH = os.path.dirname(os.path.abspath(__file__))
DENVR_PATH = os.path.join(os.path.dirname(SCRIPTS_PATH), "denvr")
TESTS_PATH = os.path.join(os.path.dirname(SCRIPTS_PATH), "tests")
API_SPEC_URL = "https://api.cloud.denvrdata.dev/swagger/v1/swagger.json"
API_SPEC_PATH = "./swagger.json"

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
    "/api/v1/servers/applications/CreateCatalogApplication",
    "/api/v1/servers/applications/CreateCustomApplication",
    "/api/v1/servers/applications/StartApplication",
    "/api/v1/servers/applications/StopApplication",
    "/api/v1/servers/applications/DestroyApplication",
    "/api/v1/servers/metal/GetHosts",
    "/api/v1/servers/metal/GetHost",
    # "/api/v1/servers/metal/AddHostVpc",
    # "/api/v1/servers/metal/RemoveHostVpc",
    "/api/v1/servers/metal/RebootHost",
    "/api/v1/servers/metal/ReprovisionHost",
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
    "any": "Any",
}

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def fetchapi(url: str = API_SPEC_URL) -> dict:
    """
    Fetch the API spec and extracts the JSON object.
    """
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()


def loadapi(fp: str = API_SPEC_PATH) -> dict:
    with open(fp) as fobj:
        return json.load(fobj)


def validate(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        openapi_spec_validator.validate(result)
        return result

    return wrapper


@validate
def filter(api: dict, included=INCLUDED_PATHS) -> dict:
    """
    Given an OpenAPI spec, remove all paths that are not in the included paths.
    """
    rem = set(api["paths"].keys()).difference(set(included))

    for path in rem:
        logger.info("Dropping path %s", path)
        api["paths"].pop(path)

    return api


@validate
def flatten(api: dict) -> dict:
    """
    Given an OpenAPI spec, it will remove all "$ref" key values and replace them with the
    appropriate object content.
    """

    def _flatten(src: dict, dst: dict, visited: list = []) -> dict:
        logger.info("-" * len(visited))
        for k, v in dst.items():
            logger.info("%s -> %s", k, type(v))
            if isinstance(v, dict):
                if "$ref" in v:
                    refpath = v["$ref"]
                    assert refpath.startswith("#/")
                    path = ".".join(refpath[2:].split("/"))
                    logger.info(path)
                    if path in visited:
                        logger.warn("Cycle on %s identified. Exiting recusive loop.", path)
                    else:
                        dst[k] = _flatten(src, glom(src, path), visited=visited + [path])
                else:
                    dst[k] = _flatten(src, v, visited=visited)

        return dst

    result = copy.deepcopy(api)
    _flatten(api, result)
    return result


def extract_param_examples(params: list) -> dict:
    """
    Returns a simple dict of name => example for a list of parameters

    Args:
        params (list): A list of params in an open api spec.

    Returns:
        A dictionary of the examples.
    """

    def example(p):
        name = p["name"]
        typ = TYPE_MAP[glom(p, "schema.type")]
        example = p.get("example", None)

        if example:
            return example
        elif typ == "str":
            return name
        elif typ == "bool":
            return True
        elif typ == "int":
            return 1
        elif typ == "list":
            return ["foo"]
        elif typ == "dict":
            return {"foo": "bar"}
        else:
            raise Exception(f"Type {typ} is not supported")

    return {p["name"]: example(p) for p in params}


def extract_schema_examples(schema: dict, seed=1234) -> Any:
    """
    Recursively pull examples out of a schema definition.

    Args:
        schema (dict): The schema dictionary to process

    Returns:
        A valid example or None if

    NOTE: We assume that the spec has already been flattened.
    """
    # Ensure that any "random" values are reproducible given the same spec file.
    random.seed(seed)

    # Early exit cases if not flattened, schema is empty or there's an example at the top level
    assert "$ref" not in schema
    if len(schema) == 0:
        return None
    elif "example" in schema:
        return schema["example"]
    elif "enum" in schema:
        return random.choice(schema["enum"])

    # Otherwise we need to extract nested examples based on the schema type
    # or generate a reasonable sample value based on the type.
    schema_type = schema.get("type", "any")
    if schema_type == "object":
        if "example" in schema:
            return schema["example"]
        else:
            results = {}
            required = schema.get("required", [])

            for name, val in schema.get("properties", {}).items():
                r = extract_schema_examples(val)
                if r is not None or name in required:
                    results[name] = r
            return results
    elif schema_type == "array":
        return [extract_schema_examples(schema.get("items", {}))]
    elif schema_type == "boolean":
        return random.choice([True, False])
    elif schema_type == "integer":
        return random.randint(schema.get("minimum", 0), schema.get("maximum", 10))
    elif schema_type == "number":
        return round(random.uniform(schema.get("minimum", 0), schema.get("maximum", 100)))
    elif schema_type == "string":
        format_type = schema.get("format", "")
        if format_type == "date-time":
            return "2024-01-01T12:00:00Z"
        elif format_type == "date":
            return "2024-01-01"
        elif format_type == "email":
            return "user@example.com"
        else:
            return "string"
    else:
        return None


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
    elif typ == "Any":
        return '["foo", "bar"]'
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
    template_env.filters["quotify"] = (
        lambda val: "'{}'".format(val) if isinstance(val, str) else val
    )
    client_template = template_env.get_template("client.py.jinja2")
    test_template = template_env.get_template("test_client.py.jinja2")

    api = filter(flatten(fetchapi()))
    paths = api["paths"]

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
        context = {"module": os.path.splitroot(module)[-1].replace("/", "."), "methods": []}
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
            method["example"] = {}

            logger.debug("%s(%s) -> %s", methodname, http_method, json.dumps(path_vals))

            # Collect the argument names and types
            if "parameters" in path_vals:
                params = path_vals["parameters"]
                for param in params:
                    method["params"].append(
                        {
                            "param": param["name"],
                            "kwarg": snakecase(param["name"]),
                            "type": TYPE_MAP[param["schema"]["type"]],
                            "desc": " ".join(param.get("description", "").splitlines()),
                            "required": param.get("required", False),
                        }
                    )
                    if param.get("required", False):
                        method["required"].append(param["name"])
                method["example"].update(extract_param_examples(params))

            if "requestBody" in path_vals:
                # TODO: Technically we should test for the '$ref' case first
                schema = path_vals["requestBody"]["content"]["application/json"]["schema"]
                assert schema["type"] == "object"
                method["required"].extend(schema.get("required", []))
                method["example"].update(extract_schema_examples(schema))
                for name, val in schema["properties"].items():
                    method["json"].append(
                        {
                            "param": name,
                            "kwarg": snakecase(name),
                            "type": TYPE_MAP[val.get("type", "any")],
                            "desc": " ".join(val.get("description", "").splitlines()),
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
            schema = success[0]["content"]["application/json"]["schema"]

            assert "type" in schema
            if schema["type"] == "object":
                method["rtype"] = "dict"
                for name, val in schema["properties"].items():
                    logger.debug("%s : %s", name, val)
                    method["rprops"].append(
                        {
                            "name": snakecase(name),
                            "type": TYPE_MAP[val.get("type", "object")],
                            "desc": " ".join(val.get("description", "").splitlines()),
                        }
                    )
            elif schema["type"] == "array":
                method["rtype"] = "list"

            # Add our method to
            context["methods"].append(method)

        content = client_template.render(context)
        with open(modpath, "w") as fobj:
            fobj.write(content)

        content = test_template.render(context)
        with open(testspath, "w") as fobj:
            fobj.write(content)


if __name__ == "__main__":
    generate()

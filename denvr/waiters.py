import time

from typing import Tuple, Callable, Union


class Waiter:
    """
    A utility class which waits on a check function to return True after executing an action function.
    For example, waiting for `get_server` to return status "ONLINE" after calling `create_server`.

    Args:
        action (callable): Function which takes kwargs, runs an operation and returns a response.
        check (callable): Function which takes the action response and returns (bool, result) representing
            whether a check has passed and any results to return.
        cleanup (callable): An optional function to run in failure conditions.
    """

    def __init__(
        self, action: Callable, check: Callable, cleanup: Union[Callable, None] = None
    ):
        self.action = action
        self.check = check
        self.cleanup = cleanup

    def __call__(self, interval=30, timeout=600, **kwargs):
        resp = self.action(**kwargs)
        try:
            return self.wait(resp, interval, timeout)
        except Exception as e:
            if self.cleanup:
                self.cleanup(resp)
            raise e

    def wait(self, resp, interval=30, timeout=600):
        start_time = time.time()

        # Loop until check succeeds or timeout occurs
        while True:
            passes, result = self.check(resp)
            if passes:
                return result

            if time.time() - start_time > timeout:
                raise TimeoutError("Wait operation timed out")

            time.sleep(interval)


def waiter(operation: Callable) -> Waiter:
    """
    A waiter factory function that creates a Waiter instance for a given operation.

    Example:

        create_server = waiter(virtual.create_server)
        create_server(name="my-test-vm", rpool="on-demand", vpc="denvr", ...)

    Args:
        operation: The operation to wait for.

    Returns:
        A Waiter instance.

    Raises:
        ValueError: If the operation is not supported.
    """
    # NOTE: This function is a bit of a hack that could use a more declarative approach for describing waiter rules.
    # Arguably each service client should be responsible for this, but that would complicate the existing code generation.
    client = getattr(operation, "__self__", None)
    if client is None:
        raise ValueError(f"Operation must be a method of a client. Not {operation}.")

    class_name = getattr(client.__class__, "__name__", "")
    module_name = getattr(client, "__module__", "")
    method_name = getattr(operation, "__name__", "")

    if client and class_name == "Client" and module_name.startswith("denvr"):
        if module_name.endswith("virtual"):
            if method_name in ["create_server", "start_server"]:
                return Waiter(
                    action=operation, check=lambda resp: _vm_online_check(client, resp)
                )
            elif method_name == "stop_server":
                return Waiter(
                    action=operation, check=lambda resp: _vm_offline_check(client, resp)
                )
        elif module_name.endswith("applications"):
            if method_name in [
                "create_catalog_application",
                "create_custom_application",
                "start_application",
            ]:
                return Waiter(
                    action=operation, check=lambda resp: _app_online_check(client, resp)
                )
            elif method_name == "stop_application":
                return Waiter(
                    action=operation, check=lambda resp: _app_offline_check(client, resp)
                )

    # If we don't find a waiter configuration then raise a ValueError
    raise ValueError(f"Unsupported operation: {module_name}.{class_name}/{method_name}")


def _vm_online_check(client, resp: dict) -> Tuple[bool, dict]:
    result = client.get_server(
        id=resp["id"], namespace=resp["namespace"], cluster=resp["cluster"]
    )
    is_online = result["status"] == "ONLINE"
    return is_online, result


def _vm_offline_check(client, resp: dict) -> Tuple[bool, dict]:
    result = client.get_server(
        id=resp["id"], namespace=resp["namespace"], cluster=resp["cluster"]
    )
    is_offline = result["status"] == "OFFLINE"
    return is_offline, result


def _app_online_check(client, resp: dict) -> Tuple[bool, dict]:
    result = client.get_application_details(id=resp["id"], cluster=resp["cluster"])
    is_online = result["instance_details"]["status"] == "ONLINE"
    return is_online, result


def _app_offline_check(client, resp: dict) -> Tuple[bool, dict]:
    result = client.get_application_details(id=resp["id"], cluster=resp["cluster"])
    is_offline = result["instance_details"]["status"] == "OFFLINE"
    return is_offline, result

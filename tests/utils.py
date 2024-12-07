import os
from contextlib import contextmanager


@contextmanager
def temp_env():
    """
    Really simple context manager to simplify the config environment variable tests.
    """
    _environ = dict(os.environ)
    try:
        yield
    finally:
        os.environ.clear()
        os.environ.update(_environ)

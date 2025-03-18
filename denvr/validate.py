import json
import logging

from typing import Dict

logger = logging.getLogger(__name__)


def validate_kwargs(method, path, kwargs, required):
    """
    For `None` values in `kwargs` error if they are in `required` or drop them.
    """
    result: Dict[str, Dict] = {}
    for kw, args in kwargs.items():
        result[kw] = {}
        for k, v in args.items():
            if v is None:
                if k in required:
                    raise TypeError(
                        f"Required {kw} parameter {k} is missing for {method} request to {path}"
                    )

                logger.debug("Dropping missing %s argument %s", kw, k)
            elif kw == "params" and isinstance(v, bool):
                # Handle converting True to 'true' for boolean params
                result[kw][k] = json.dumps(v)
            else:
                result[kw][k] = v

    return result

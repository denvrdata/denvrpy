import logging

logger = logging.getLogger(__name__)


def validate_kwargs(method, path, kwargs, required):
    """
    For `None` values in `kwargs` error if they are in `required` or drop them.
    """
    result = {}
    for kw, args in kwargs.items():
        result[kw] = {}
        for k, v in args.items():
            if v is None:
                if k in required:
                    raise TypeError(f"Required {kw} parameter {k} is missing for {method} request to {path}")

                logger.debug("Dropping missing %s argument %s", kw, k)
            else:
                result[kw][k] = v

    return result
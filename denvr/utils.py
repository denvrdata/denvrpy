import logging
import typing

from requests import JSONDecodeError, HTTPError, Response

logger = logging.getLogger(__name__)


def snakecase(text: str) -> str:
    """
    Convert camelcase and titlecase strings to snakecase.

    Args:
        str (str): The string to convert.

    Returns:
        str: The converted string.
    """
    return "".join(["_" + i.lower() if i.isupper() else i for i in text]).lstrip("_")


# We'll disable mypy for this function since we're largely trying to match the requests code.
@typing.no_type_check
def raise_for_status(resp: Response):
    """
    Given a response object return either resp.json() or resp.json()["error"].
    This is basically just a modified version of
    https://requests.readthedocs.io/en/latest/_modules/requests/models/#Response.raise_for_status

    Args:
        resp (Response): The request response object.

    Returns:
        The request response error.
    """
    # Early exit if everything is fine.
    if resp.status_code < 400:
        return None

    # Start building the error message that we'll raise
    if isinstance(resp.reason, bytes):
        # We attempt to decode utf-8 first because some servers
        # choose to localize their reason strings. If the string
        # isn't utf-8, we fall back to iso-8859-1 for all other
        # encodings. (See PR #3538)
        try:
            reason = resp.reason.decode("utf-8")
        except UnicodeDecodeError:
            reason = resp.reason.decode("iso-8859-1")
    else:
        reason = resp.reason

    details = ""
    try:
        details = " - {}".format(resp.json()["error"]["message"])
    except JSONDecodeError:
        logger.debug("Failed to decode JSON response")
    except KeyError:
        logger.debug("Failed to extract error message from response")

    msg = ""
    if 400 <= resp.status_code < 500:
        msg = f"{resp.status_code} Client Error: {reason} for url: {resp.url}{details}"
    elif 500 <= resp.status_code < 600:
        msg = f"{resp.status_code} Server Error: {reason} for url: {resp.url}{details}"

    if msg:
        raise HTTPError(msg, response=resp)

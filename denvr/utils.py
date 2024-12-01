def snakecase(text: str) -> str:
    """
    Convert camelcase and titlecase strings to snakecase.

    Args:
        str (str): The string to convert.

    Returns:
        str: The converted string.
    """
    return "".join(["_" + i.lower() if i.isupper() else i for i in text]).lstrip("_")

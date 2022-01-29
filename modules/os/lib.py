import os


def _fr(path):
    """
    Convert Back Slashes to forward slashes

    Args:
        path (str): system path

    Returns:
        str: system path converted
    """
    return path.replace(os.sep, "/")
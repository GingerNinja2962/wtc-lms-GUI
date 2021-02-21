import os


def dirCheck(dirPath):
    """
    Check whether the directory exists and if not make it.

    Parameters
    ----------
    dirPath : str
        The path to the directory being checked.

    Returns
    -------
    dirPath : str
        The path to the checked directory.
    """
    if not os.path.exists(dirPath):
        os.mkdir(dirPath)
    return dirPath

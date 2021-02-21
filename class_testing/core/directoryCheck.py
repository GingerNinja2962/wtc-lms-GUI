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


def fileCheck(filePath):
    """
    Checks whether the file at the specified path exists.

    Parameters
    ----------
    filePath : str
        The path to the file to be checked.

    Returns
    -------
    checkStatus : bool
        The status of the check, False is failed, True if passed
    """
    if not os.path.isfile(filePath):
        return False
    return True

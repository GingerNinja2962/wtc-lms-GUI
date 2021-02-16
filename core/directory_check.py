import os

def dir_check(dir_path):
    """
    check whether the directory exists and if not make it then return the path

    :param dir_path: the path to the directory being checked
    """
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    return dir_path


def writeToFile(contents, filePath):
    """
    Write content to the specifide file path.
    
    Parameters
    ----------
        contents : str
            The message to be written.
        filePath : str
            The path to the file to be written to.
    """
    with open(filePath, "w") as timeCheckFile:
        timeCheckFile.write(contents)


def readFromFile(filePath):
    """
    Read from the specifide file path.
    
    Parameters
    ----------
        filePath : str
            The path to the file to be read from.

    Returns
    -------
        contents : str
            The contents of the read file.
    """
    with open(filePath, "r") as timeCheckFile:
        contents = timeCheckFile.read()
    return contents

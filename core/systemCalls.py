from subprocess import PIPE, Popen, check_output


def systemCallComms(systemCall):
    """
    Return the system output and errors of a subprocess.

    Parameters
    ----------
    systemCall : subprocess
        the subprocess from which the output and errors are extracted from.

    Returns
    -------
    subprocessOutput : tuple (output, errors)
        the terminal output and errors returned from the subprocess
    """
    return systemCall.communicate()


def systemCallClose(systemCall):
    """
    Close the subprocess call.

    Parameters
    ----------
    systemCall : subprocess
        The subprocess to be closed.
    """
    systemCall.stdout.close()


def grepSystemCall(filters, pattern, stdinProcess):
    """
    Start a grep subprocess call searching a set stdin subprocess.

    Parameters
    ----------
    filters : str
        The filters used in grep e.g. -i or -A1.
    pattern : str
        The pattern to be used in the grep subprocess call.
    stdinProcess : subprocess
        The subprocess to be greped.

    Returns
    -------
    grepProcess : subprocess
        The grep subprocess.
    """
    grepProcess = Popen(["grep", filters,pattern],stdin=stdinProcess.stdout,
            universal_newlines=True, stdout=PIPE)
    return grepProcess


def grepCall(filters, pattern, searchFile):
    """
    Start a grep subprocess call searching a file.

    Parameters
    ----------
    filters : str
        The filters used in grep e.g. -i or -A1.
    pattern : str
        The pattern to be used in the grep subprocess call.
    searchFile : str
        The file to be greped.

    Returns
    -------
    grepProcess : subprocess
        The grep subprocess.
    """
    grepProcess = Popen(["grep", filters, pattern, searchFile],
            universal_newlines=True, stdout=PIPE)
    return grepProcess


def lmsCall(command):
    """
    Start a wtc-lms subprocess call.

    Parameters
    ----------
    command : str, list
        The command to be used with wtc-lms.

    Returns
    -------
    lmsSubprocess : subprocess
        The wtc-lms subprocess.
    """
    if isinstance(command, str):
        return Popen(["wtc-lms", command], stdout=PIPE, universal_newlines=True)
    elif isinstance(command, list):
        return Popen(command, stdout=PIPE, universal_newlines=True)
    else:
        return Popen(["wtc-lms", "help"], stdout=PIPE, universal_newlines=True)

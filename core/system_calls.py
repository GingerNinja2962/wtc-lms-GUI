from subprocess import PIPE, Popen, check_output


def system_call_comms(system_call):
    """
    return the system output and errors

    :param system_call: the system_call object to be comunicated with
    :return out: the terminal output
    :return err: the error values returned from subproces
    """
    return system_call.communicate()


def system_call_close(system_call):
    """
    close the system call

    :param system_call: the system_call object to be closed
    """
    system_call.stdout.close()


def lms_call(command):
    """
    handles the lms calls

    :param command: the command to be used with wtc-lms
    :return lms_process: the process run by the subprocess
    """
    if isinstance(command, str):
        return Popen(["wtc-lms", command], stdout=PIPE, universal_newlines=True)
    elif isinstance(command, list):
        return Popen(command, stdout=PIPE, universal_newlines=True)
    else:
        return Popen(["wtc-lms", "help"], stdout=PIPE, universal_newlines=True)


def grep_system_call(filters, pattern, stdin_process):
    """
    handles the grep calls taking in a stdin

    :param filters: the filters used in grep e.g. -i or -A1
    :param pattern: the pattern to be used in the grep process call
    :param stdin_process: the process to be greped
    :return grep_process: the grep process run by the subprocess
    """
    grep_process = Popen(["grep", filters,pattern],stdin=stdin_process.stdout,
            universal_newlines=True, stdout=PIPE)
    return grep_process


def grep_call(filters, pattern, search_file):
    """
    handles the grep calls that search files

    :param filters: the filters used in grep e.g. -i or -A1
    :param pattern: the pattern to be used in the grep process call
    :param search_file: the file to be greped
    :return grep_process: the grep process run by the subprocess
    """
    grep_process = Popen(["grep", filters,pattern,search_file],
            universal_newlines=True, stdout=PIPE)
    return grep_process
from pathlib import Path

import reviews
import core


def valid_uuid(checked_uuid):
    """
    a small function that checks to see if the UUID is valid
    and returns the buttons to enable

    :param checked_uuid: the entered uuid to be checked
    """
    uuid_file = f"{Path.home()}/bin/lms_GUI/problems_data/.reviews_data.txt"

    if checked_uuid == '':
        return [True]*4

    if checked_uuid.count('-') < 3:
        return [True]*4

    if checked_uuid in core.read_from_file(uuid_file):
        grep_process = core.grep_call("-i", checked_uuid, uuid_file)
        (temp_out, err) = core.system_call_comms(grep_process)
        if "Assigned" in temp_out:
            return [False, True, False, False]
        if "Invited" in temp_out:
            return [False, False, True, True]
        else:
            return [False, True, True, True]
    return [True]*4


def problem_selection(values):
    """
    a small function to build a grep pattern from the selected filters
    and then call the subprocess to run the command to return the results

    :param values: this is the window values that are currently active
    """

    reviews_data_path = f"{Path.home()}/bin/lms_GUI/problems_data/.reviews_data.txt"

    if values['-TOGGLE-ALL-']:
        grep_process = core.grep_call("-i", ">", reviews_data_path)
    else:
        grep_process = core.grep_call("-i", f"{values['-PROBLEM-'][0]}", reviews_data_path)

    grep_pattern = ""
    if values['-INVITED-']:
        grep_pattern = grep_pattern + 'Invited'

    if values['-ASSIGNED-']:
        if grep_pattern != "": grep_pattern = grep_pattern + "|"
        grep_pattern = grep_pattern + 'Assigned'

    if values['-GRADED-']:
        if grep_pattern != "": grep_pattern = grep_pattern + "|"
        grep_pattern = grep_pattern + 'Graded'

    if values['-BLOCKED-']:
        if grep_pattern != "": grep_pattern = grep_pattern + "|"
        grep_pattern = grep_pattern + 'AcceptanceBlocked'

    if grep_pattern != "":
        filtered_process = core.grep_system_call("-Ei", grep_pattern, grep_process)
        (out, err) = core.system_call_comms(filtered_process)
        print(out)
    else:
        (out, err) = core.system_call_comms(grep_process)
        print(out)
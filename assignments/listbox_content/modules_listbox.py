import os

import core


def modules_listbox_contents():
    """
    check whether new data needs to be loaded or not

    :return topics_uuid_link: a dictionary linking the topic uuids to modules
    """
    save_path = (f"{os.getcwd()}/.save_data/data_modules/.modules.txt")

    lms_modules_grep = core.grep_call("-i", " \[", f"{save_path}")
    (lms_modules_data, err) = core.system_call_comms(lms_modules_grep)

    lms_modules_data = lms_modules_data.split("\n")
    new_modules_data = []

    for string in lms_modules_data:
        string = string.replace(')', '')
        string = string.split(" (")
        if string != ['']:
            new_modules_data.append(string[0])

    return new_modules_data

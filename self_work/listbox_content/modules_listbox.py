from pathlib import Path

import os

import reviews
import core


def get_new_module_data(save_file):
    """
    a simple function to return new module data and store it

    :param save_file: this is the file location to save the data to
    :return lms_modules_data: this is the dictionary linking topics uuid's to modules
    """
    lms_modules = core.lms_call("modules")
    lms_modules_grep = core.grep_system_call("-iA3", "]", lms_modules)
    core.system_call_close(lms_modules)
    (lms_modules_data, err) = core.system_call_comms(lms_modules_grep)
    core.write_to_file(lms_modules_data, save_file)
    reviews.token_handeler.force_time_update()
    return lms_modules_data


def get_old_module_data(save_file):
    """
    a simple function to get old module data

    :param save_file: this is the file location to read the data from
    :return lms_modules_data: this is the dictionary linking topics uuid's to modules
    """
    lms_modules_grep = core.grep_call("-iA3", "]", save_file)
    (lms_modules_data, err) = core.system_call_comms(lms_modules_grep)
    return lms_modules_data


def modules_listbox_contents():
    """
    a simple function to check whether new data needs to be loaded or not

    :return topics_uuid_link: a dictionary linking the topic uuids to modules
    """
    save_path = f"{Path.home()}/bin/lms_GUI/problems_data/modules_data"
    save_file = ".modules.txt"

    if not os.path.isdir(save_path):
        os.mkdir(save_path)
        lms_modules_data = get_new_module_data(f"{save_path}/{save_file}")

    elif os.path.isfile(f"{save_path}/{save_file}") and not reviews.token_handeler.time_check():
        lms_modules_data = get_old_module_data(f"{save_path}/{save_file}")

    else:
        lms_modules_data = get_new_module_data(f"{save_path}/{save_file}")

    lms_modules_data = lms_modules_data.replace("(", "\n")
    lms_modules_data = lms_modules_data.replace(")", "\n")
    lms_modules_data = lms_modules_data.split('\n')
    for item in lms_modules_data:
        if item == '': lms_modules_data.remove('')

    topics_uuid_link = {}

    for index, item in enumerate(lms_modules_data[0::4]):
        if item == '':
            continue
        topics_uuid_link[item] = lms_modules_data[(index*4)+1]

    return topics_uuid_link

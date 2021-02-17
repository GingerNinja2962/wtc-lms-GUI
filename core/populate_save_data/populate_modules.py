import os

import core


def populate_modules():
    """
    download all modules data and saves it
    """
    save_data_path = core.dir_check(f"{os.getcwd()}/.save_data/data_modules")
    modules_data_path = save_data_path + "/.modules.txt"

    lms_modules = core.lms_call("modules")
    lms_modules_grep = core.grep_system_call("-iA3", "]", lms_modules)

    core.system_call_close(lms_modules)
    (lms_modules_data, err) = core.system_call_comms(lms_modules_grep)

    core.write_to_file(lms_modules_data, modules_data_path)
    core.force_token_update("assignment")

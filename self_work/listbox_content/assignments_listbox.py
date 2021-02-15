from pathlib import Path

import os

import reviews
import core


def get_new_problem_data(problem_uuid, save_file):
    """
    a simple function to return new problem data and store it

    :param problem_uuid: this is the uuid for the selected problem
    :param save_file: this is the file location to save the data to
    :return lms_problem_data: this data returned from the lms problems process call
    """
    lms_problems = core.lms_call(["wtc-lms","problems", problem_uuid])
    lms_problems_grep = core.grep_system_call("-iA3", "]", lms_problems)
    core.system_call_close(lms_problems)
    (lms_problems_data, err) = core.system_call_comms(lms_problems_grep)
    core.write_to_file(lms_problems_data, save_file)
    reviews.token_handeler.force_time_update()
    return lms_problems_data


def get_old_problem_data(save_file):
    """
    a simple function to get old problem data from a file

    :param save_file: this is the file location to save the data to
    :return lms_problem_data: this data returned from the read file
    """
    lms_problems_grep = core.grep_call("-iA3", "]", save_file)
    (lms_problems_data, err) = core.system_call_comms(lms_problems_grep)
    return lms_problems_data


def problems_listbox_contents(problem_uuid, window):
    """
    a simple function to check whether new data needs to be loaded or not

    :param probelm_uuid: this is the uuid for the topic holding the problems
    :param window: this is the window containing the elements to be updated
    :return problems_uuid_link: a dictionary linking the problem uuids to problems
    """
    save_path = f"{Path.home()}/bin/lms_GUI/problems_data/problems_data"
    save_file = f".{problem_uuid}problems.txt"

    if not os.path.isdir(save_path):
        os.mkdir(save_path)
        lms_problems_data = get_new_problem_data(problem_uuid, f"{save_path}/{save_file}")

    elif os.path.isfile(f"{save_path}/{save_file}") and not reviews.token_handeler.time_check():
        lms_problems_data = get_old_problem_data(f"{save_path}/{save_file}")

    else:
        lms_problems_data = get_new_problem_data(problem_uuid, f"{save_path}/{save_file}")

    if "Not Started" in lms_problems_data:
        pass

    elif "Started" in lms_problems_data:
        pass

    else:
        return state_in_progress(window, lms_problems_data)


def state_in_progress(window, lms_problems_data):
    """
    a simple function to return the correct data for assignments in a state of in progresss

    :param window: this is the window containing the elements to be updated
    :param lms_problem_data: this data returned from the lms problems process call
    """
    lms_problems_data = lms_problems_data.replace("(", "\n")
    lms_problems_data = lms_problems_data.replace(")", "\n")
    lms_problems_data = lms_problems_data.split('\n')
    for item in lms_problems_data:
        if '----' in item: lms_problems_data.remove(item)
        if item == '': lms_problems_data.remove('')

    problems_uuid_link = {}
    for index, item in enumerate(lms_problems_data[0::2]):
        if item == '':
            continue
        problems_uuid_link[item] = lms_problems_data[(index*2)+1]

    window.FindElement('-PROBLEM-').Update(
        values=[item for item in problems_uuid_link.keys() if item != ''])

    # print(problems_uuid_link)           # TODO remove
    return problems_uuid_link

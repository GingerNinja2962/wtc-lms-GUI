import PySimpleGUI as sg

import os

import core


def combo_box():
    """
    generates a list of combo boxes and the elements inside each

    :return cobo_box_layout: the list of combo boxs
    """
    module_dict = get_all_problems()
    layout = []
    i = 0
    for module_name in module_dict.keys():
        i += 1
        layout.append([ sg.Text(f"Module: {module_name}") ])
        layout.append([ sg.Combo(module_dict[module_name],
                key=f"-PROBLEM-{i}-", size=(40,1), default_value=None) ])
    return layout


def get_all_problems():
    """
    returns a list of all the assignments

    :return assignments_list: the list of all the assignments
    """
    save_path = core.dir_check(f"{os.getcwd()}/.save_data")
    if not os.path.exists(save_path + "/data_modules/.modules.txt"):
        core.populate_save_data.populate_topics()
        core.populate_save_data.populate_problems()

    lms_modules_grep = core.grep_call("-i", " \[", f"{save_path}/data_modules/.modules.txt")
    (lms_modules_data, err) = core.system_call_comms(lms_modules_grep)

    lms_modules_data = lms_modules_data.replace("\n", " (").replace(')', '')
    lms_modules_data = lms_modules_data.split(" (")

    modules_list = [ item for item in lms_modules_data[0::2] if item != '']

    modules_problems_dict = {}
    for topic_name in modules_list:
        save_path = f"{os.getcwd()}/.save_data/data_topics"
        lms_topics_grep = core.grep_call("-i", " \[", f"{save_path}/{topic_name}.txt")
        (lms_topics_data, err) = core.system_call_comms(lms_topics_grep)
        if lms_topics_data == "": continue

        lms_topics_data = lms_topics_data.replace("\n", " (").replace(')', '')
        lms_topics_data = lms_topics_data.split(" (")
        topics_list = [ item for item in lms_topics_data[0::2] if item != '']

        save_path = f"{os.getcwd()}/.save_data/data_problems"
        problems_list = []
        for problem_name in topics_list:
            lms_problems_grep = core.grep_call("-i", " \[", f"{save_path}/{problem_name}.txt")
            (lms_problems_data, err) = core.system_call_comms(lms_problems_grep)
            if lms_problems_data == "": continue

            lms_problems_data = lms_problems_data.replace("\n", " (").replace(')', '')
            lms_problems_data = lms_problems_data.split(" (")

            for item in lms_problems_data[0::2]:
                if item != "": problems_list.append(item)
        modules_problems_dict[f"{topic_name}"] = problems_list

    return modules_problems_dict

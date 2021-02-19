import PySimpleGUI as sg

import os

import core


def combo_box():
    """
    generates a tabGroup that holds Tabs names after modules holding the problems for that module

    :return tab_group_layout: the tabgroup holding tabs and listboxes
    """
    module_dict = get_all_problems()
    layout = []
    i = 0
    for module_name in module_dict.keys():
        i += 1
        listbox_layout = []
        for item in module_dict[module_name]:
            listbox_layout.append([item])

        module_name = module_name.split(" [")

        layout.append( sg.Tab( module_name[0], [ [ sg.Listbox( listbox_layout,
                key=f"-PROBLEM-{i}-", size=(40,22),) ] ], pad=(0, 20) ) )

    return [ [ sg.TabGroup( [layout] ) ] ]


def get_all_problems():
    """
    returns a dictionary of all the assignments linked to the module as akey

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
                if item != "" and item != "Coding Clinic Booking System [In Progress]":
                    problems_list.append(item)
        modules_problems_dict[f"{topic_name}"] = problems_list

    return modules_problems_dict

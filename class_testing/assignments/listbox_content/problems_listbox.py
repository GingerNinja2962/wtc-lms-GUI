import os

import core


def problems_listbox_contents(topic_name, window):
    """
    update the Problems listbox to contain the new loaded problems

    :param topic_name: the name of the topic to show the problems for 
    :param window: this is the window containing the elements to be updated
    """
    save_path = f"{os.getcwd()}/.save_data/data_problems"
    save_file = f"{topic_name}.txt"

    if core.token_check("assignment"):
        core.populate_save_data.populate_problems()

    lms_problems_grep = core.grep_call("-i", " \[", f"{save_path}/{save_file}")
    (lms_problems_data, err) = core.system_call_comms(lms_problems_grep)

    lms_problems_data = lms_problems_data.split("\n")
    new_problems_data = []

    for string in lms_problems_data:
        string = string.replace(')', '')
        string = string.split(" (")
        if string != ['']:
            new_problems_data.append(string[0])

    if new_problems_data != []:
        window['-PROBLEM-'].Update(disabled=False)
        window['-PROBLEM-'].Update(values=new_problems_data)
    else:
        window['-PROBLEM-'].Update(values=new_problems_data)
        window['-PROBLEM-'].Update(disabled=True)

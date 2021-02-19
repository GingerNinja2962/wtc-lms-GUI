import os

import core


def topics_listbox_contents(module_name, window):
    """
    update the topics_listbox to contain the new loaded topics

    :param module_name: the name of the module to show the topics for
    :param window: this is the window containing the elements to be updated
    """
    save_path = f"{os.getcwd()}/.save_data/data_topics"
    save_file = f"{module_name}.txt"

    if core.token_check("assignment"):
        core.populate_save_data.populate_topics()

    lms_topics_grep = core.grep_call("-i", " \[", f"{save_path}/{save_file}")
    (lms_topics_data, err) = core.system_call_comms(lms_topics_grep)

    lms_topics_data = lms_topics_data.split("\n")
    new_topics_data = []

    for string in lms_topics_data:
        string = string.replace(")", '')
        string = string.split(" (")
        if string != ['']:
            new_topics_data.append(string[0])

    if new_topics_data != []:
        window['-TOPIC-'].Update(disabled=False)
        window['-TOPIC-'].Update(values=new_topics_data)

    else:
        window['-TOPIC-'].Update(values=[''])
        window['-TOPIC-'].Update(disabled=True)

    window['-PROBLEM-'].Update(values=[''])
    window['-PROBLEM-'].Update(disabled=True)

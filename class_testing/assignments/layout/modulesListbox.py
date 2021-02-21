import os

from core import populateProblemsClass 


class assignmentsListboxClass(populateProblemsClass):
    def __init__(self):
        super().__init__()


# TODO convert modules_listbox_contents into class method
# def modules_listbox_contents():
#     """
#     check whether new data needs to be loaded or not

#     :return topics_uuid_link: a dictionary linking the topic uuids to modules
#     """
#     save_path = (f"{os.getcwd()}/.save_data/data_modules/.modules.txt")

#     lms_modules_grep = core.grep_call("-i", " \[", f"{save_path}")
#     (lms_modules_data, err) = core.system_call_comms(lms_modules_grep)

#     lms_modules_data = lms_modules_data.split("\n")
#     new_modules_data = []

#     for string in lms_modules_data:
#         string = string.replace(')', '')
#         string = string.split(" (")
#         if string != ['']:
#             new_modules_data.append(string[0])

#     return new_modules_data


# TODO convert topics_listbox_contents into class method
# def topics_listbox_contents(module_name, window):
#     """
#     update the topics_listbox to contain the new loaded topics

#     :param module_name: the name of the module to show the topics for
#     :param window: this is the window containing the elements to be updated
#     """
#     save_path = f"{os.getcwd()}/.save_data/data_topics"
#     save_file = f"{module_name}.txt"

#     if core.token_check("assignment"):
#         core.populate_save_data.populate_topics()

#     lms_topics_grep = core.grep_call("-i", " \[", f"{save_path}/{save_file}")
#     (lms_topics_data, err) = core.system_call_comms(lms_topics_grep)

#     lms_topics_data = lms_topics_data.split("\n")
#     new_topics_data = []

#     for string in lms_topics_data:
#         string = string.replace(")", '')
#         string = string.split(" (")
#         if string != ['']:
#             new_topics_data.append(string[0])

#     if new_topics_data != []:
#         window['-TOPIC-'].Update(disabled=False)
#         window['-TOPIC-'].Update(values=new_topics_data)

#     else:
#         window['-TOPIC-'].Update(values=[''])
#         window['-TOPIC-'].Update(disabled=True)

#     window['-PROBLEM-'].Update(values=[''])
#     window['-PROBLEM-'].Update(disabled=True)


# TODO convert problems_listbox_contents into class method
# def problems_listbox_contents(topic_name, window):
#     """
#     update the Problems listbox to contain the new loaded problems

#     :param topic_name: the name of the topic to show the problems for 
#     :param window: this is the window containing the elements to be updated
#     """
#     save_path = f"{os.getcwd()}/.save_data/data_problems"
#     save_file = f"{topic_name}.txt"

#     if core.token_check("assignment"):
#         core.populate_save_data.populate_problems()

#     lms_problems_grep = core.grep_call("-i", " \[", f"{save_path}/{save_file}")
#     (lms_problems_data, err) = core.system_call_comms(lms_problems_grep)

#     lms_problems_data = lms_problems_data.split("\n")
#     new_problems_data = []

#     for string in lms_problems_data:
#         string = string.replace(')', '')
#         string = string.split(" (")
#         if string != ['']:
#             new_problems_data.append(string[0])

#     if new_problems_data != []:
#         window['-PROBLEM-'].Update(disabled=False)
#         window['-PROBLEM-'].Update(values=new_problems_data)
#     else:
#         window['-PROBLEM-'].Update(values=new_problems_data)
#         window['-PROBLEM-'].Update(disabled=True)

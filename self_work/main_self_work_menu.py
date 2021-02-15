import PySimpleGUI as sg

import problems_data
import self_work

def own_work_menu():
    """
    Function to get all assigned reviews
    """
    layout, modules_dict = self_work.problem_selection_layout()
    topics_dicts = {}
    assignments_dict = {}

    window = sg.Window("LMS Assignment Gui", layout, element_justification='c', location=(500, 300))

    while 1:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            window.close()
            return False

        if event == "Back":
            window.close()
            return True

        if event == "-MODULE-":
            topics_dict = self_work.listbox_content.topics_listbox_contents(
                modules_dict[values["-MODULE-"][0]],
                window
            )

        if event == "-TOPIC-":
            problems_dict = self_work.listbox_content.problems_listbox_contents(
                topics_dict[values["-TOPIC-"][0]],
                window
            )

        if event == "-PROBLEM-":
            self_work.frame_layout.assignment_buttons_update(
                problems_dict[values["-PROBLEM-"][0]],
                window
            )

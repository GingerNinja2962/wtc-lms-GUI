import PySimpleGUI as sg

import assignments
import settings
import reviews
import core

def assignments_main_menu():
    """
    the main menu for selecting assignments
    """
    layout = assignments.problem_selection_layout()

    core.populate_save_data.populate_save_data()

    window = sg.Window("LMS Assignment Gui", layout, element_justification='c', location=(300, 200))

    while 1:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            window.close()
            return False

        if values["-SETTINGS-MENU-"] == "General Settings":
            settings.general_settings()

        elif values["-NAVIGATE-MENU-"] == "   Main Menu":
            window.close()
            return True

        elif values["-NAVIGATE-MENU-"] == "   Reviews Menu":
            window.close()
            return reviews.review_problem()

        if event == "-MODULE-":
            assignments.listbox_content.topics_listbox_contents(
                values["-MODULE-"][0], window )
            assignments.frame_layout.reset_buttons(window)

        if event == "-TOPIC-":
            assignments.listbox_content.problems_listbox_contents(
                values["-TOPIC-"][0], window )
            assignments.frame_layout.reset_buttons(window)

        if event == "-PROBLEM-":
            assignments.frame_layout.assignment_buttons_update(
                values["-PROBLEM-"][0], window)
        
        if event == '-START-':
            settings.general_settings()
        if event == '-SAVE-':
            settings.general_settings()
        if event == '-GRADE-':
            settings.general_settings()
        if event == '-HISTORY-':
            settings.general_settings()

import PySimpleGUI as sg

import assignments
import settings
import reviews
import core


def assignments_main_menu():
    """
    the main menu for selecting assignments
    """
    if core.token_check("assignment"):
        core.populate_save_data.populate_save_data("assignments")

    layout = assignments.problem_selection_layout()

    window = sg.Window("LMS Assignment Gui", layout, element_justification='c',
        location=(300, 200)).finalize()

    event, values = window.read(timeout=1)

    if assignments.listbox_content.modules_listbox_contents() == []:
        window["-MODULE-"].Update(disabled=True)

    while 1:
        event, values = window.read(timeout=5000)

        if core.token_check("assignment"):
            core.populate_save_data.populate_save_data("assignments")

        if event in (sg.WIN_CLOSED, "Exit"):
            window.close()
            return False

        elif values["-SETTINGS-MENU-"] == "General Settings":
            settings.general_settings()

        elif values["-SETTINGS-MENU-"] == "Change Theme":
            settings.theme_menu()

        elif values["-SETTINGS-MENU-"] == "Update Assignments":
            core.populate_save_data.populate_save_data("assignments")
            window["-MODULE-"].Update(disabled=False)
            window["-MODULE-"].Update(
                assignments.listbox_content.modules_listbox_contents())
            window["-TOPIC-"].Update([''])
            window['-TOPIC-'].Update(disabled=True)
            window["-PROBLEM-"].Update([''])
            window['-PROBLEM-'].Update(disabled=True)

        elif values["-NAVIGATE-MENU-"] == "    Main Menu":
            window.close()
            return True

        elif values["-NAVIGATE-MENU-"] == "    Reviews Menu":
            window.close()
            if core.token_check("review"):
                core.populate_save_data.populate_save_data("reviews")
            return reviews.review_problem()

        elif event == "-MODULE-":
            assignments.listbox_content.topics_listbox_contents(
                values["-MODULE-"][0], window )
            assignments.frame_layout.reset_buttons(window)

        elif event == "-TOPIC-":
            assignments.listbox_content.problems_listbox_contents(
                values["-TOPIC-"][0], window )
            assignments.frame_layout.reset_buttons(window)

        elif event == "-PROBLEM-":
            assignments.frame_layout.assignment_buttons_update(
                values["-PROBLEM-"][0], window)
        
        elif event == '-START-':
            settings.general_settings()
        elif event == '-SAVE-':
            settings.general_settings()
        elif event == '-GRADE-':
            settings.general_settings()
        elif event == '-HISTORY-':
            settings.general_settings()

import PySimpleGUI as sg

import assignments
import settings
import reviews


def main_menu(running):
    """
    the main menu for the lms system,
    choose whether you are going to do reviews or assignments
    """

    if running:
        #TODO get menu full functionality
        menu_def = [ ['File', ['Settings', 'Exit'] ],
                    ['Login', ['login'] ],
                    ['Help', ['About'] ] ]

        layout = [ [ sg.Menu([ ['File', ['Settings', 'Exit'] ] ],
            tearoff=False, )],
            [ sg.Column([[sg.Button('Assignments')]]),
            sg.VSeperator(),
            sg.Column([[sg.Button('Reviews')]]) ] ]

        window = sg.Window("Lms Gui", layout, element_justification='c', location=(500, 300))

    while running:
        event, _ = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            window.close()
            running = False

        if event == "Settings":
            settings.general_settings()

        if event == "Assignments":
            window.close()
            running = assignments.assignments_main_menu()
            break

        if event == "Reviews":
            if reviews.load_reviews():
                window.close()
                running = reviews.review_problem()
                break

    if running:
        main_menu(running)
    return

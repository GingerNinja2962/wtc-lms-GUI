import PySimpleGUI as sg

import assignments
import settings
import reviews


def main_menu(running):
    """
    the main menu for the lms system,
    choose whether you are going to do reviews or assignments
    """
    version_num = 1.3

    if running:
        window = sg.Window("Lms GUI", main_menu_layout(),
            element_justification='c', location=(500, 300))

    while running:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            window.close()
            running = False

        elif values["-SETTINGS-MENU-"] == "General Settings":
            settings.general_settings()

        elif event == "Assignments":
            window.close()
            running = assignments.assignments_main_menu()
            break

        elif event == "Reviews":
            if reviews.load_reviews():
                window.close()
                running = reviews.review_problem()
                break

    if running:
        main_menu(running)
    return


def main_menu_layout():
    """
    returns the layout for the main menu

    :return layout: the layout for the main menu
    """
    settings_menu_items = ["Unused", ["&Change Theme", "General Settings"]]
    exit_menu_items   =   ["Unused", ["&Exit"]]
    about_menu_items   =   ["Unused", ["&About"]]

    return [
        [
            sg.ButtonMenu("Settings",  settings_menu_items, key="-SETTINGS-MENU-", size=(9,1)),
            sg.Text("", pad=(98,0)),
            sg.Button("About", pad=(0,0)),
            sg.Button("Exit", pad=(0,0))
        ],
        [sg.HSeparator()],
        [
            sg.Text("\n\nThis is a custom made GUI for the lms menu.\n"+
                    "\nPlease note this is a beta test and not the\n"+
                    "final product, thus it is subject to constant change\n\n",
                    font="Calibri 9")
        ],
        [sg.HSeparator()],
        [
            sg.Column([[sg.Button("Assignments")]]),
            sg.VSeperator(pad=(100,0)),
            sg.Column([[sg.Button("Reviews")]])
        ]
    ]

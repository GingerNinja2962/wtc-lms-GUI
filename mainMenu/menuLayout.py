import PySimpleGUI as sg


def layout():
    """
    Creates the layout for the main menu.

    Returns
    -------
    mainMenuLayout : list
        The layout to be used by the main menu GUI.
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
import PySimpleGUI as sg

import assignments


def problem_selection_layout():
    """
    sets up the basic problem selection layout for
        assignments and returns it as a list

    :return layout: the layout list that
    """
    settings_menu_items = ["Unused", ["&General Settings", "&Change Theme", "&Update Assignments"]]
    navigate_menu_items = ["Unused", ["    &Main Menu", "!> & Assignments Menu", "    &Reviews Menu"]]
    help_menu_items = ["Unused", ["&About"]]

    return [
        [ sg.ButtonMenu("Settings",  settings_menu_items, key="-SETTINGS-MENU-",
            size=(9,1), font="Calibri 9"),
            sg.ButtonMenu("Navigate", navigate_menu_items, key="-NAVIGATE-MENU-",
            size=(9,1), font="Calibri 9"),
            sg.ButtonMenu("Help", help_menu_items, key="-HELP-MENU-",
            size=(8,1), font="Calibri 9"),
            sg.Text("", pad=(305,0)),
            sg.Button("Exit", pad=(0,0))
        ],
        [ sg.HSeparator() ],
        [ sg.Column(
            [ [ sg.Text("Modules", font="Calibri 9") ],
                [ sg.Column(
                [ [ sg.Listbox(
                    values=assignments.listbox_content.modules_listbox_contents(),
                    size=(30,20), key="-MODULE-", enable_events=True) ] ]
            ), ] ], element_justification='c' ),
        sg.Column(
            [ [ sg.Text("Topics", font="Calibri 9") ],
            [ sg.Column(
                [ [ sg.Listbox(values=[],
                    size=(35,20), key="-TOPIC-",enable_events=True,
                    disabled=True) ] ] ),
            ] ], element_justification='c' ),
        sg.Column(
            [ [ sg.Text("Assignments", font="Calibri 9") ],
                [ sg.Column(
                    [ [ sg.Listbox(values=[],
                        size=(40,20), key="-PROBLEM-",enable_events=True,
                        disabled=True) ] ]
                ) ]
            ], element_justification='c' ),
        sg.Text("", pad=(10,0)),
        sg.Column(
            [ [ sg.Text("Actions", font="Calibri 9") ],
                [ sg.Frame(title="Operations",
                    layout=assignments.frame_layout.assignment_buttons_frame(),
                    pad=(0,82)) ],
            ], element_justification='c')
        ]
    ]

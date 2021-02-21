import PySimpleGUI as sg

# import reviews


def problem_selection_layout():
    """
    sets up the basic problem selection for reviews

    :return layout: the layout list that
    """
    settings_menu_items = ["Unused", ["&General Settings", "&Change Theme", "&Update Reviews"]]
    navigate_menu_items = ["Unused", ["   &Main Menu", "   &Assignments Menu", "!>& Reviews Menu"]]
    help_menu_items = ["Unused", ["&About"]]

    layout = [
        [ sg.ButtonMenu("Settings",  settings_menu_items, key="-SETTINGS-MENU-",
                size=(9,1), item_font="Calibri 9"),
            sg.ButtonMenu("Navigate", navigate_menu_items, key="-NAVIGATE-MENU-",
                size=(9,1), item_font="Calibri 9"),
            sg.ButtonMenu("Help", help_menu_items, key="-HELP-MENU-", size=(8,1),
                item_font="Calibri 9"),
            sg.Text("", pad=(490,0)),
            sg.Button("Exit", pad=(0,0))
        ],
        [ sg.HSeparator() ],
        [ sg.Column(
            [ [ sg.Text("Please select an assignment: ",
            font="Calibri 12") ],
            [
                sg.Column( reviews.layout.tab_group(), pad=(5,0) ),
                sg.Column(
                    [ [ sg.Frame("Filters", Filter_Frame, # TODO change this to function call
                            title_color="#FF8C00", title_location="n",
                            font="Calibri 10") ],
                        [ sg.Frame("Review Count", Review_count_Frame, # TODO change this to function call
                            title_color="#FF8C00", title_location="n",
                            element_justification="l", font="Calibri 10")
                    ] ],
                    element_justification="c", pad=(5,0)) ] ], pad=(0,10) ),
            sg.VSeparator(pad=(5,0)),
            sg.Column( [
                [ sg.Output(size=(110, 30), key="-OUTPUT-", pad=(0,20))],
                [ sg.Text("UUID", font="Calibri 10"), sg.InputText( "",
                        tooltip="The UUID you wish to work with", key="-INPUT-"),
                    sg.Button("Review details", disabled=True,
                        tooltip="View the details of the review"),
                    sg.Button("Accept", disabled=True,
                        tooltip="Accepts the review invitation"),
                    sg.Button("Comment", disabled=True,
                        tooltip="Add a comment to the review"),
                    sg.Button("Grade", disabled=True,
                        tooltip="Grade the review")
                ]
            ] )
        ]
    ]

    return layout

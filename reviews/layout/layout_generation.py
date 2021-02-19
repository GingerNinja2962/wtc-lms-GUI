import PySimpleGUI as sg

import os

import reviews
import core


def problem_selection_layout():
    """
    sets up the basic problem selection for reviews

    :return layout: the layout list that
    """
    Filter_Frame = reviews.layout.review_filter_frame()
    Review_count_Frame = reviews.layout.review_counter_frame()
    Toggle_all_Frame = reviews.layout.toggle_all_frame()

    settings_menu_items = ["Unused", ["&Change Theme", "General Settings"]]
    navigate_menu_items = ["Unused", ["   &Main Menu", "   &Assignments Menu", "!>& Reviews Menu"]]
    help_menu_items = ["Unused", ["&About"]]

    layout = [
        [ sg.ButtonMenu("Settings",  settings_menu_items, key="-SETTINGS-MENU-", size=(9,1)),
            sg.ButtonMenu("Navigate", navigate_menu_items, key="-NAVIGATE-MENU-", size=(9,1)),
            sg.ButtonMenu("Help", help_menu_items, key="-HELP-MENU-", size=(8,1)),
            sg.Text("", pad=(490,0)),
            sg.Button("Exit", pad=(0,0))
        ],
        [ sg.Column(
            [ [ sg.Text("Please select an assignment: ") ],
            [
                sg.Column( reviews.layout.combo_box() ),
                sg.Column(
                    [ [ sg.Frame("Search all assignments", Toggle_all_Frame,
                        title_color="#FF8C00", title_location="n", pad=(0,5) ) ],
                        [ sg.Frame("Filters", Filter_Frame, title_color="#FF8C00",
                        title_location="n", pad=(0,5)) ],
                        [ sg.Frame("Review Count", Review_count_Frame,
                        title_color="#FF8C00", title_location="n",
                        element_justification="l", pad=(0,5)) ] ],
                element_justification="c") ], ] ),
        sg.VSeparator(),
        sg.Column( [
            [ sg.Output(size=(110, 30), key="-OUTPUT-")],
            [ sg.Text("UUID"), sg.InputText( "",
                tooltip="The UUID you wish to work with", key="-INPUT-"),
                sg.Button("Review details", disabled=True,
                tooltip="View the details of the review"),
                sg.Button("Accept", disabled=True, tooltip="Accepts the review invitation"),
                sg.Button("Comment", disabled=True, tooltip="Add a comment to the review"),
                sg.Button("Grade", disabled=True, tooltip="Grade the review") ] ] )
        ]
    ]

    return layout

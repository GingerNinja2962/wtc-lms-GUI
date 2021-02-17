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

    #TODO make menu functional
    menu_def = [ ['File', ['Main Menu','Settings', 'Exit'] ],
                ['Login', ['login'] ],
                ['Help', ['About'] ] ]

    menu_def = [ ['File', ['Main Menu', 'Settings', 'Exit'] ] ]

    layout = [
        [ sg.Menu(menu_def, tearoff=False, )],
        [ sg.Column([
        [ sg.Text('Please select an assignment: ')],
        [ sg.Column([ [] ]) ],
        [ sg.Column(reviews.layout.combo_box()),
        sg.Column([ [sg.Frame('Search all assignments', Toggle_all_Frame,
        title_color='#FF8C00')],
        [ sg.Frame('Filters', Filter_Frame, title_color='#FF8C00',
        key='-FILTERS-')],
        [ sg.Frame('Review Count', Review_count_Frame, title_color='#FF8C00')],
        [ sg.Button('Update review data')] ]) ], ]),
        sg.VSeparator(),
        sg.Column([
        [ sg.Output(size=(110, 30), key='-OUTPUT-')],
        [ sg.Text('UUID'), sg.InputText( '',
        tooltip='Check to see commands for UUid', key='-INPUT-'),
        sg.Button('⟳', tooltip='Checks if the UUID is valid or not.'),
        sg.Button('Review details', disabled=True,
        tooltip='List the details of the review'),
        sg.Button('Accept', disabled=True, tooltip='Accepts the review invitation'),
        sg.Button('Comment', disabled=True, tooltip='Add a comment to a review'),
        sg.Button('Grade', disabled=True, tooltip='Grade review')]
        ]) ]
    ]

    return layout

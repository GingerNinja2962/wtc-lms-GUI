import PySimpleGUI as sg

import assignments


def problem_selection_layout():
    """
    sets up the basic problem selection layout for
        assignments and returns it as a list

    :return layout: the layout list that
    """
    return [
        [ 
            sg.Column(
                [ [ sg.Text('Please select a module: ') ],
                [ sg.Column(
                [ [ sg.Listbox(
                values=assignments.listbox_content.modules_listbox_contents(),
                size=(30,20), key='-MODULE-', enable_events=True) ],
                [ sg.Button('Back',tooltip='Go back to wtc-lms main menu') ] ]
                ), ] ]
            ),sg.VSeparator(),
            sg.Column(
                [ [ sg.Text('Please select a topic: ') ],
                [ sg.Column(
                    [ [ sg.Listbox(values=[],
                    size=(35,20), key='-TOPIC-',enable_events=True,
                    disabled=True) ] ]
                ), ] ]
            ),sg.VSeparator(),
            sg.Column(
                [ [ sg.Text('Please select an assignment: ') ],
                [ sg.Column(
                    [ [ sg.Listbox(values=[],
                    size=(40,20), key='-PROBLEM-',enable_events=True,
                    disabled=True) ] ]
                ), ] ]
            ),sg.VSeparator(),
            sg.Column(
                [ [ sg.Text('Please select a operation: ') ],
                [ sg.Column(
                    [ [ sg.Frame(title='Operations',
                    layout=assignments.frame_layout.assignment_buttons_frame()) ] ]
                ), ] ]
            ), ] ]

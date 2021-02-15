import PySimpleGUI as sg

import problems_data
import self_work
import reviews


def problem_selection_layout():
    """
    a small function that sets up the basic problem selection for reviews

    :return layout: the layout list that
    """
    modules_dict = self_work.listbox_content.modules_listbox_contents()

    layout = [
        [ 
            sg.Column(
                [ [ sg.Text('Please select a module: ') ],
                [ sg.Column(
                    [ [ sg.Listbox(values=[item for item in modules_dict.keys() if item != ''],
                    size=(30,20), key='-MODULE-', enable_events=True) ],
                    [ sg.Button('Back',tooltip='Go back to wtc-lms main menu') ] ]
                ), ] ]
            ),sg.VSeparator(),
            sg.Column(
                [ [ sg.Text('Please select a topic: ') ],
                [ sg.Column(
                    [ [ sg.Listbox(values=[],
                    size=(35,20), key='-TOPIC-', enable_events=True) ] ]
                ), ] ]
            ),sg.VSeparator(),
            sg.Column(
                [ [ sg.Text('Please select an assignment: ') ],
                [ sg.Column(
                    [ [ sg.Listbox(values=[],
                    size=(40,20), key='-PROBLEM-', enable_events=True) ] ]
                ), ] ]
            ),sg.VSeparator(),
            sg.Column(
                [ [ sg.Text('Please select a operation: ') ],
                [ sg.Column(
                    [ [ sg.Frame(title='Operations', layout=self_work.frame_layout.assignment_buttons_frame()) ] ]
                ), ] ]
            ), ] ]

    return layout, modules_dict
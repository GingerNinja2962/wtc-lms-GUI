import PySimpleGUI as sg


def assignment_buttons_frame():
    """
    a small function that returns a assignment button frame with 4 wtc-lms assignment options

    :return assignment_frame: a frame containing the options for wtc-lms assignments
    """
    return [
        [sg.Button('Start', key='-START-', disabled=True,
            tooltip="Start the assignment and clone into the assignment folder",
            size=(6,1), pad=(1,1))],
        [sg.Button('Save', key='-SAVE-', disabled=True,
            tooltip="Save your work to the wtc-lms cloud server",
            size=(6,1), pad=(1,1))],
        [sg.Button('Grade', key='-GRADE-', disabled=True,
            tooltip="Submit your work for grading",
            size=(6,1), pad=(1,1))],
        [sg.Button('History', key='-HISTORY-', disabled=True,
            tooltip="View the History of your graded assignment",
            size=(6,1), pad=(1,1))]
    ]

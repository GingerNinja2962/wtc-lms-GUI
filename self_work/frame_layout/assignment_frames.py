import PySimpleGUI as sg


def assignment_buttons_frame():
    """
    a small function that returns a assignment button frame with 4 wtc-lms assignment options

    :return assignment_frame: a frame containing the options for wtc-lms assignments
    """
    assignment_frame = [
        [sg.Button('Start', key='-START-', disabled=True,
        tooltip="Start the assignment and clone into the assignment folder")],
        [sg.Button('Save', key='-SAVE-', disabled=True,
        tooltip="Save your work to the wtc-lms cloud server")],
        [sg.Button('Grade', key='-GRADE-', disabled=True,
        tooltip="Submit your work for grading")],
        [sg.Button('History', key='-HISTORY-', disabled=True,
        tooltip="View the History of your graded assignment")]
        ]
    return assignment_frame


def assignment_buttons_update(problem_uuid, window):
    """
    a simple function to check which button to re-ebable or disable and do so

    :param problem_uuid: the uuid for the problem that the buttons need to be reconfigured to
    :param window: the sg object containing all the elements for the program window
    """
    pass
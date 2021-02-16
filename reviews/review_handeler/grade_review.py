import PySimpleGUI as sg

import reviews
import core


def grade_review(probelm_uuid, window):
    """
    manages adding a grade to the review

    :param probelm_uuid: the UUID for the probelm
    :param window: this is the window that holds all elements
    """
    event, values = sg.Window('WTC-LMS GUI add a grade',
    [[sg.Text("Would you like to Grade the following review?")],
    [sg.Text('Grade'), sg.Spin(values=('1','2','3','4','5','6','7','8','9','10'),
    initial_value='10', tooltip='Choose the grade to give',
    key='-GRADE-', size=(3,3))],[sg.Text("***Please note this cannot be undone***")],
    [sg.HSeparator()], [sg.Button('Submit'),
    sg.Button('Cancel')]],location=(500, 300)).read(close=True)

    if event == "Submit":
        grade_review_process = core.lms_call(["wtc-lms","grade_review",
        probelm_uuid, f"{values['-GRADE-']}"])
        (grade_review_data, err) = core.system_call_comms(grade_review_process)

        reviews.review_handeler.review_details(probelm_uuid, window)

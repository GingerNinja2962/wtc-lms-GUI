import PySimpleGUI as sg

import reviews
from core import lmsCall, systemCallComms


def gradeReview(probelmUUID):
    """
    Creates a pop up window to allow the user to add a grade to a
    review.

    Parameters
    ----------
        probelmUUID : str
            The UUID for the probelm that the grade is being given to.
    """
    event, values = sg.Window('WTC-LMS GUI add a grade',
        [[sg.Text("Would you like to Grade the following review?")],
        [sg.Text('Grade'),
        sg.Spin(values=('1','2','3','4','5','6','7','8','9','10'),
        initial_value='10', tooltip='Choose the grade to give',
        key='-GRADE-', size=(3,3))],
        [sg.Text("***Please note that this cannot be undone***")],
        [sg.HSeparator()], [sg.Button('Submit'),
        sg.Button('Cancel')]],location=(500, 300)).read(close=True)

    if event == "Submit":
        gradeReviewProcess = lmsCall(["wtc-lms","grade_review",
        probelmUUID, f"{values['-GRADE-']}"])
        (gradeReviewData, err) = systemCallComms(gradeReviewProcess)

        reviews.reviewHandeler.reviewDetailsPopup(probelmUUID)

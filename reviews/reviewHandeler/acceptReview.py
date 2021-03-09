import PySimpleGUI as sg

import reviews
import core


def acceptReview(probelmUUID, window):
    """
    a function that will accept the review

    :param probelmUUID: the UUID for the probelm
    :param window: this is the window that holds all elements
    """
    request = sg.popup("Would you like to Accept the following review?",
            f"{reviews.reviewHandeler.returnReviewDetails(probelmUUID)}",
            "***Please note this cannot be undone & may take a few seconds***",
            title="WTC-LMS accept a review",
            custom_text=("Accept", "Cancel"),
            location=(500, 300))

    if request == "Accept":
        acceptReviewProcess = core.lmsCall(["wtc-lms","accept", probelmUUID])
        (out, err) = core.systemCallComms(acceptReviewProcess)

        reviews.reviewHandeler.reviewDetailsPopup(probelmUUID)

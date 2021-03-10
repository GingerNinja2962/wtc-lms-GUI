import PySimpleGUI as sg

import reviews
from core import lmsCall, systemCallComms


def acceptReview(probelmUUID):
    """
    Accept a review from wtc-lms.

    Parameters
    ----------
        probelmUUID : str
            The UUID for the probelm to be accepted.
    """
    request = sg.popup("Would you like to Accept the following review?",
        f"{reviews.reviewHandeler.returnReviewDetails(probelmUUID)}",
        "***Please note that this cannot be undone & may take a few seconds***",
        title="WTC-LMS accept a review",
        custom_text=("Accept", "Cancel"),
        location=(500, 300))

    if request == "Accept":
        acceptReviewProcess = lmsCall(["wtc-lms","accept", probelmUUID])
        (out, err) = systemCallComms(acceptReviewProcess)

        reviews.reviewHandeler.reviewDetailsPopup(probelmUUID)

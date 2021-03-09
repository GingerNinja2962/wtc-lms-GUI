import PySimpleGUI as sg

import core


def reviewDetailsPopup(probelmUUID):
    """
    displays the review details in a popup

    :param probelmUUID: the UUID for the probelm
    :param window: this is the window that holds all elements
    """
    sg.popup(f"{returnReviewDetails(probelmUUID)}",
              title="Review Details",
              location=(500, 300))


def returnReviewDetails(probelmUUID):
    """
    returns the review details

    :param probelmUUID: the UUID for the probelm
    :return review_details: the review details for the problem uuid
    """
    reviewDetailsProcess = core.lmsCall(["wtc-lms","review_details", probelmUUID])
    (reviewDetailsData, err) = core.systemCallComms(reviewDetailsProcess)

    return reviewDetailsData

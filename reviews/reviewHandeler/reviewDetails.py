import PySimpleGUI as sg

from core import lmsCall, systemCallComms


def reviewDetailsPopup(probelmUUID):
    """
    Display the review details in a popup window.

    Parameters
    ----------
        probelmUUID : str
            The problem UUID that will have its' reviews details
            shown.
    """
    sg.popup(f"{returnReviewDetails(probelmUUID)}",
              title="Review Details",
              location=(500, 300))


def returnReviewDetails(probelmUUID):
    """
    Return the review details for the given problemUUID.

    Parameters
    ----------
        probelmUUID : [type]
            The UUID of problem of which review details is needed.

    Returns
    -------
        reviewDetailsData : str
            The review details for the given problem UUID.
    """
    reviewDetailsProcess = lmsCall(["wtc-lms","review_details", probelmUUID])
    (reviewDetailsData, err) = systemCallComms(reviewDetailsProcess)

    return reviewDetailsData

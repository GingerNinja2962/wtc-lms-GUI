import PySimpleGUI as sg

import reviews
import core


def accept_review(probelm_uuid, window):
    """
    a function that will accept the review

    :param probelm_uuid: the UUID for the probelm
    :param window: this is the window that holds all elements
    """
    request = sg.popup("Would you like to Accept the following review?",
            f"{reviews.review_handeler.return_review_details(probelm_uuid)}",
            "***Please note this cannot be undone & may take a few seconds***",
            title="WTC-LMS accept a review",
            custom_text=("Accept", "Cancel"),
            location=(500, 300))

    if request == "Accept":
        accept_review_process = core.lms_call(["wtc-lms","accept", probelm_uuid])
        (accept_review_data, err) = core.system_call_comms(accept_review_process)

        reviews.review_handeler.review_details(probelm_uuid, window)

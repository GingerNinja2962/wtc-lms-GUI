import PySimpleGUI as sg

import core


def review_details_popup(probelm_uuid):
    """
    displays the review details in a popup

    :param probelm_uuid: the UUID for the probelm
    :param window: this is the window that holds all elements
    """
    sg.popup(f"{return_review_details(probelm_uuid)}",
              title="Review Details",
              location=(500, 300))


def return_review_details(probelm_uuid):
    """
    returns the review details

    :param probelm_uuid: the UUID for the probelm
    :return review_details: the review details for the problem uuid
    """
    review_details_process = core.lms_call(["wtc-lms","review_details", probelm_uuid])
    (review_details_data, err) = core.system_call_comms(review_details_process)

    return review_details_data

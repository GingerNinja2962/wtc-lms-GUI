import core


def review_details(probelm_uuid, window):
    """
    displays the review details

    :param probelm_uuid: the UUID for the probelm
    :param window: this is the window that holds all elements
    """
    review_details_process = core.lms_call(["wtc-lms","review_details", probelm_uuid])
    (review_details_data, err) = core.system_call_comms(review_details_process)

    window['-OUTPUT-'].Update('')
    print(("\n"+' '*20)+"UUID  :  "+f"{probelm_uuid}"+"\n")
    print(review_details_data)


def return_review_details(probelm_uuid):
    """
    returns the review details

    :param probelm_uuid: the UUID for the probelm
    :return review_details: the review details for the problem uuid
    """
    review_details_process = core.lms_call(["wtc-lms","review_details", probelm_uuid])
    (review_details_data, err) = core.system_call_comms(review_details_process)

    return review_details_data

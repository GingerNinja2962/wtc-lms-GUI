import os

import core


def populate_reviews():
    """
    download all review data and saves it
    """
    save_data_path = core.dir_check(f"{os.getcwd()}/.save_data/data_reviews")

    reviews_data_process = core.lms_call("reviews")
    (reviews_data, err) = core.system_call_comms(reviews_data_process)

    core.write_to_file(reviews_data,
        save_data_path + "/.reviews_data.txt")
    core.force_token_update("review")


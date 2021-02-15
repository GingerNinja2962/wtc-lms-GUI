from pathlib import Path
import os

import PySimpleGUI as sg

import reviews
import core


def fetch_lms_reviews():
    """
    a function that will fetch the stored lms reviews

    :return reviews_data: the reviews data
    """
    save_file = f"{Path.home()}/bin/lms_GUI/problems_data/.reviews_data.txt"

    if os.path.exists(save_file):
        return True

    else:
        request = sg.popup("No saved review data has been found",
            "would you like to update the data automatically or load a save file?",
            "Please note that loading new data will need an active internet connection",
            title="WTC-LMS GUI [Work In Progress]",
            custom_text=("update", "load save"),
            location=(500, 300))

        if request == "update":
            data_download()
            return True

        elif request == "load save":
            file_to_load = sg.popup_get_file(
                "Please select the file to load:",
                title="reviews save data",
                default_path=f"{Path.home()}",
                grab_anywhere=True)
            try:
                loadeddata = core.read_from_file(file_to_load)
                core.write_to_file(loadeddata, save_file)
                return True
            except:
                return False
        return False


def data_download():
    """
    this function only downloads and pickls the data
    """
    reviews_data_process = core.lms_call("reviews")
    (reviews_data, err) = core.system_call_comms(reviews_data_process)

    save_file = f"{Path.home()}/bin/lms_GUI/problems_data/.reviews_data.txt"

    core.write_to_file(reviews_data, save_file)


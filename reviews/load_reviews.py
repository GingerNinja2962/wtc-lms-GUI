import PySimpleGUI as sg

import os

import core


def load_reviews():
    """
    check for the stored lms reviews and if non are found load them

    :return reviews_data: the reviews data
    """
    save_file = f"{os.getcwd()}/.save_data/data_reviews/.reviews_data.txt"
    if os.path.exists(save_file): return True

    else:
        request = sg.popup("No saved review data has been found",
"would you like to update the data automatically or load a save file?",
"Please note that loading new data will need an active internet connection",
            title="WTC-LMS GUI [Work In Progress]",
            custom_text=("update", "load save"),
            location=(500, 300))

        if request == "update":
            core.populate_save_data.populate_reviews()
            return True

        elif request == "load save":
            file_to_load = sg.popup_get_file(
                "Please select the file to load:",
                title="reviews save data",
                default_path=f"{os.getcwd()}",
                grab_anywhere=True)
            try:
                loadeddata = core.read_from_file(file_to_load)
                save_file = core.dir_check(f"{os.getcwd()}/.save_data")
                core.dir_check(save_file + "/data_reviews")
                core.write_to_file(loadeddata, save_file)
                return True
            except:
                return False
        return False

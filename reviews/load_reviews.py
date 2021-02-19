import PySimpleGUI as sg

import os

import core


def load_reviews():
    """
    check for the stored lms reviews and if non are found load them

    :return reviews_data: the reviews data
    """
    save_file = f"{os.getcwd()}/.save_data/data_reviews/.reviews_data.txt"
    modules_file = f"{os.getcwd()}/.save_data/data_modules/.modules.txt"

    if os.path.exists(save_file) and os.path.exists(modules_file):
        if core.token_check("review"):
            core.populate_save_data.populate_save_data("reviews")
        return True

    else:
        event, valuse = sg.Window("lms GUI",
            [
                [ sg.Text("No saved data has been found\n") ],
                [ sg.Text("Would you like to update the data automatically or load a custom save folder?\n") ],
                [ sg.Text("***Please note that updating the data will need an active internet connection.***\n") ],
                [ sg.Button("Update", size=(9,1)), sg.Text("", pad=(50, 0)), sg.Button("Load folder", size=(9,1)) ],
            ], element_justification='c', location=(500, 300)).read(close=True)

        if event == "Update":
            core.populate_save_data.populate_save_data()
            return True

        elif event == "Load folder":
            folder_to_load = sg.popup_get_folder(
                "Please select a folder that holds the following folders:\n" + 
                " - data_modules\n - data_topics\n - data_problems\n - data_reviews\n - tokens",
                title="reviews save data",
                default_path=f"{os.getcwd()}",
                grab_anywhere=True, location=(500, 300))
            try:
                save_path = core.dir_check(f"{os.getcwd()}/.save_data")
                for path, folders, files in os.walk(folder_to_load):
                    if files == []: continue
                    if "data_reviews" in path:
                        data_reviews_file = True
                        save_dir = f"{save_path}/data_reviews"
                    elif "data_modules" in path:
                        data_modules_file = True
                        save_dir = f"{save_path}/data_modules"
                    elif "data_topics" in path:
                        data_topics_file = True
                        save_dir = f"{save_path}/data_topics"
                    elif "data_problems" in path:
                        data_problems_file = True
                        save_dir = f"{save_path}/data_problems"
                    elif "tokens" in path:
                        token_file = True
                        save_dir = f"{save_path}/tokens"
                    else: continue
                    for a_file in files:
                        loadeddata = core.read_from_file(f"{path}/{a_file}")
                        save_file = core.dir_check(f"{save_dir}")
                        core.write_to_file(loadeddata, f"{save_dir}/{a_file}")
                if data_modules_file and data_topics_file \
                    and data_problems_file and data_reviews_file and token_file:
                    return True
            except:
                sg.popup_ok(
                "Sorry that folder was not a valid save folder:\n" +
                "\nA valid save folder holds the following folders with their corrisponding data:\n\n" + 
                " - data_modules\n - data_topics\n - data_problems\n - data_reviews\n - tokens",
                title="reviews save data",
                grab_anywhere=True, location=(500, 300))
                load_reviews()
        return False

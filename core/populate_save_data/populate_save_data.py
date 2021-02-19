import PySimpleGUI as sg

import core
import os


def populate_save_data(prefered_data="ALL"):
    """
    check tokens and updates the reviews, 
    modules, topics, problems and assignments data accordingly

    :param prefered_data: the data to be populated e.g. 'assignments'
            or 'reviews', default if BOTH
    """
    save_data_path = f"{os.getcwd()}/.save_data"

    loading_data_message = sg.Window("Updating Saved Data", 
        [
            [ sg.Text("\nYour save data is being updated.") ],
            [ sg.Text("\nUpdating the saved data may take a minute or two") ],
            [ sg.Text("depending on your internet connection.") ],
        ], element_justification='c', size=(400, 110), location=(500, 300)).finalize()


    if not os.path.exists(save_data_path):
        core.dir_check(save_data_path)

        if prefered_data == "assignment":
            populate_assignments()
        elif prefered_data == "reviews":
            core.populate_save_data.populate_reviews()
        else:
            populate_assignments()
            core.populate_save_data.populate_reviews()
        return

    if prefered_data == "assignment":
        populate_assignments()
    elif prefered_data == "reviews":
        core.populate_save_data.populate_reviews()
    else:
        populate_assignments()
        core.populate_save_data.populate_reviews()

    loading_data_message.close()


def populate_assignments():
    """
    populates all assignments. Modules, Topics and Problems will be reloaded
    """
    core.populate_save_data.populate_modules()
    core.populate_save_data.populate_topics()
    core.populate_save_data.populate_problems()
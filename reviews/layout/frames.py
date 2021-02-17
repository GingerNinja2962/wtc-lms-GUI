import PySimpleGUI as sg

import os

import reviews
import core


def review_filter_frame():
    """
    returns a filter frame with 4 review filters

    :return filter_frame: a frame containing the filters for reviews
    """
    return [
        [sg.CB('Invited', key='-INVITED-')],
        [sg.CB('Assigned', key='-ASSIGNED-')],
        [sg.CB('Graded', key='-GRADED-')],
        [sg.CB('AcceptanceBlocked', key='-BLOCKED-')]
        ]


def toggle_all_frame():
    """
    returns a filter frame with a toggle all CheckBox

    :return Toggle_all_Frame: a frame containing a toggle CheckBox for all reviews
    """
    return [ [ sg.CB('Search all', key='-TOGGLE-ALL-') ] ]
    

def review_counter_frame():
    """
    returns a sg frame that holds the wtc-lms graded assignments counted data

    :return review_count_frame: the sg frame list that holds the review counter frame data
    """
    (reviews_done, reviews_pending, reviews_needed) = counter_data()

    return [
        [ sg.Text(f"Reviews Done:\t{reviews_done:0>2}", key='-REVIEWS-DONE-')],
        [ sg.Text(f"Reviews pending:\t{reviews_pending:0>2}",key='-REVIEWS-PENDING-')],
        [ sg.Text(f"Reviews needed:\t{reviews_needed:0>2}",key='-REVIEWS-NEEDED-')]]


def counter_data():
    """
    returns the calculationed counter data for reviews

    :return reviews_done: the number of reviews done
    :return reviews_pending: the number of reviews accepted
    :return reviews_needed: the number of reviews needing to be compleated
    """
    save_data_path = (f"{os.getcwd()}/.save_data/data_reviews/.reviews_data.txt")
    if not os.path.exists(save_data_path) or core.token_check("review"):
        core.populate_save_data.populate_reviews()

    grep_count_process = core.grep_call("-ic", "Graded", save_data_path)
    (reviews_done, err) = core.system_call_comms(grep_count_process)
    if reviews_done == "0\n": reviews_done = "0"

    grep_pending_process = core.grep_call("-ic", "Assigned", save_data_path)
    (reviews_pending, err) = core.system_call_comms(grep_pending_process)
    if reviews_pending == "0\n": reviews_pending = "0"

    all_problems = []
    for module in [item for item in reviews.layout.get_all_problems().values()]:
        for problem in module:
            all_problems.append(problem)

    reviews_needed = (len(all_problems)* 3) - int(reviews_done)
    if reviews_needed < 1: reviews_needed = "0"
    else: reviews_needed = str(reviews_needed)

    return reviews_done, reviews_pending, reviews_needed


def update_counter_frame(window):
    """
    updates the counter information

    :param window: a sg object holding all the window contents and elements
    """
    (reviews_done, reviews_pending, reviews_needed) = counter_data()
    window['-REVIEWS-DONE-'].update(f'Reviews Done:      {reviews_done}')
    window['-REVIEWS-PENDING-'].update(f'Reviews pending:   {reviews_pending}')
    window['-REVIEWS-NEEDED-'].update(f'Reviews needed:    {reviews_needed}')

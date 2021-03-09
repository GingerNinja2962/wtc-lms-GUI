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
        [sg.CB('Search all', key='-TOGGLE-ALL-')],
        [sg.Text("-"*34)],
        # [sg.HSep(pad=(0,10))],
        [sg.CB('Invited', key='-INVITED-')],
        [sg.CB('Assigned', key='-ASSIGNED-')],
        [sg.CB('Graded', key='-GRADED-')],
        [sg.CB('AcceptanceBlocked', key='-BLOCKED-')]
        ]


def review_counter_frame():
    """
    returns a sg frame that holds the wtc-lms graded assignments counted data

    :return review_count_frame: the sg frame list that holds the review counter frame data
    """
    (reviews_done, reviews_pending, reviews_needed) = counter_data()

    return [
        [ sg.Text(f"Reviews Done:\t{reviews_done:0>2}", key='-REVIEWS-DONE-',pad=(5,0))],
        [ sg.Text(f"Reviews pending:\t{reviews_pending:0>2}",key='-REVIEWS-PENDING-',pad=(5,0))],
        [ sg.Text(f"Reviews needed:\t{reviews_needed:0>2}",key='-REVIEWS-NEEDED-',pad=(5,0))]]


def counter_data():
    """
    returns the calculationed counter data for reviews

    :return reviews_done: the number of reviews done
    :return reviews_pending: the number of reviews accepted
    :return reviews_needed: the number of reviews needing to be compleated
    """
    save_data_path = (f"{os.getcwd()}/.save_data/data_reviews/.reviews_data.txt")

    grep_count_process = core.grep_call("-ic", "Graded", save_data_path)
    (reviews_done, err) = core.system_call_comms(grep_count_process)

    grep_pending_process = core.grep_call("-ic", "Assigned", save_data_path)
    (reviews_pending, err) = core.system_call_comms(grep_pending_process)

    reviews_done = reviews_done.replace('\n', '')
    reviews_pending = reviews_pending.replace('\n', '')

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
    window['-REVIEWS-DONE-'].update(f'Reviews Done:\t{reviews_done:0>2}')
    window['-REVIEWS-PENDING-'].update(f'Reviews pending:\t{reviews_pending:0>2}')
    window['-REVIEWS-NEEDED-'].update(f"Reviews needed:\t{reviews_needed:0>2}")

import PySimpleGUI as sg
from pathlib import Path

import problems_data
import reviews
import core


def review_filter_frame():
    """
    a small function that returns a filter frame with 4 wtc-lms review filters

    :return Filter_Frame: a frame containing the filters for wtc-lms reviews
    """
    Filter_Frame = [
        [sg.CB('Invited', key='-INVITED-')],
        [sg.CB('Assigned', key='-ASSIGNED-')],
        [sg.CB('Graded', key='-GRADED-')],
        [sg.CB('AcceptanceBlocked', key='-BLOCKED-')]
        ]
    return Filter_Frame


def toggle_all_frame():
    """
    a small function that returns a filter frame with a toggle all CheckBox for wtc-lms reviews

    :return Toggle_all_Frame: a frame containing a toggle CheckBox for wtc-lms reviews
    """
    return [ [ sg.CB('Search all', key='-TOGGLE-ALL-') ] ]
    

def review_counter_frame():
    """
    function that returns a sg frame that holds the wtc-lms graded assignments counted data

    :return review_count_frame: the sg frame list that holds the wtc-lms review counter frame data
    """
    (reviews_done, reviews_pending, reviews_needed) = counter_data()

    review_count_frame = [
        [ sg.Text(f'Reviews Done:      {reviews_done}', key='-REVIEWS-DONE-')],
        [ sg.Text(f'Reviews pending:   {reviews_pending}',key='-REVIEWS-PENDING-')],
        [ sg.Text(f'Reviews needed:    {reviews_needed}',key='-REVIEWS-NEEDED-')]]

    return review_count_frame


def counter_data():
    """
    a simple function that handles the calculation of counter data for reviews

    :return reviews_done: the number of reviews done
    :return reviews_pending: the number of reviews accepted
    :return reviews_needed: the number of reviews nneding to be compleated
    """    
    reviews_data_path = f"{Path.home()}/bin/lms_GUI/problems_data/.reviews_data.txt"

    grep_count_process = core.grep_call("-ic", "Graded", reviews_data_path)
    (reviews_done, err) = core.system_call_comms(grep_count_process)

    grep_pending_process = core.grep_call("-ic", "Assigned", reviews_data_path)
    (reviews_pending, err) = core.system_call_comms(grep_pending_process)

    reviews_needed = (len(problems_data.review_problems)*3) - int(reviews_done)
    if reviews_needed < 1: reviews_needed = '0'

    return reviews_done, reviews_pending, reviews_needed


def update_counter_frame(window):
    """
    a simple function that updates the counter information

    :param window: a sg object holding all the window contents and elements
    """
    (reviews_done, reviews_pending, reviews_needed) = counter_data()
    window.FindElement('-REVIEWS-DONE-').update(f'Reviews Done:      {reviews_done}')
    window.FindElement('-REVIEWS-PENDING-').update(f'Reviews pending:   {reviews_pending}')
    window.FindElement('-REVIEWS-NEEDED-').update(f'Reviews needed:    {reviews_needed}')
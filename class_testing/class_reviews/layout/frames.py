import PySimpleGUI as sg

import os

import reviews
from core import systemCallClose, systemCallComms, lmsCall, grepCall, grepSystemCall


def reviewFilterFrame():
    """
    returns a filter frame with 4 review filters

    :return filterFrame: a frame containing the filters for reviews
    """
    return [
        [sg.CB('Search all', key='-TOGGLE-ALL-')],
        [sg.Text("-"*34)], # Can be changed to: [sg.HSep(pad=(0,10))],
        [sg.CB('Invited', key='-INVITED-')],
        [sg.CB('Assigned', key='-ASSIGNED-')],
        [sg.CB('Graded', key='-GRADED-')],
        [sg.CB('AcceptanceBlocked', key='-BLOCKED-')]
        ]


def reviewCounterFrame():
    """
    returns a sg frame that holds the wtc-lms graded assignments counted data

    :return reviewCountFrame: the sg frame list that holds the review counter frame data
    """
    (reviewsDone, reviewsPending, reviewsNeeded) = counterData()

    return [
        [ sg.Text(f"Reviews Done:\t{reviewsDone:0>2}", key='-REVIEWS-DONE-',pad=(5,0))],
        [ sg.Text(f"Reviews pending:\t{reviewsPending:0>2}",key='-REVIEWS-PENDING-',pad=(5,0))],
        [ sg.Text(f"Reviews needed:\t{reviewsNeeded:0>2}",key='-REVIEWS-NEEDED-',pad=(5,0))]]


def counterData():
    """
    returns the calculationed counter data for reviews

    :return reviewsDone: the number of reviews done
    :return reviewsPending: the number of reviews accepted
    :return reviewsNeeded: the number of reviews needing to be compleated
    """
    saveDataPath = (f"{os.getcwd()}/.save_data/data_reviews/.reviews_data.txt")

    grepCountProcess = core.grepCall("-ic", "Graded", saveDataPath)
    (reviewsDone, err) = core.systemCallComms(grepCountProcess)

    grepPendingProcess = core.grepCall("-ic", "Assigned", saveDataPath)
    (reviewsPending, err) = core.systemCallComms(grepPendingProcess)

    reviewsDone = reviewsDone.replace('\n', '')
    reviewsPending = reviewsPending.replace('\n', '')

    allProblems = []
    for module in [item for item in reviews.layout.getAllProblems().values()]:
        for problem in module:
            allProblems.append(problem)

    reviewsNeeded = (len(allProblems)* 3) - int(reviewsDone)
    if reviewsNeeded < 1: reviewsNeeded = "0"
    else: reviewsNeeded = str(reviewsNeeded)

    return reviewsDone, reviewsPending, reviewsNeeded


def updateCounterFrame(window):
    """
    updates the counter information

    :param window: a sg object holding all the window contents and elements
    """
    (reviewsDone, reviewsPending, reviewsNeeded) = counterData()
    window['-REVIEWS-DONE-'].update(f'Reviews Done:\t{reviewsDone:0>2}')
    window['-REVIEWS-PENDING-'].update(f'Reviews pending:\t{reviewsPending:0>2}')
    window['-REVIEWS-NEEDED-'].update(f"Reviews needed:\t{reviewsNeeded:0>2}")

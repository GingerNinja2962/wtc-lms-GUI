import os

import reviews
import core


def validUUID(mainWindow): # TODO check if finalized
    """
    Check to if the UUID is valid and return the buttons stats.

    Parameters
    ----------
        mainWindow : object
            The PySimpleGUI window object that has been opened.

    Returns
    -------
        list
            The stats of the buttons according to the UUID entered
    """
    if (mainWindow.values['-INPUT-']
        ) in mainWindow.layout.reviewsData.reviewUUIDs:
        grepReviewProcess = core.grepCall("-i", mainWindow.values['-INPUT-'],
            mainWindow.layout.reviewsData.reviewsPath)
        (tempOut, err) = core.systemCallComms(grepReviewProcess)
        if "Assigned" in tempOut:
            return [False, True, False, False]
        if "Invited" in tempOut:
            return [False, False, True, True]
        else:
            return [False, True, True, True]
    return [True]*4


def problemSelection(mainWindow):
    """
    Build a grep pattern from the selected filters, then call
    the subprocess to run the command and return the results of the
    command run.

    Parameters
    ----------
        mainWindow : object
            The PySimpleGUI window object that has been opened.
    """
    if mainWindow.values['-TOGGLE-ALL-']:
        grepProcess = core.grepCall("-i", " \[",
            mainWindow.layout.reviewsData.reviewsPath)


    elif mainWindow.values[f"-{mainWindow.values[1]}-"] != []:
        grepModuleProcess = core.grepCall("-i", mainWindow.values[1],
            mainWindow.layout.reviewsData.reviewsPath)
        grepProcess = core.grepSystemCall("-i", mainWindow.values[
            f"-{mainWindow.values[1]}-"][0], grepModuleProcess)
        core.systemCallClose(grepModuleProcess)
    else: return

    grepPattern = ""
    if mainWindow.values['-INVITED-']:
        grepPattern = grepPattern + 'Invited'

    if mainWindow.values['-ASSIGNED-']:
        if grepPattern != "": grepPattern = grepPattern + "|"
        grepPattern = grepPattern + 'Assigned'

    if mainWindow.values['-GRADED-']:
        if grepPattern != "": grepPattern = grepPattern + "|"
        grepPattern = grepPattern + 'Graded'

    if mainWindow.values['-BLOCKED-']:
        if grepPattern != "": grepPattern = grepPattern + "|"
        grepPattern = grepPattern + 'AcceptanceBlocked'

    if grepPattern != "":
        filteredProcess = core.grepSystemCall("-Ei", grepPattern, grepProcess)
        (out, err) = core.systemCallComms(filteredProcess)
    else: (out, err) = core.systemCallComms(grepProcess)
    print(out)

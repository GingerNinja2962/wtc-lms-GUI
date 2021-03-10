import os

from core import grepCall, systemCallComms, systemCallClose, grepSystemCall


def validUUID(mainWindow):
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
        grepReviewProcess = grepCall("-i", mainWindow.values['-INPUT-'],
            mainWindow.layout.reviewsData.reviewsPath)
        (tempOut, err) = systemCallComms(grepReviewProcess)
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
        grepProcess = grepCall("-i", " \[",
            mainWindow.layout.reviewsData.reviewsPath)


    elif mainWindow.values[f"-{mainWindow.values[1]}-"] != []:
        grepModuleProcess = grepCall("-i", mainWindow.values[1],
            mainWindow.layout.reviewsData.reviewsPath)
        grepProcess = grepSystemCall("-i", mainWindow.values[
            f"-{mainWindow.values[1]}-"][0], grepModuleProcess)
        systemCallClose(grepModuleProcess)
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
        filteredProcess = grepSystemCall("-Ei", grepPattern, grepProcess)
        (out, err) = systemCallComms(filteredProcess)
    else: (out, err) = systemCallComms(grepProcess)
    print(out)

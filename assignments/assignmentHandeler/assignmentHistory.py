import PySimpleGUI as sg

from classTemplates import baseWindowClass

import core


class assignmentHistory(baseWindowClass):
    """
    A class to be used to view the History of an assignment from
    wtc-lms.

    Parameters
    ----------
        baseWindowClass : class
            The base window class to inherit from.

    Attributes
    ----------
        mainWindow : object
            The PySimpleGUI window object that has been opened.

    Methods
    -------
        getLayout()
            Creates the layout list setting the font to monospace and
            calling getHistoryData() to get the data.
        getHistoryData()
            Runs the lms history command on the given UUID and returns
            the output from lms. 
    """
    def __init__(self, mainWindow):
        """
        The constructor for assignmentHistory.

        Parameters
        ----------
            mainWindow : object
                The PySimpleGUI window object that has been opened.
        """
        super().__init__()
        self.mainWindow = mainWindow
        self.location = (55, 150)
        self.getLayout()
        self.run()


    def getLayout(self):
        """
        Creates the layout list setting the font to monospace and
        calling getHistoryData() to get the data.
        """
        self.layout = [
            [ sg.Text(self.getHistoryData(), font="monospace 10") ],
            [sg.Button("Close")]
        ]


    def getHistoryData(self):
        """
        Runs the lms history command on the given UUID and returns the
        output from lms. 

        Returns
        -------
            assignmentHistoryData : str
                The output from lms after running the history command.
        """
        assignmentHistoryProcess = core.lmsCall(["wtc-lms","history",
            self.mainWindow.layout.listboxs.assignmentsDict[
            self.mainWindow.values["-PROBLEM-"][0]]])
        (assignmentHistoryData, err) = core.systemCallComms(
            assignmentHistoryProcess)
        return assignmentHistoryData

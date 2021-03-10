import PySimpleGUI as sg

import core


class assignmentSave:
    """
    A class to be used to save assignments from wtc-lms.

    Attributes
    ----------
        mainWindow : object
            The PySimpleGUI window object that has been opened.

    Methods
    -------
        lmsSaveAssignment()
            Start a subprocess calling lms to save an assignment.
        openMessage()
            Open a saving data message that will remain open until
            closed.
        closeMessage()
            Close the saving data message stored in this instance of
            the class.
    """
    def __init__(self, mainWindow):
        """
        The constructor for assignmentSave.

        Parameters
        ----------
            mainWindow : object
                The PySimpleGUI window object that has been opened.
        """
        self.mainWindow = mainWindow
        self.openMessage()
        self.lmsSaveAssignment()
        self.closeMessage()


    def lmsSaveAssignment(self):
        """
        Start a subprocess calling lms to save an assignment.
        """
        assignmentSaveProcess = core.lmsCall(["wtc-lms","save",
            self.mainWindow.layout.listboxs.assignmentsDict[
            self.mainWindow.values["-PROBLEM-"][0]]])
        (assignmentSaveData, err) = core.systemCallComms(assignmentSaveProcess)


    def openMessage(self):
        """
        Open a saving data message that will remain open until closed.
        """
        self.savingMessage = sg.Window(f"Saving your assignment",
            [
                [ sg.Text(f"\nYour assignment is being saved.") ],
                [ sg.Text(f"Saving your assignment may take a minute or two") ],
                [ sg.Text("depending on your internet connection.") ],
            ], element_justification='c', size=(400, 110), location=(500, 300)
        ).finalize()


    def closeMessage(self):
        """
        Close the saving data message stored in this instance of the
        class.
        """
        self.savingMessage.close()

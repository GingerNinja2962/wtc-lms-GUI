import PySimpleGUI as sg

import core


class assignmentGrade:
    """
    A class to be used to grade assignments from wtc-lms.

    Attributes
    ----------
        mainWindow : object
            The PySimpleGUI window object that has been opened.

    Methods
    -------
        lmsGradeAssignment()
            Start a subprocess calling lms to grade an assignment.
        openMessage()
            Open a saving data message that will remain open until
            closed.
        closeMessage()
            Close the graded assignment message stored in this
            instance of the class.
    """
    def __init__(self, mainWindow):
        """
        The constructor for assignmentGrade.

        Parameters
        ----------
            mainWindow : object
                The PySimpleGUI window object that has been opened.
        """
        self.mainWindow = mainWindow
        self.openMessage()
        self.lmsGradeAssignment()
        self.closeMessage()


    def lmsGradeAssignment(self):
        """
        Start a subprocess calling lms to grade an assignment.
        """
        assignmentGradingProcess = core.lmsCall(["wtc-lms","grade",
            self.mainWindow.layout.listboxs.assignmentsDict[
            self.mainWindow.values["-PROBLEM-"][0]]])
        (assignmentGradingData, err) = core.systemCallComms(
            assignmentGradingProcess)


    def openMessage(self):
        """
        Open a graded assignment message that will remain open until
        closed.
        """
        self.gradingMessage = sg.Window(f"graded your assignment",
            [
                [ sg.Text(
                    f"\nYour assignment has been submitted for grading.")],
                [ sg.Text(f"To check your grade check out the 'History',") ],
                [ sg.Text("for this assignment.") ],
                [ sg.Button("Close")]
            ], element_justification='c', size=(400, 110), location=(500, 300)
        ).finalize()


    def closeMessage(self):
        """
        Close the graded assignment message stored in this instance of
        the class.
        """
        self.event, self.values = self.gradingMessage.read()

        if self.event in (sg.WIN_CLOSED, "Exit", "Close"):
            self.gradingMessage.close()

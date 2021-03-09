import PySimpleGUI as sg

import core


class assignmentSave():
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.openMessage()
        self.lmsSaveAssignment()
        self.closeMessage()


    def lmsSaveAssignment(self):
        assignmentSaveProcess = core.lmsCall(["wtc-lms","save",
            self.mainWindow.layout.listboxs.assignmentsDict[self.mainWindow.values["-PROBLEM-"][0]]])
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
        Close the saving data message stored in this instance of the class.
        """
        self.savingMessage.close()

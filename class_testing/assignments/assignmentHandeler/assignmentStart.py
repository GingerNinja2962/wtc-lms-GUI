import PySimpleGUI as sg

import core


class assignmentStart():
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.openMessage()
        self.lmsStartAssignment()
        self.closeMessage()


    def lmsStartAssignment(self):
        assignmentStartProcess = core.lmsCall(["wtc-lms","start",
            self.mainWindow.layout.listboxs.assignmentsDict[self.mainWindow.values["-PROBLEM-"][0]]])
        (assignmentStartData, err) = core.systemCallComms(assignmentStartProcess)
        sg.popup(f"{assignmentStartData}", title="lms GUI assignments",
            auto_close=True, auto_close_duration=5, location=(500, 300))


    def openMessage(self):
        """
        Open a downloading data message that will remain open until closed.
        """
        self.downloadingMessage = sg.Window(f"downloading your assignment",
            [
                [ sg.Text(f"\nYour assignment is being downloaded.") ],
                [ sg.Text(f"downloading your assignment may take a minute or two") ],
                [ sg.Text("depending on your internet connection.") ],
            ], element_justification='c', size=(400, 110), location=(500, 300)
        ).finalize()


    def closeMessage(self):
        """
        Close the downloading data message stored in this instance of the class.
        """
        self.downloadingMessage.close()

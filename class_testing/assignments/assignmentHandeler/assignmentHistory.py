import PySimpleGUI as sg

from classTemplates import baseWindowClass

import core


class assignmentHistory(baseWindowClass):
    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow
        self.location = (55, 150)
        self.getLayout()
        self.run()


    def getLayout(self):
        self.layout = [
            [ sg.Text(self.getHistoryData(), font="monospace 10") ],
            [sg.Button("Close")]
        ]


    def getHistoryData(self):
        assignmentHistoryProcess = core.lmsCall(["wtc-lms","history",
            self.mainWindow.layout.listboxs.assignmentsDict[self.mainWindow.values["-PROBLEM-"][0]]])
        (assignmentHistoryData, err) = core.systemCallComms(assignmentHistoryProcess)
        return assignmentHistoryData

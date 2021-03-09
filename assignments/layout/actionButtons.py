from custom_inherit import DocInheritMeta

import PySimpleGUI as sg


class actionButtonsClass(metaclass=DocInheritMeta(style="numpy_with_merge", include_special_methods=True)):
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.stateList = [True]*4
        self.actionButtonsFrame()


    def actionButtonsUpdate(self):
        """
        set the assignment buttons to the required state depending
            on the problem state
        """
        problemState = self.mainWindow.layout.listboxs.problemsState[self.mainWindow.values['-PROBLEM-'][0]]
        if problemState == "Not Started":
            self.stateList = [False]+[True]*3
        elif problemState == "In Progress":
            self.stateList = [False]*4
        else:
            self.stateList = [False]*4

        self.mainWindow.window['-START-'].Update(disabled=self.stateList[0])
        self.mainWindow.window['-SAVE-'].Update(disabled=self.stateList[1])
        self.mainWindow.window['-GRADE-'].Update(disabled=self.stateList[2])
        self.mainWindow.window['-HISTORY-'].Update(disabled=self.stateList[3])


    def resetButtons(self):
        """
        reset the assignment buttons to an inactive state
        """
        self.mainWindow.window['-START-'].Update(disabled=True)
        self.mainWindow.window['-SAVE-'].Update(disabled=True)
        self.mainWindow.window['-GRADE-'].Update(disabled=True)
        self.mainWindow.window['-HISTORY-'].Update(disabled=True)


    def actionButtonsFrame(self):
        """
        returns a assignment button frame with 4 wtc-lms assignment options
        """
        self.buttonsFrame = [
            [sg.Button('Start', key='-START-', disabled=self.stateList[0],
                tooltip="Start the assignment and clone into the assignment folder",
                size=(6,1), pad=(1,1))],
            [sg.Button('Save', key='-SAVE-', disabled=self.stateList[0],
                tooltip="Save your work to the wtc-lms cloud server",
                size=(6,1), pad=(1,1))],
            [sg.Button('Grade', key='-GRADE-', disabled=self.stateList[0],
                tooltip="Submit your work for grading",
                size=(6,1), pad=(1,1))],
            [sg.Button('History', key='-HISTORY-', disabled=self.stateList[0],
                tooltip="View the History of your graded assignment",
                size=(6,1), pad=(1,1))]
        ]

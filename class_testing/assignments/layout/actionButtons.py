from custom_inherit import DocInheritMeta

import PySimpleGUI as sg


class actionButtonsClass(metaclass=DocInheritMeta(style="numpy_with_merge", include_special_methods=True)):
    def __init__(self):
        super().__init__()
        self.assignmentState = None
        self.stateList = [True]*4


    def assignment_buttons_update(self, problemName):
        """
        set the assignment buttons to the required state depending
            on the problem state

        :param problem_name: this is the name of the choosen assignment
        """
        if self.token.tokenCheck("assignment"):
            self.problemsData.populateProblems()

        self.assignmentState = (problemName.replace('[', ']')
                .split("\n")[1])

        if self.assignmentState == "Not Started":
            self.stateList = [False]+[True]*3
        elif self.assignmentState == "Started":
            self.stateList = [False]*3+[True]
        elif self.assignmentState == "In Progress":
            self.stateList = [False]+[True]*2+[False]
        else: # TODO find out what this is for
            self.stateList = [False]*4

        self.window['-START-'].Update(disabled=self.stateList[0])
        self.window['-SAVE-'].Update(disabled=self.stateList[1])
        self.window['-GRADE-'].Update(disabled=self.stateList[2])
        self.window['-HISTORY-'].Update(disabled=self.stateList[3])


    def reset_buttons(self):
        """
        reset the assignment buttons to an inactive state
        """
        self.window['-START-'].Update(disabled=True)
        self.window['-SAVE-'].Update(disabled=True)
        self.window['-GRADE-'].Update(disabled=True)
        self.window['-HISTORY-'].Update(disabled=True)


    def assignmentButtonsFrame(self):
        """
        a small function that returns a assignment button frame with 4 wtc-lms assignment options

        :return assignment_frame: a frame containing the options for wtc-lms assignments
        """
        return [
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

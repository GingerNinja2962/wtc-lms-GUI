import PySimpleGUI as sg

from classTemplates.windowTemplate import baseWindowClass
from classTemplates.inDevelopmentPopup import inDevelopmentPopup
from assignments.layout import assignmentsLayoutClass

import settings
import assignments
import core


class assignmentsMenuClass(baseWindowClass):
    """
    A class to create a assignments menu window.
    """
    def __init__(self):
        super().__init__()
        self.token = core.tokensClass()
        self.layout = assignmentsLayoutClass(self)
        self.title = "LMS Assignments GUI"
        self.location = (225, 200)


    def run(self):
        self.window = sg.Window(self.title, self.layout.layout, 
                element_justification=self.elementJustification,
                location=self.location).finalize()

        if self.layout.listboxs.modulesList == []:
            self.window["-MODULE-"].Update(disabled=True)

        while self.running:
            nextAction = self.read()
        return nextAction


    def read(self):
        self.event, self.values = self.window.read(timeout=5000)

        if not self.token.tokenCheck("Assignment") or \
                self.values["-SETTINGS-MENU-"] == "Update Assignments":
            self.layout.listboxs.populateAssignments()
            self.layout.listboxs.resetListboxs()

        if self.event in (sg.WIN_CLOSED, "Exit"):
            self.close()
            return "Closed"

        elif self.values["-SETTINGS-MENU-"] == "General Settings":
            settings.generalSettings()

        elif self.values["-SETTINGS-MENU-"] == "Change Theme":
            settings.themeMenuClass().run()

        elif self.values["-NAVIGATE-MENU-"] == "    Main Menu":
            self.close()
            return "mainMenu"

        elif self.values["-NAVIGATE-MENU-"] == "    Reviews Menu":
            self.close()
            return "reviews"

        elif self.event == "-MODULE-":
            self.layout.listboxs.topicsListbox()
            self.layout.actionButtons.resetButtons()

        elif self.event == "-TOPIC-":
            self.layout.listboxs.problemsListbox()
            self.layout.actionButtons.resetButtons()

        elif self.event == "-PROBLEM-":
            self.layout.actionButtons.actionButtonsUpdate()

        elif self.event == '-START-':
            assignments.assignmentHandeler.assignmentStart(self)
            self.layout.listboxs.populateAssignments() # TODO improve to only update this problem

        elif self.event == '-SAVE-':
            assignments.assignmentHandeler.assignmentSave(self)

        elif self.event == '-GRADE-':
            assignments.assignmentHandeler.assignmentGrade(self)

        elif self.event == '-HISTORY-':
            assignments.assignmentHandeler.assignmentHistory(self)

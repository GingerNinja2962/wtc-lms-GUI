import PySimpleGUI as sg

import classTemplates
from assignments import layout

import settings
import assignments
import core


class assignmentsMenuClass(classTemplates.baseWindowClass, layout.assignmentsLayoutClass):
    """
    A class to create a assignments menu window.
    """
    def __init__(self):
        super().__init__()
        self.token = core.tokensClass()
        self.title = "LMS Assignments GUI"
        super().setupLayout()


    def run(self):
        self.window = sg.Window(self.title, self.layout, 
                element_justification=self.elementJustification,
                location=self.location).finalize()

        if self.modulesList == []: # TODO check for bugs
            self.window["-MODULE-"].Update(disabled=True)

        while self.running:
            self.nextAction = self.read()
        return self.nextAction


    def read(self):
        self.event, self.values = self.window.read(timeout=5000)

        if not self.token.tokenCheck("Assignment"):
            self.populateProblems()

        if self.event in (sg.WIN_CLOSED, "Exit"):
            self.close()
            return "Closed"

        elif self.values["-SETTINGS-MENU-"] == "General Settings":
            settings.generalSettings()

        elif self.values["-SETTINGS-MENU-"] == "Change Theme":
            settings.themeMenuClass().run()

        elif self.values["-SETTINGS-MENU-"] == "Update Assignments":
            self.populateProblems()
            self.resetListboxs()

        elif self.values["-NAVIGATE-MENU-"] == "    Main Menu":
            self.close()
            return "mainMenu"

        elif self.values["-NAVIGATE-MENU-"] == "    Reviews Menu":
            self.close()
            return "mainMenu" # TODO change to "reviews" onec reviews is up and running

        elif self.event == "-MODULE-":
            self.topicsListbox()
            self.resetButtons()

        elif self.event == "-TOPIC-":
            self.problemsListbox()
            self.resetButtons()

        elif self.event == "-PROBLEM-":
            self.actionButtonsUpdate()

        elif self.event == '-START-':
            classTemplates.inDevelopmentPopup()
        elif self.event == '-SAVE-':
            classTemplates.inDevelopmentPopup()
        elif self.event == '-GRADE-':
            classTemplates.inDevelopmentPopup()
        elif self.event == '-HISTORY-':
            classTemplates.inDevelopmentPopup()

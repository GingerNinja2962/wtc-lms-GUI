#!/usr/bin/python3
import PySimpleGUI as sg
from custom_inherit import doc_inherit

from classTemplates.windowTemplate import baseWindowClass

import mainMenu
import settings


class mainMenuClass(baseWindowClass):
    """
    A class to create a main menu window.
    """
    def __init__(self):
        super().__init__()
        self.title = "wtc-lms GUI menu"
        self.layout = mainMenu.layout()


    def read(self):
        self.event, self.values = self.window.read()

        if self.event in (sg.WIN_CLOSED, "Exit"):
            self.close()
            return "Closed"

        elif self.values["-SETTINGS-MENU-"] == "General Settings":
            settings.generalSettings()

        elif self.values["-SETTINGS-MENU-"] == "Change Theme":
            settings.themeMenuClass().run()

        # TODO finish setting up clas swapover
        elif self.event == "Assignments":
            self.close()
            return "assignments"            

        # TODO finish setting up clas swapover
        # elif self.event == "Reviews":
        #     self.close()
        #     self.running = reviews.review_problem()


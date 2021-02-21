#!/usr/bin/python3
import PySimpleGUI as sg
from custom_inherit import doc_inherit

import baseClasses
import mainMenu
import settings


class mainMenuClass(baseClasses.baseWindowClass):
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

        elif self.values["-SETTINGS-MENU-"] == "General Settings":
            settings.generalSettings()

        elif self.values["-SETTINGS-MENU-"] == "Change Theme":
            themeMenu = settings.themeMenuClass().run()
            del themeMenu

        # TODO finish setting up clas swapover
        # elif self.event == "Assignments":
        #     self.close()
        #     self.running = assignments.assignments_main_menu()

        # TODO finish setting up clas swapover
        # elif self.event == "Reviews":
        #     self.close()
        #     self.running = reviews.review_problem()


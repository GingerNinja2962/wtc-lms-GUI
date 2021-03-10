import PySimpleGUI as sg
from custom_inherit import doc_inherit

from classTemplates.windowTemplate import baseWindowClass

from mainMenu import layout
import settings


class mainMenuClass(baseWindowClass):
    """
    A class to create a main menu window.

    Parameters
    ----------
        baseWindowClass : class
            The base window class to inherit from when making a window
            class.
    """
    def __init__(self):
        """
        The constructor for assignmentsMenuClass.
        """
        super().__init__()
        self.title = "wtc-lms GUI menu"
        self.layout = layout()


    def read(self):
        self.event, self.values = self.window.read()

        if self.event in (sg.WIN_CLOSED, "Exit"):
            self.close()
            return "Closed"

        elif self.values["-SETTINGS-MENU-"] == "General Settings":
            settings.generalSettings()

        elif self.values["-SETTINGS-MENU-"] == "Change Theme":
            settings.themeMenuClass().run()

        elif self.event == "Assignments":
            self.close()
            return "assignments"

        elif self.event == "Reviews":
            self.close()
            return "reviews"

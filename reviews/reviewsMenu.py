import PySimpleGUI as sg

from os import remove

from classTemplates.windowTemplate import baseWindowClass
from classTemplates.inDevelopmentPopup import inDevelopmentPopup

from core import tokensClass
from core.lmsLogin import manageLogin

import settings
import assignments
from reviews import layout, reviewHandeler, problemSelection, validUUID


class reviewsMenuClass(baseWindowClass):
    """
    A class to create a reviews menu window.

    Attributes
    ----------
        status : boollean
            The return value from the checkModuleData function. 

    Methods
    -------
        checkChanges()
            Checks if the window has gotten any changes in review
            filters.
    """
    def __init__(self):
        """
        The constructor for reviewsMenuClass.

        Attributes
        ----------
            status : boollean
                The return value from the checkModuleData function. 
        """
        super().__init__()
        self.status = True
        self.token = tokensClass()
        self.layout = layout.reviewsLayoutClass(self)
        self.title = "LMS Reviews GUI"
        self.location = (50, 125)


    def run(self):
        if not self.status:
            sg.Window(self.title, [ [ sg.Output(key="-OUTPUT-", visible=False) # Keep this as it clears the output never used bug
            ] ] ).finalize().close() # Overrides the original Output panal in layout.layout and thus forces the del of that item upon closing.
            remove(f"{self.layout.assignmentData.saveDataPath}/tokens/loginF")
            return "mainMenu"

        self.window = sg.Window(self.title, self.layout.layout,
                element_justification=self.elementJustification,
                location=self.location).finalize()

        self.oldResults = [False]* 7
        self.activeButtons = [False]* 4

        while self.running:
            nextAction = self.read()
        return nextAction


    def read(self):
        self.event, self.values = self.window.read(timeout=750)

        self.checkChanges()

        self.oldActiveButtons = self.activeButtons
        self.activeButtons = validUUID(self)

        if not self.token.tokenCheck("Review") or self.values[
                "-SETTINGS-MENU-"] == "Update Reviews":
            self.layout.reviewsData.populateReviews()
            self.layout.reviewsData.getReviewData()
            self.window['-OUTPUT-'].update('')
            problemSelection(self)
            self.layout.frames.updateCounterFrame()

        if self.values["-SETTINGS-MENU-"] == "General Settings":
            settings.generalSettings()

        elif self.values["-SETTINGS-MENU-"] == "Change Theme":
            settings.themeMenu()

        elif self.values["-NAVIGATE-MENU-"] == "   Main Menu":
            self.close()
            return "mainMenu"

        elif self.values["-NAVIGATE-MENU-"] == "   Assignments Menu":
            self.close()
            return "assignments"

        elif self.oldActiveButtons != self.activeButtons:
            self.window['Review details'].Update(disabled=self.activeButtons[0])
            self.window['Accept'].Update(disabled=self.activeButtons[1])
            self.window['Comment'].Update(disabled=self.activeButtons[2])
            self.window['Grade'].Update(disabled=self.activeButtons[3])

        elif self.event == "Review details":
            reviewHandeler.reviewDetailsPopup(self.values['-INPUT-'])

        elif self.event == "Accept":
            reviewHandeler.acceptReview(self.values['-INPUT-'])
            self.layout.reviewsData.populateReviews()
            self.layout.frames.updateCounterFrame()

        elif self.event == "Comment":
            reviewHandeler.commentHandeler(self.values['-INPUT-'])

        elif self.event == "Grade":
            reviewHandeler.gradeReview(self.values['-INPUT-'])
            self.layout.reviewsData.populateReviews()
            self.layout.frames.updateCounterFrame()

        if self.oldResults[0] \
                or self.values["-SETTINGS-MENU-"] == "Update Reviews" \
                or self.event == "Review details" or self.event == "Accept" \
                or self.event == "Comment" or self.event == "Grade":
            self.window['-OUTPUT-'].update('')
            problemSelection(self)

        elif self.event in (sg.WIN_CLOSED, "Exit"):
            self.close()
            return "Closed"


    def checkChanges(self):
        """
        Check if the windows data has changed.
        """
        results = [
        self.values[1],
        self.values[f"-{self.values[1]}-"],
        self.values["-TOGGLE-ALL-"],
        self.values["-INVITED-"],
        self.values["-ASSIGNED-"],
        self.values["-GRADED-"],
        self.values["-BLOCKED-"] ]

        if results == self.oldResults[1::]:
            self.oldResults = [False] + results

        elif (self.values[f"-{self.values[1]}-"] == [] and \
                self.values["-TOGGLE-ALL-"] == False and \
                results[0] != self.oldResults[1]):
            self.window['-OUTPUT-'].update('')
            self.oldResults = [False] + results

        else:
            self.oldResults = [True] + results

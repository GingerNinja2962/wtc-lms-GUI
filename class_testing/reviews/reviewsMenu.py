import PySimpleGUI as sg

from classTemplates.windowTemplate import baseWindowClass
from classTemplates.inDevelopmentPopup import inDevelopmentPopup

import settings
import assignments
import reviews
import core


class reviewsMenuClass(baseWindowClass):
    """
    A class to create a reviews menu window.
    """
    def __init__(self):
        super().__init__()
        self.token = core.tokensClass()
        self.layout = reviews.layout.reviewsLayoutClass(self)
        self.title = "LMS Reviews GUI"
        self.location = (50, 125)


                   # TODO i don't belive that the base template will work in this case
                   # TODO as the oldResaults and activeButtons vars need to be instanciated
    def run(self): # TODO check if needed or base template can be used
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
        self.activeButtons = reviews.validUUID(self)

        if not self.token.tokenCheck("Review") or self.values["-SETTINGS-MENU-"] == "Update Reviews":
            self.layout.reviewsData.populateReviews()
            self.layout.reviewsData.getReviewData()
            self.window['-OUTPUT-'].update('')
            reviews.problemSelection(self)
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
            reviews.review_handeler.review_details_popup(self.values['-INPUT-'])

        elif self.event == "Accept":
            reviews.review_handeler.accept_review(self.values['-INPUT-'], window)
            core.populate_save_data.populate_save_data("reviews")
            reviews.layout.update_counter_frame(window)

        elif self.event == "Comment":
            reviews.review_handeler.comment_handeler(self.values['-INPUT-'], window)

        elif self.event == "Grade":
            reviews.review_handeler.grade_review(self.values['-INPUT-'], window)
            core.populate_save_data.populate_save_data("reviews")
            reviews.layout.update_counter_frame(window)

        if self.oldResults[0] or self.values["-SETTINGS-MENU-"] == "Update Reviews" \
                or self.event == "Review details" or self.event == "Accept" \
                or self.event == "Comment" or self.event == "Grade":
            pass
            self.window['-OUTPUT-'].update('')
            reviews.problemSelection(self)

        elif self.event in (sg.WIN_CLOSED, "Exit"):
            self.close()
            return "Closed"


    def checkChanges(self):
        """
        checks if the window has gotten any changes in review filters
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
            # print(f"pass 1")
            self.oldResults = [False] + results

        elif (self.values[f"-{self.values[1]}-"] == [] and \
                self.values["-TOGGLE-ALL-"] == False and \
                results[0] != self.oldResults[1]):
            # print("pass 2")
            self.window['-OUTPUT-'].update('')
            self.oldResults = [False] + results

        else:
            # print("pass 3")
            self.oldResults = [True] + results

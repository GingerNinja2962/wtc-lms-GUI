import PySimpleGUI as sg

from classTemplates.windowTemplate import baseWindowClass
from classTemplates.inDevelopmentPopup import inDevelopmentPopup

import settings
import assignments
import core


class reviewsMenuClass(baseWindowClass):
    """
    A class to create a reviews menu window.
    """
    def __init__(self):
        super().__init__()
        self.token = core.tokensClass()
        self.layout = reviewsLayoutClass(self)
        self.title = "LMS Reviews GUI"
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
        self.event, self.values = self.window.read(timeout=750)

        old_results = check_changes(event, values, old_results, window)

        old_active_buttons = active_buttons
        active_buttons = reviews.valid_uuid(values['-INPUT-'])

        if core.token_check("review") or values["-SETTINGS-MENU-"] == "Update Reviews":
            if values["-SETTINGS-MENU-"] == "Update Reviews":
                core.populate_save_data.populate_save_data("reviews")
            else:
                core.populate_save_data.populate_reviews()
            window['-OUTPUT-'].update('')
            reviews.problem_selection(values)
            reviews.layout.update_counter_frame(window)

        if values["-SETTINGS-MENU-"] == "General Settings":
            settings.general_settings()

        elif values["-SETTINGS-MENU-"] == "Change Theme":
            settings.theme_menu()

        elif values["-NAVIGATE-MENU-"] == "   Main Menu":
            window.close()
            return True

        elif values["-NAVIGATE-MENU-"] == "   Assignments Menu":
            window.close()
            return assignments.assignments_main_menu()

        elif old_active_buttons != active_buttons:
            window['Review details'].Update(disabled=active_buttons[0])
            window['Accept'].Update(disabled=active_buttons[1])
            window['Comment'].Update(disabled=active_buttons[2])
            window['Grade'].Update(disabled=active_buttons[3])

        elif event == "Review details":
            reviews.review_handeler.review_details_popup(values['-INPUT-'])

        elif event == "Accept":
            reviews.review_handeler.accept_review(values['-INPUT-'], window)
            core.populate_save_data.populate_save_data("reviews")
            reviews.layout.update_counter_frame(window)

        elif event == "Comment":
            reviews.review_handeler.comment_handeler(values['-INPUT-'], window)

        elif event == "Grade":
            reviews.review_handeler.grade_review(values['-INPUT-'], window)
            core.populate_save_data.populate_save_data("reviews")
            reviews.layout.update_counter_frame(window)

        if old_results[0] or values["-SETTINGS-MENU-"] == "Update Reviews" \
                or event == "Review details" or event == "Accept" \
                or event == "Comment" or event == "Grade":
            window['-OUTPUT-'].update('')
            reviews.problem_selection(values)

        elif event in (sg.WIN_CLOSED, "Exit"):
            window.close()
            return False


def check_changes(event, values, old_results, window):
    """
    checks if the window has gotten any changes in review filters

    :param event: this is the current even that has run
    :param values: this is the values from the open window
    :param old_resaults: this is the old check_changes resaults
    :param window: this is the sg object containing all the elements for the window
    :return boollean: True if there are changes False if not
    """
    results = [
    values["-PROBLEM-1-"],
    values["-PROBLEM-2-"],
    values["-TOGGLE-ALL-"],
    values["-INVITED-"],
    values["-ASSIGNED-"],
    values["-GRADED-"],
    values["-BLOCKED-"] ]

    if results == old_results[1::]:
        return ([False] + results)

    elif (values["-PROBLEM-1-"] == [] and values["-PROBLEM-2-"] == []\
                and values["-TOGGLE-ALL-"] == False):
        window['-OUTPUT-'].update('')
        return ([False] + results)

    else:
        if results[2::] == old_results[3::]:
            if values["-PROBLEM-1-"] == old_results[1] and values["-PROBLEM-2-"] != []:
                window['-PROBLEM-1-'].set_value([])
            elif values["-PROBLEM-2-"] == old_results[2] and values["-PROBLEM-1-"] != []:
                window['-PROBLEM-2-'].set_value([])
        return ([True] + results)

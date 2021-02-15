import PySimpleGUI as sg

import reviews
import settings


def review_problem():
    """
    Function to get all assigned reviews
    """
    Layout = reviews.layout.problem_selection_layout()

    window = sg.Window("LMS Reviews Gui", Layout, element_justification='c', location=(100, 100))
    old_results = [False]*7

    while 1:

        event, values = window.read(timeout=500)
        old_results = check_changes(event, values, old_results, window)

        if reviews.token_handeler.time_check():
            reviews.token_handeler.data_download()

        if event == sg.WIN_CLOSED or event == "Exit":
            window.close()
            return False

        if event == "Settings":
            settings.general_settings()

        elif event == '⟳':
            active_buttons = reviews.valid_uuid(values['-INPUT-'])
            window['Review details'].Update(disabled=active_buttons[0])
            window['Accept'].Update(disabled=active_buttons[1])
            window['Comment'].Update(disabled=active_buttons[2])
            window['Grade'].Update(disabled=active_buttons[3])

        elif event == "Update review data":
            reviews.token_handeler.data_download()
            reviews.token_handeler.force_time_update()
            reviews.layout.update_counter_frame(window)

        elif old_results[0]:
            window.FindElement('-OUTPUT-').update('')
            reviews.problem_selection(values)

        elif event == "Main Menu":
            window.close()
            return True

        elif event == "Review details":
            reviews.review_handeler.review_details(values['-INPUT-'], window)

        elif event == "Accept":
            reviews.review_handeler.accept_review(values['-INPUT-'], window)

        elif event == "Comment":
            reviews.review_handeler.comment_handeler(values['-INPUT-'], window)

        elif event == "Grade":
            reviews.review_handeler.grade_review(values['-INPUT-'], window)


def check_changes(event, values, old_results, window):
    """
    a small function that checks if the window has gotten any changes

    :param event: this is the current even that has run
    :param values: this is the values from the open window
    :param old_resaults: this is the old check_changes resaults
    :param window: this is the sg object containing all the elements for the window
    :return boollean: True if there are changes False if not
    """
    if values["-PROBLEM-"] != []: ch_1 = True
    else: ch_1 = False
    ch_2 = values["-TOGGLE-ALL-"]
    ch_3 = values["-INVITED-"]
    ch_4 = values["-ASSIGNED-"]
    ch_5 = values["-GRADED-"]
    ch_6 = values["-BLOCKED-"]

    results = [ch_1, ch_2, ch_3, ch_4, ch_5, ch_6]

    if event == "-PROBLEM-":
        # print("test_0 passed - problem change")
        return ([True] + results)

    if results == old_results[1::]:
        # print("test_1 failed - results same")
        return ([False] + results)

    elif (ch_1 == False and ch_2 == False):
        # print("test_2 failed - no problem selected")
        window.FindElement('-OUTPUT-').update('')
        return ([False] + results)

    else:
        # print("test_3 Pass - filters changed")
        return ([True] + results)

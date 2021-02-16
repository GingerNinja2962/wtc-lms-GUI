import os

import core


def assignment_buttons_update(problem_name, window):
    """
    reset the assignment buttons to an inactive state

    :param problem_name: this is the name of the choosen assignment
    :param window: the sg object containing the elements to be updated
    """
    if core.token_check("assignment"):
        core.populate_save_data.populate_problems()

    assignment_state = (problem_name.replace('[', '\n')
            .replace(']', '\n').split("\n")[1])

    if assignment_state == "Not Started":
        window['-START-'].Update(disabled=False)
        window['-SAVE-'].Update(disabled=True)
        window['-GRADE-'].Update(disabled=True)
        window['-HISTORY-'].Update(disabled=True)
    elif assignment_state == "Started":
        window['-START-'].Update(disabled=False)
        window['-SAVE-'].Update(disabled=False)
        window['-GRADE-'].Update(disabled=False)
        window['-HISTORY-'].Update(disabled=True)
    elif assignment_state == "In Progress":
        window['-START-'].Update(disabled=False)
        window['-SAVE-'].Update(disabled=True)
        window['-GRADE-'].Update(disabled=True)
        window['-HISTORY-'].Update(disabled=False)
    else: #TODO find what this filter is
        window['-START-'].Update(disabled=True)
        window['-SAVE-'].Update(disabled=True)
        window['-GRADE-'].Update(disabled=True)
        window['-HISTORY-'].Update(disabled=True)


def reset_buttons(window):
    """
    reset the assignment buttons to an inactive state

    :param window: the sg object containing the elements to be updated
    """
    window['-START-'].Update(disabled=True)
    window['-SAVE-'].Update(disabled=True)
    window['-GRADE-'].Update(disabled=True)
    window['-HISTORY-'].Update(disabled=True)

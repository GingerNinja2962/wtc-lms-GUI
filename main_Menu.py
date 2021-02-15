import PySimpleGUI as sg
import settings
import reviews
import self_work


def main_LMS_Menu(running):
    """
    the main menu for the lms system,
    choose weather you are going to do reviews or your own work
    """

    if running:
        #TODO get menu full functionality
        menu_def = [ ['File', ['Settings', 'Exit'] ],
                    ['Login', ['login'] ],
                    ['Help', ['About'] ] ]

        menu_def = [ ['File', ['Settings', 'Exit'] ] ]

        Layout = [ [ sg.Menu(menu_def, tearoff=False, )],
            [ sg.Column([[sg.Button('My Work')]]),
            sg.VSeperator(),
            sg.Column([[sg.Button('Reviews')]]) ] ]

        window = sg.Window("Lms Gui", Layout, element_justification='c', location=(500, 300))

    while running:
        event, _ = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            window.close()
            running = False

        if event == "Settings":
            settings.general_settings()

        if event == "My Work":
            window.close()
            running = self_work.own_work_menu()
            break

        if event == "Reviews":
            reviews_data = reviews.token_handeler.fetch_lms_reviews()
            if reviews_data:
                window.close()
                running = reviews.review_problem()
                break

    if running:
        main_LMS_Menu(running)
    return

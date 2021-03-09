import PySimpleGUI as sg


def general_settings():
    """
    The function that will manage the general settings for the GUI app
    """
    sg.popup("This feature is still in development",
            title="WTC-LMS GUI",
            auto_close=True,
            auto_close_duration=10,
            location=(500, 300))

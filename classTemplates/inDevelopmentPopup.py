import PySimpleGUI as sg


def inDevelopmentPopup():
    """
    Generate a popup that auto-closes after 10 seconds, displaying
    the in development message.
    """
    sg.popup("This feature is still in development",
        title="WTC-LMS GUI",
        auto_close=True,
        auto_close_duration=10,
        location=(500, 300))

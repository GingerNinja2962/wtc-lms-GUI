import PySimpleGUI as sg

from classTemplates.windowTemplate import baseWindowClass


class themeMenuClass(baseWindowClass):
    """
    Create a window that allows you to choose a theme to change to.
    """
    def __init__(self):
        """
        The constructor for themeMenuClass.
        """
        super().__init__()
        self.layout = [
            [ sg.Text("Look and Feel Browser") ],
            [ sg.Text("Click a look and feel color to see demo window") ],
            [ sg.Listbox(values=sg.theme_list(),
                size=(20, 20), key='-THEME-LIST-', enable_events=True) ],
            [ sg.Button("Exit") ] ]
        self.title = "Theme Menu"


    def read(self):
        self.event, self.values = self.window.read()

        if self.event in (sg.WIN_CLOSED, "Exit"):
            return self.close()

        sg.theme(self.values['-THEME-LIST-'][0])

        event = sg.popup(
            f"This is {self.values['-THEME-LIST-'][0]}",
            "Would you like to set this theme?", custom_text=("Yes", "No"),
            location=self.location)

        if event == "Yes":
            return self.close()

        elif event in (sg.WIN_CLOSED, "No"):
            sg.theme(self.defaultTheme)
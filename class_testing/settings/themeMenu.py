import PySimpleGUI as sg

import classTemplates


class themeMenuClass(classTemplates.baseWindowClass):
    """
    Create a window that allows you to chage the theme
    """
    def __init__(self):
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
            "Would you like to set this theme?", custom_text=("Yes", "No"))

        if event == "Yes":
            return self.close()

        elif event in (sg.WIN_CLOSED, "No"):
            sg.theme(self.defaultTheme)
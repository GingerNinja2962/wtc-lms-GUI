import PySimpleGUI as sg

def theme_menu():
    """
    open a window to change the theme
    """
    layout = [[sg.Text('Look and Feel Browser')],
            [sg.Text('Click a look and feel color to see demo window')],
            [sg.Listbox(values=sg.theme_list(),
                        size=(20, 20), key='-LIST-', enable_events=True)],
            [sg.Button('Exit')]]

    window = sg.Window('Look and Feel Browser', layout)

    while True:  # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        sg.theme(values['-LIST-'][0])
        sg.popup_get_text('This is {}'.format(values['-LIST-'][0]), default_text=values['-LIST-'][0])

    window.close()
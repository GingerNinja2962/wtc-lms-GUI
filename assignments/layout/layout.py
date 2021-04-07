import PySimpleGUI as sg

from core import dataHandelerClass

from assignments.layout import actionButtonsClass, assignmentsListboxClass


class assignmentsLayoutClass(dataHandelerClass):
    """
    A class to use for generating the layout for the assignments
    window.

    Parameters
    ----------
        dataHandelerClass : class
            The data handeler class to inherit from, that will manage
            the downloading and retriving of saved data.

    Attributes
    ----------
        mainWindow : object
            The PySimpleGUI window object that has been opened.
        actionButtons : object
            The object created from the actionButtonsClass class,
            holding all the data related to the action buttons.
        listboxs : object
            The object created from the assignmentsListboxClass class,
            holding all the data relating to the listboxes.

    Methods
    -------
        assignmentsLayout()
            Generate the problem selection layout for assignments.
    """
    def __init__(self, mainWindow):
        """
        The constructor for assignmentsLayoutClass.

        Parameters
        ----------
            mainWindow : object
                The PySimpleGUI window object that has been opened.
        """
        super().__init__()
        self.mainWindow = mainWindow
        self.actionButtons = actionButtonsClass(self.mainWindow)
        self.listboxs = assignmentsListboxClass(self.mainWindow)
        self.assignmentsLayout()


    def assignmentsLayout(self):
        """
        Generate the problem selection layout for assignments.
        """
        settings_menu_items = ["Unused", ["&General Settings", "&Change Theme", "&Update Assignments"]]
        navigate_menu_items = ["Unused", ["    &Main Menu", "!> & Assignments Menu", "    &Reviews Menu"]]
        help_menu_items = ["Unused", ["&About"]]

        self.layout = [
            [ sg.ButtonMenu("Settings",  settings_menu_items, key="-SETTINGS-MENU-",
                size=(9,1), font="Calibri 9"),
                sg.ButtonMenu("Navigate", navigate_menu_items, key="-NAVIGATE-MENU-",
                size=(9,1), font="Calibri 9"),
                sg.ButtonMenu("Help", help_menu_items, key="-HELP-MENU-",
                size=(8,1), font="Calibri 9"),
                sg.Text("", pad=(305,0)),
                sg.Button("Exit", pad=(0,0))
            ],
            [ sg.HSeparator() ],
            [ sg.Column(
                [ [ sg.Text("Modules", font="Calibri 9") ],
                    [ sg.Column(
                    [ [ sg.Listbox(
                        values=self.listboxs.modulesList,
                        size=(30,20), key="-MODULE-", enable_events=True) ] ]
                ), ] ], element_justification='c' ),
            sg.Column(
                [ [ sg.Text("Topics", font="Calibri 9") ],
                [ sg.Column(
                    [ [ sg.Listbox(values=[],
                        size=(35,20), key="-TOPIC-",enable_events=True,
                        disabled=True) ] ] ),
                ] ], element_justification='c' ),
            sg.Column(
                [ [ sg.Text("Assignments", font="Calibri 9") ],
                    [ sg.Column(
                        [ [ sg.Listbox(values=[],
                            size=(40,20), key="-PROBLEM-",enable_events=True,
                            disabled=True) ] ]
                    ) ]
                ], element_justification='c' ),
            sg.Text("", pad=(10,0)),
            sg.Column(
                [ [ sg.Text("Actions", font="Calibri 9") ],
                    [ sg.Frame(title="Operations",
                        layout=self.actionButtons.buttonsFrame,
                        pad=(0,82)) ],
                ], element_justification='c')
            ]
        ]

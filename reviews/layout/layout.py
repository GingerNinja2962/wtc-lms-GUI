import PySimpleGUI as sg

from core import dataHandelerClass

import reviews
import core


class reviewsLayoutClass(dataHandelerClass):
    """
    A class to generate the reviews menu layout.

    Parameters
    ----------
        dataHandelerClass : class
            The data handeler class to inherit from, that will manage
            the downloading and retriving of saved data for reviews.

    Attributes
    ----------
        mainWindow : object
            The PySimpleGUI window object that has been opened.
        assignmentData : object
            The assignemts data class object dedicated to managing
            the population of the save data for assignments from
            wtc-lms.
        reviewsData : object
            The review data class object dedicated to managing the
            population of the saved reviews data from wtc-lms.
        tabGroup : object
            The tab group class object dediacted to creating and
            managing a tab group layout for the reviews window.
        frames : object
            The filter frame class object that holds the filter frame
            layout for the reviews window.
        layout : list
            The layout of the window.

    Methods
    -------
        reviewsLayout()
            Set up the basic problem selection layout for reviews.
    """
    def __init__(self, mainWindow):
        """
        The constructor for reviewsLayoutClass.

        Parameters
        ----------
            mainWindow : object
                The PySimpleGUI window object that has been opened.
        """
        super().__init__()
        self.mainWindow = mainWindow
        self.assignmentData = core.populateSaveData.populateAssignmentsClass()
        self.reviewsData = core.populateSaveData.populateReviewsClass()

        if not core.fileCheck(self.assignmentData.modulesDataPath):
            self.assignmentData.populateAssignments()

        self.tabGroup = reviews.layout.tabGroupClass(self)
        self.frames = reviews.layout.framesClass(self, self.mainWindow)
        self.layout = [[]]
        self.reviewsLayout()


    def reviewsLayout(self):
        """
        Set up the basic problem selection layout for reviews.

        Returns
        -------
            layout : list
                The list of lists containing PySimpleGUI objects to be
                placed in the window.
        """
        settingsMenuItems = ["Unused",
            ["&General Settings", "&Change Theme", "&Update Reviews"]]
        navigateMenuItems = ["Unused",
            ["   &Main Menu", "   &Assignments Menu", "!>& Reviews Menu"]]
        helpMenuItems = ["Unused", ["&About"]]

        self.layout = [
            [ sg.ButtonMenu("Settings",  settingsMenuItems,
                    key="-SETTINGS-MENU-", size=(9,1), item_font="Calibri 9"),
                sg.ButtonMenu("Navigate", navigateMenuItems,
                    key="-NAVIGATE-MENU-", size=(9,1), item_font="Calibri 9"),
                sg.ButtonMenu("Help", helpMenuItems, key="-HELP-MENU-",
                    size=(8,1), item_font="Calibri 9"),
                sg.Text("", pad=(490,0)),
                sg.Button("Exit", pad=(0,0))
            ],
            [ sg.HSeparator() ],
            [ 
            sg.Column(
                [ [ sg.Text("Please select an assignment: ",
                font="Calibri 12") ],
                [
                    sg.Column( self.tabGroup.tabGrouplayout, pad=(5,0) ),
                    sg.Column(
                        [
                            [ sg.Frame("Filters", self.frames.filterFrame,
                                title_color="#FF8C00", title_location="n",
                                font="Calibri 10") ],
                            [ sg.Frame("Review Count", self.frames.CounterFrame,
                                title_color="#FF8C00", title_location="n",
                                element_justification="l", font="Calibri 10") ]
                        ],
                    element_justification="c", pad=(5,0)) ] ], pad=(0,10) ),
            sg.VSeparator(pad=(5,0)),
            sg.Column( [
                [ sg.Output(size=(110, 30), key="-OUTPUT-", pad=(0,20))],
                [ sg.Text("UUID", font="Calibri 10"), sg.InputText( "",
                    tooltip="The UUID you wish to work with", key="-INPUT-"),
                    sg.Button("Review details", disabled=True,
                    tooltip="View the details of the review"),
                    sg.Button("Accept", disabled=True,
                        tooltip="Accepts the review invitation"),
                    sg.Button("Comment", disabled=True,
                        tooltip="Add a comment to the review"),
                    sg.Button("Grade", disabled=True,
                        tooltip="Grade the review") ] ] )
            ]
        ]

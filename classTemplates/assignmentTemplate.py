import PySimpleGUI as sg
from custom_inherit import DocInheritMeta

import os


class baseAssignmentClass(metaclass=DocInheritMeta(style="numpy_with_merge",
include_special_methods=True)):
    """
    A base class to use for running assignment related command which
    includes a downloading message if you are downloading data from
    lms.

    Attributes
    ----------
        downloadingMessage : object
            The PySimpleGUI object that has been opened to display
            a downloading message.

    Methods
    -------
        openMessage()
            Open a downloading data message that will remain open
            until closed.
        closeMessage()
            Close the downloading data message stored in this instance
            of the class.
    """
    def __init__(self):
        """
        The constructor for the baseAssignmentsClass.
        """
        self.downloadingMessage = None


    def openMessage(self, dataType="assignment"):
        """
        Open a downloading data message that will remain open until
        closed.

        Parameters
        ----------
            dataType : str
                This is the type of data being downloaded,
                by default 'assignment'.
        """
        self.downloadingMessage = sg.Window(f"Downloading your {dataType}",
            [
                [ sg.Text(f"\nYour {dataType} is being downloaded.") ],
                [ sg.Text(
                    f"\Downloading your {dataType} may take a minute or two") ],
                [ sg.Text("depending on your internet connection.") ],
            ], element_justification='c', size=(400, 110), location=(500, 300)
        ).finalize()


    def closeMessage(self):
        """
        Close the downloading data message stored in this instance of
        the class.
        """
        if self.downloadingMessage != None:
            self.downloadingMessage.close()
        self.downloadingMessage = None

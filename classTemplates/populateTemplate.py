import PySimpleGUI as sg
from custom_inherit import DocInheritMeta

import os


class basePopulateDataClass(metaclass=DocInheritMeta(style="numpy_with_merge",
include_special_methods=True)):
    """
    A base class to inherit if making a population class.

    Attributes
    ----------
        saveDataPath : str
            The path to the folder holding all saved data.
        loadingMessage : object
            The PySimpleGUI object that has been opened to display a
            loading message.

    Methods
    -------
        openLoadingMessage()
            Open a loading data message that will remain open until
            closed.
        closeLoadingMessage()
            Close the loading data message stored in this instance of
            the class.
    """
    def __init__(self):
        """
        The constructor for basePopulateDataClass.
        """
        self.saveDataPath = f"{os.getcwd()}/.save_data"
        if not os.path.exists(self.saveDataPath): os.mkdir(self.saveDataPath)
        self.loadingMessage = None


    def openLoadingMessage(self, dataType="save"):
        """
        Open a loading data message that will remain open until
        closed.

        Parameters
        ----------
        dataType : str
            This is the type of data being loaded, by default 'save'.
        """
        self.loadingMessage = sg.Window("Updating Your Data",
            [
                [ sg.Text(f"\nYour {dataType} data is being updated.") ],
                [ sg.Text(
                    "\nUpdating the saved data may take a minute or two") ],
                [ sg.Text("depending on your internet connection.") ],
            ], element_justification='c', size=(400, 110), location=(500, 300)
        ).finalize()


    def closeLoadingMessage(self):
        """
        Close the loading data message stored in this instance of the
        class.
        """
        if self.loadingMessage != None:
            self.loadingMessage.close()
        self.loadingMessage = None

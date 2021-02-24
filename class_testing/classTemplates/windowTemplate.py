#!/usr/bin/python3
import PySimpleGUI as sg

from custom_inherit import DocInheritMeta


class baseWindowClass(metaclass=DocInheritMeta(style="numpy_with_merge", include_special_methods=True)):
    """
    A base class to inherit if making a window class.

    Attributes
    ----------
        defaultTheme : str
            The default theme of the window.
        version : float
            The version number of the program.
        versionName : str
            The name of the version.
        title : str
            The title of the window.
        layout : list
            The layout of the window.
        elementJustification : str
            The type of justification to use on all elements on the window.
        location : tuple
            The x and y values to place the top left courner of the window.
        running : bool
            The status of the window (True if running False if closed).
        window : object
            The PySimpleGUI window object.
        event : str
            The event picked up from the read function.
        values : list
            The values of the elements of the open window.
        nextAction : str
            The next window to be opened.

    Methods
    -------
        run()
            Start the window and run the window in a while true loop.
        read()
            Read the user input and map input to functionality of window where possible.
        close()
            Close the window.
    """
    def __init__(self):
        """
        Constructs all the necessary attributes for the standard window objects.

        Parameters
        ----------
            defaultTheme : str
                The default theme of the window.
            version : float
                The version number of the program.
            versionName : str
                The name of the version.
            title : str
                The title of the window.
            layout : list
                The layout of the window.
            elementJustification : str
                The type of justification to use on all elements on the window.
            location : tuple
                The x and y values to place the top left courner of the window.
            running : bool
                The status of the window (True if running False if closed).
            window : object
                The PySimpleGUI window object.
            event : str
                The event picked up from the read function.
            values : list
                The values of the elements of the open window.
            nextAction : str
                The next window to be opened.
        """
        self.defaultTheme = "DarkAmber"
        self.version = 1.4
        self.versionName = "class update"
        self.title = "Lms GUI default window"
        self.layout = [[sg.Text("This is the base window class layout.")]]
        self.elementJustification = 'c'
        self.location=(500, 300)
        self.running = True
        self.window = None
        self.event = ""
        self.values = []
        self.nextAction = None


    def run(self):
        """
        Start the window and run the window in a while true loop.

        Returns
        -------
        nextAction : str
            The next action to be done by the program.
        """
        self.window = sg.Window(self.title, self.layout,
                element_justification=self.elementJustification,
                location=self.location)

        while self.running:
            self.nextAction = self.read()
        return self.nextAction


    def read(self):
        """
        Read the user input and map input to functionality of window where possible.
        """
        self.event, self.values = self.window.read()

        if self.event in (sg.WIN_CLOSED, "Exit", "Close"):
            self.close()


    def close(self):
        """
        Close the window.
        """
        self.running = False
        self.window.close()

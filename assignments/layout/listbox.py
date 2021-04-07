from core import dataHandelerClass


class assignmentsListboxClass(dataHandelerClass):
    """
    A class to use for generating the assignment listboxs
    which will also download the data if needed.

    Parameters
    ----------
        dataHandelerClass : class
            The data handeler class to inherit from, that will manage
            the downloading and retriving of saved data.

    Attributes
    ----------
        mainWindow : object
            The PySimpleGUI window object that has been opened.

    Methods
    -------
        getListboxData()
            Retrieve the saved data or download new data for modules,
            topics, problems and assignments.
        topicsListbox()
            Update the topicsListbox to contain the new loaded topics.
        problemsListbox()
            Update the problemsListbox to contain the new loaded
            problems.
        resetListboxs()
            Re-set the contents of the listboxs to their default
            values.
    """
    def __init__(self, mainWindow):
        """
        The constructor for assignmentsListboxClass.

        Parameters
        ----------
            mainWindow : object
                The PySimpleGUI window object that has been opened.
        """
        super().__init__()
        self.mainWindow = mainWindow
        self.getListboxData()


    def getListboxData(self):
        """
        Retrieve the saved data or download new data for modules,
        topics, problems and assignments.
        """
        if not self.getModules():
            self.mainWindow.status = False
            return
        self.getTopics()
        self.getProblems()
        self.getAssignments()


    def topicsListbox(self):
        """
        Update the topicsListbox to contain the new loaded topics.
        """
        if self.mainWindow.values["-MODULE-"][0] in self.topicsDict.keys():
            topicsData = self.topicsDict[self.mainWindow.values["-MODULE-"][0]]
        else: topicsData = []

        if topicsData != []:
            self.mainWindow.window['-TOPIC-'].Update(disabled=False)
            self.mainWindow.window['-TOPIC-'].Update(values=topicsData)
        else:
            self.mainWindow.window['-TOPIC-'].Update(values=topicsData)
            self.mainWindow.window['-TOPIC-'].Update(disabled=True)

        self.mainWindow.window['-PROBLEM-'].Update(values=[''])
        self.mainWindow.window['-PROBLEM-'].Update(disabled=True)


    def problemsListbox(self):
        """
        Update the problemsListbox to contain the new loaded problems.
        """
        if self.mainWindow.values["-TOPIC-"][0] in self.problemsDict.keys():
            problemsData = self.problemsDict[self.mainWindow.values["-TOPIC-"]
                [0]]
        else: problemsData = []

        if problemsData != []:
            self.mainWindow.window['-PROBLEM-'].Update(disabled=False)
            self.mainWindow.window['-PROBLEM-'].Update(values=problemsData)
        else:
            self.mainWindow.window['-PROBLEM-'].Update(values=problemsData)
            self.mainWindow.window['-PROBLEM-'].Update(disabled=True)


    def resetListboxs(self):
        """
        Re-set the contents of the listboxs to their default values.
        """
        self.getListboxData()
        if self.modulesList == []:
            self.mainWindow.window["-MODULE-"].Update(self.modulesList)
            self.mainWindow.window["-MODULE-"].Update(disabled=True)
        else:
            self.mainWindow.window["-MODULE-"].Update(disabled=False)
            self.mainWindow.window["-MODULE-"].Update(self.modulesList)

        self.mainWindow.window["-TOPIC-"].Update([''])
        self.mainWindow.window['-TOPIC-'].Update(disabled=True)

        self.mainWindow.window["-PROBLEM-"].Update([''])
        self.mainWindow.window['-PROBLEM-'].Update(disabled=True)

import os

import core


class assignmentsListboxClass(core.dataHandelerClass):
    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow
        self.getListboxData()


    def getListboxData(self):
        self.getModules()
        self.getTopics()
        self.getProblems()
        self.getAssignments()


    def topicsListbox(self):
        """
        update the topics_listbox to contain the new loaded topics
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
        update the Problems listbox to contain the new loaded problems
        """
        if self.mainWindow.values["-TOPIC-"][0] in self.problemsDict.keys():
            problemsData = self.problemsDict[self.mainWindow.values["-TOPIC-"][0]]
        else: problemsData = []

        if problemsData != []:
            self.mainWindow.window['-PROBLEM-'].Update(disabled=False)
            self.mainWindow.window['-PROBLEM-'].Update(values=problemsData)
        else:
            self.mainWindow.window['-PROBLEM-'].Update(values=problemsData)
            self.mainWindow.window['-PROBLEM-'].Update(disabled=True)


    def resetListboxs(self):
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

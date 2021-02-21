import os

from core.populateSaveData import populateProblemsClass

import core


class assignmentsListboxClass(populateProblemsClass):
    def __init__(self):
        self.setupListbox()


    def setupListbox(self, token):
        super().__init__()
        self.token = token
        self.modulesListbox()


    def modulesListbox(self):
        if not self.token.tokenCheck("Assignment"):
            self.populateProblems()
        if not self.getModules(): self.populateProblems()


    def topicsListbox(self):
        """
        update the topics_listbox to contain the new loaded topics
        """
        if not self.getTopics(): topicsData = []
        else:
            print(self.topicsDict)
            topicsData = self.topicsDict[self.values["-MODULE-"][0]]
            print(topicsData)

        if topicsData != []:
            self.window['-TOPIC-'].Update(disabled=False)
            self.window['-TOPIC-'].Update(values=topicsData)
        else:
            self.window['-TOPIC-'].Update(values=topicsData)
            self.window['-TOPIC-'].Update(disabled=True)

        self.window['-PROBLEM-'].Update(values=[''])
        self.window['-PROBLEM-'].Update(disabled=True)


    def problemsListbox(self):
        """
        update the Problems listbox to contain the new loaded problems
        """
        if not self.getProblems(): problemsData = []
        else:
            problemsData = self.problemsDict[self.values["-TOPIC-"][0]]

        if problemsData != []:
            self.window['-PROBLEM-'].Update(disabled=False)
            self.window['-PROBLEM-'].Update(values=problemsData)
        else:
            self.window['-PROBLEM-'].Update(values=problemsData)
            self.window['-PROBLEM-'].Update(disabled=True)
        self.window['-PROBLEM-'].Update(values=problemsData)


    def resetListboxs(self):
        if not self.getModules(): self.populateProblems()
        if self.modulesList == []: 
            self.window["-MODULE-"].Update(self.modulesList)
            self.window["-MODULE-"].Update(disabled=True)
        else:
            self.window["-MODULE-"].Update(disabled=False)
            self.window["-MODULE-"].Update(self.modulesList)

        self.window["-TOPIC-"].Update([''])
        self.window['-TOPIC-'].Update(disabled=True)

        self.window["-PROBLEM-"].Update([''])
        self.window['-PROBLEM-'].Update(disabled=True)

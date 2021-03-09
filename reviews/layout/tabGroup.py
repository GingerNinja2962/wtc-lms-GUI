import PySimpleGUI as sg

import os

import core


class tabGroupClass():
    def __init__(self, layout):
        super().__init__()
        self.layout = layout
        self.tabGroup()


    def tabGroup(self):
        """
        generates a tabGroup that holds Tabs names after modules holding the problems for that module
        """
        self.layout.assignmentData.getTopicNamesUUID()
        layout = []

        for module in self.layout.assignmentData.topicNamesUUID:
            content = self.getModuleProblems(module)
            if content == []: continue

            layout.append( sg.Tab( module, [ [ sg.Listbox( content,
                    key=f"-{module}-", size=(40,22),) ] ], pad=(0, 20) ) )

        self.tabGrouplayout =  [ [ sg.TabGroup( [layout] ) ] ]


    def getModuleProblems(self, topicFile):
        """
        returns a dictionary of all the assignments linked to the module as akey
        """
        moduleProblems = []
        topicFilePath = f"{self.layout.assignmentData.topicsPath}/{topicFile}.txt"

        grepTopicProcess = core.grepCall("-i", " \[", topicFilePath)
        (problemNames, err) = core.systemCallComms(grepTopicProcess)

        for problem in problemNames.split('\n'):
            problem = (problem.split(' ['))[0]
            if problem == '': continue

            problemFilePath = f"{self.layout.assignmentData.problemsPath}/{problem}.txt"
            grepProblemProcess = core.grepCall("-i", " \[", problemFilePath)
            (assignmentNames, err) = core.systemCallComms(grepProblemProcess)

            for assignment in assignmentNames.split('\n'):
                assignment = (assignment.split(' ['))[0]
                if assignment == '': continue

                moduleProblems.append(assignment)
        return moduleProblems

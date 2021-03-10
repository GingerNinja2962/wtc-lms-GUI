import PySimpleGUI as sg

from core import grepCall, systemCallComms


class tabGroupClass:
    """
    A class to create a tab group layout for the reviews window.

    Methods
    -------
        tabGroup()
            Generate a tabGroup that holds Tabs names after making a
            dict of modules holding problems under those modules.
        getModuleProblems()
            Returns a dictionary of all the assignments linked to
            their modules as a key.
    """
    def __init__(self, layout):
        """
        The constructor for tabGroupClass.

        Parameters
        ----------
            layout : list
                The layout of the reviews window.
        """
        super().__init__()
        self.layout = layout
        self.tabGroup()


    def tabGroup(self):
        """
        Generate a tabGroup that holds Tabs names after making a dict
        of modules holding problems under those modules.
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
        Returns a dictionary of all the assignments linked to their
        modules as a key.
        """
        moduleProblems = []
        topicPath = f"{self.layout.assignmentData.topicsPath}/{topicFile}.txt"

        grepTopicProcess = grepCall("-i", " \[", topicPath)
        (problemNames, err) = systemCallComms(grepTopicProcess)

        for problem in problemNames.split('\n'):
            problem = (problem.split(' ['))[0]
            if problem == '': continue

            FPath = f"{self.layout.assignmentData.problemsPath}/{problem}.txt"
            grepProblemProcess = grepCall("-i", " \[", FPath)
            (assignmentNames, err) = systemCallComms(grepProblemProcess)

            for assignment in assignmentNames.split('\n'):
                assignment = (assignment.split(' ['))[0]
                if assignment == '': continue

                moduleProblems.append(assignment)
        return moduleProblems

from core.populate_save_data.populate_topics import populateTopicsClass

import core


class populateProblemsClass(populateTopicsClass):
    def __init__(self):
        super().__init__()
        self.problemsPath = core.dirCheck(f"{self.saveDataPath}/problemsData")
        self.problemsDataPaths = []


    def populateProblems(self):
        self.populateTopics()
        self.problemsDataPaths = []

        for topicFile in self.topicsDataPaths:
            grepTopicsCall = core.grepCall("-i", " \[", topicFile)
            (lmsProblemsData, err) = core.systemCallComms(grepTopicsCall)

            lmsProblemsData = lmsProblemsData.split(')\n')
            problemsData = {}

            for string in lmsProblemsData:
                if string == '': continue
                string = string.split(' (')
                problemsData[(string[0].split(' ['))[0]] = string[1]

            for topicName in problemsData.keys():
                lmsProblemsCall = core.lmsCall(["wtc-lms", "problems", problemsData[topicName]])
                (lmsAssignmentData, err) = core.systemCallComms(lmsProblemsCall)
                self.problemsDataPaths.append(f"{self.problemsPath}/{topicName}.txt")
                core.writeToFile(lmsAssignmentData, self.problemsDataPaths[-1])

        token = core.tokensClass()
        token.forceTokenUpdate("Assignment")
        self.closeLoadingMessage()

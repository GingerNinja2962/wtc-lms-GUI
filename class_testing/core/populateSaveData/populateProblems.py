from core.populateSaveData.populateTopics import populateTopicsClass

import classTemplates
import core


class populateProblemsClass(populateTopicsClass):
    def __init__(self):
        super().__init__()
        self.problemsPath = core.dirCheck(f"{self.saveDataPath}/problemsData")
        self.problemsDataPaths = []
        self.problemsDict = {}
        self.problemsState = {}


    def populateProblems(self):
        self.populateTopics()

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


    def getProblems(self):
        if core.fileCheck(f"{self.problemsPath}/{self.values['-TOPIC-'][0]}.txt"):
            grepTopicsCall = core.grepCall("-i", " \[", f"{self.problemsPath}/{self.values['-TOPIC-'][0]}.txt")
            (lmsProblemsData, err) = core.systemCallComms(grepTopicsCall)
        else:
            return False

        lmsProblemsData = lmsProblemsData.split(')\n')
        problemsData = []

        for string in lmsProblemsData:
            if string == '': continue
            problemsData.append((((string.split(' ('))[0]).split(' ['))[0])
            self.problemsState[(((string.split(' ('))[0]).split(' ['))[0]] = ((string.replace(' [', ']')).split(']'))[1]
        self.problemsDict[self.values["-TOPIC-"][0]] = problemsData
        return True

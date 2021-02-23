from core import dirCheck, writeToFile, tokensClass, lmsCall, grepCall, systemCallComms, populateSaveData
import os


class populateAssignmentsClass(populateSaveData.populateReviewsClass):
    def __init__(self):
        super().__init__()
        self.modulesPath = dirCheck(f"{self.saveDataPath}/modulesData")
        self.modulesDataPath = f"{self.modulesPath}/modulesData.txt"
        self.topicsPath = dirCheck(f"{self.saveDataPath}/topicsData")
        self.problemsPath = dirCheck(f"{self.saveDataPath}/problemsData")

        self.topicNamesUUID = {}
        self.problemNamesUUID = {}
        self.topicFilePaths = []
        self.problemFilePaths = []


    def populateAssignments(self):
        self.populateModules()
        self.populateTopics()
        self.populateProblems()


    def populateModules(self):
        self.openLoadingMessage("assignments")
        dirCheck(f"{dirCheck(self.saveDataPath)}/modulesData")

        modulesDataProcess = lmsCall("modules")
        (modulesData, err) = systemCallComms(modulesDataProcess)
        writeToFile(modulesData, self.modulesDataPath)


    def populateTopics(self):
        self.getTopicNamesUUID()
        dirCheck(f"{dirCheck(self.saveDataPath)}/topicsData")
        self.topicFilePaths = []

        for module in self.topicNamesUUID.keys():
            lmsTopicsCall = lmsCall(["wtc-lms", "topics", self.topicNamesUUID[module]])
            (lmsProblemsData, err) = systemCallComms(lmsTopicsCall)
            self.topicFilePaths.append(f"{self.topicsPath}/{module}.txt")
            writeToFile(lmsProblemsData, self.topicFilePaths[-1])


    def populateProblems(self):
        self.getProblemNamesUUID()
        dirCheck(f"{dirCheck(self.saveDataPath)}/problemsData")
        self.problemFilePaths = []

        for topic in self.problemNamesUUID.keys():
            lmsProblemsCall = lmsCall(["wtc-lms", "problems", self.problemNamesUUID[topic]])
            (lmsAssignmentData, err) = systemCallComms(lmsProblemsCall)
            self.problemFilePaths.append(f"{self.problemsPath}/{topic}.txt")
            writeToFile(lmsAssignmentData, self.problemFilePaths[-1])

        assignmentstoken = tokensClass()
        assignmentstoken.forceTokenUpdate("Assignment")
        self.closeLoadingMessage()


    def getTopicNamesUUID(self):
        self.topicNamesUUID = {}
        dirCheck(f"{dirCheck(self.saveDataPath)}/modulesData")
        grepModulesCall = grepCall("-i", " \[", self.modulesDataPath)
        (lmsTopicsData, err) = systemCallComms(grepModulesCall)

        for string in lmsTopicsData.split(')\n'):
            if string == '': continue
            self.topicNamesUUID[(((string.split(' ('))[0]).split(' ['))[0]] = (string.split(' ('))[1]


    def getProblemNamesUUID(self):
        self.problemNamesUUID = {}
        self.topicFilePaths = []
        dirCheck(f"{dirCheck(self.saveDataPath)}/topicsData")

        for topicFile in os.listdir(self.topicsPath):
            self.topicFilePaths.append(f"{self.topicsPath}/{topicFile}")

        for topicFile in self.topicFilePaths:
            grepTopicsCall = grepCall("-i", " \[", topicFile)
            (lmsProblemsData, err) = systemCallComms(grepTopicsCall)

            for string in lmsProblemsData.split(')\n'):
                if string == '': continue
                self.problemNamesUUID[(((string.split(' ('))[0]).split(' ['))[0]] = (string.split(' ('))[1]

from core import dirCheck, fileCheck, grepCall, systemCallComms
from core.populateSaveData.populateAssignments import populateAssignmentsClass

import os

import core


class dataHandelerClass(populateAssignmentsClass):
    def __init__(self):
        super().__init__()
        self.modulesList = []
        self.topicsDict = {}
        self.problemsDict = {}
        self.assignmentsDict = {}


    def getModules(self):
        self.modulesList = []
        if not fileCheck(self.modulesDataPath): self.populateAssignments()

        grepModulesCall = grepCall("-i", " \[", self.modulesDataPath)
        (lmsModulesData, err) = systemCallComms(grepModulesCall)

        for module in lmsModulesData.split(')\n'):
            if module == '': continue
            self.modulesList.append((module.split(' ['))[0])


    def getTopics(self):
        if self.topicFilePaths == []:
            for topicFile in os.listdir(self.topicsPath):
                self.topicFilePaths.append(f"{self.topicsPath}/{topicFile}")

        for topicPath in self.topicFilePaths:
            if not fileCheck(topicPath): continue
            grepTopicsCall = grepCall("-i", " \[", topicPath)
            (lmsTopicsData, err) = systemCallComms(grepTopicsCall)

            moduleName = ((topicPath.split("/"))[-1]).replace(".txt", '')
            topicsList = []

            for topic in lmsTopicsData.split(')\n'):
                if topic == '': continue
                topicsList.append((topic.split(' ['))[0])
            self.topicsDict[moduleName] = topicsList


    def getProblems(self):
        self.problemsState = {}
        for problemFile in os.listdir(self.problemsPath):
            grepProblemsCall = grepCall("-i", " \[", f"{self.problemsPath}/{problemFile}")
            (lmsProblemsData, err) = systemCallComms(grepProblemsCall)

            topicName = (((problemFile.split('/'))[-1]).replace('.txt', ''))

            lmsProblemsData = lmsProblemsData.split(')\n')
            problemsData = []

            for string in lmsProblemsData:
                if string == '': continue
                problemsData.append((string.split(' ['))[0])
                self.problemsState[problemsData[-1]] = (
                        (string.replace(' [', ']')).split(']'))[1]
            self.problemsDict[topicName] = problemsData


    def getAssignments(self):
        for problemFile in os.listdir(self.problemsPath):
            grepProblemsCall = grepCall("-i", " \[", f"{self.problemsPath}/{problemFile}")
            (lmsProblemsData, err) = systemCallComms(grepProblemsCall)

            lmsProblemsData = lmsProblemsData.split(')\n')

            for string in lmsProblemsData:
                if string == '': continue
                self.assignmentsDict[(string.split(' ['))[0]] = (string.split(' ('))[1]
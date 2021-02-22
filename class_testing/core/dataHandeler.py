from core import dirCheck, fileCheck, grepCall, systemCallComms
from core.populateSaveData.populateAssignments import populateAssignmentsClass


class dataHandelerClass(populateAssignmentsClass):
    def __init__(self):
        super().__init__()
        self.modulesList = []


    def getModules(self): # TODO fix
        self.modulesList = []
        if fileCheck(self.modulesDataPath):
            grepModulesCall = grepCall("-i", " \[", self.modulesDataPath)
            (lmsModulesData, err) = systemCallComms(grepModulesCall)

            for module in lmsModulesData.split(')\n'):
                if module == '': continue
                self.modulesList.append(((module.split(' ('))[0].split(' ['))[0])


    def getTopics(self): # TODO fix
        if self.topicsDataPaths == []:
            for module in self.getTopicNames().keys():
                self.topicsDataPaths.append(f"{self.topicsPath}/{module}.txt")

        for topicPath in self.topicsDataPaths:
            if not fileCheck(topicPath): continue
            grepTopicsCall = grepCall("-i", " \[", topicPath)
            (lmsTopicsData, err) = systemCallComms(grepTopicsCall)

            moduleName = ((topicPath.split("/"))[-1]).replace(".txt", '')

            topicsList = []
            for topic in lmsTopicsData.split(')\n'):
                if topic == '': continue
                topicsList.append((((topic.split(' ('))[0]).split(' ['))[0])
            self.topicsDict[moduleName] = topicsList
        if len(self.topicsDict.keys()) < 1:
            return False
        return True


    def getProblems(self): # TODO fix
        if fileCheck(f"{self.problemsPath}/{self.values['-TOPIC-'][0]}.txt"):
            grepTopicsCall = grepCall("-i", " \[", f"{self.problemsPath}/{self.values['-TOPIC-'][0]}.txt")
            (lmsProblemsData, err) = systemCallComms(grepTopicsCall)
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

from core.populateSaveData.populateModules import populateModulesClass

import core


class populateTopicsClass(populateModulesClass):
    def __init__(self):
        super().__init__()
        self.topicsPath = core.dirCheck(f"{self.saveDataPath}/topicsData")
        self.topicsDataPaths = []
        self.topicsDict = {}


    def populateTopics(self):
        self.populateModules()

        topicsData = self.getTopicNames()

        for module in topicsData.keys():
            lmsTopicsCall = core.lmsCall(["wtc-lms", "topics", topicsData[module]])
            (lmsProblemsData, err) = core.systemCallComms(lmsTopicsCall)
            self.topicsDataPaths.append(f"{self.topicsPath}/{module}.txt")
            core.writeToFile(lmsProblemsData, self.topicsDataPaths[-1])


    def getTopics(self):
        if self.topicsDataPaths == []:
            for module in self.getTopicNames().keys():
                self.topicsDataPaths.append(f"{self.topicsPath}/{module}.txt")

        for topicPath in self.topicsDataPaths:
            if not core.fileCheck(topicPath): continue
            grepTopicsCall = core.grepCall("-i", " \[", topicPath)
            (lmsTopicsData, err) = core.systemCallComms(grepTopicsCall)

            moduleName = ((topicPath.split("/"))[-1]).replace(".txt", '')

            topicsList = []
            for topic in lmsTopicsData.split(')\n'):
                if topic == '': continue
                topicsList.append((((topic.split(' ('))[0]).split(' ['))[0])
            self.topicsDict[moduleName] = topicsList
        if len(self.topicsDict.keys()) < 1:
            return False
        return True


    def getTopicNames(self):
        grepModulesCall = core.grepCall("-i", " \[", self.modulesDataPath)
        (lmsTopicsData, err) = core.systemCallComms(grepModulesCall)

        lmsTopicsData = lmsTopicsData.split(')\n')
        topicsData = {}

        for string in lmsTopicsData:
            if string == '': continue
            topicsData[(((string.split(' ('))[0]).split(' ['))[0]] = (string.split(' ('))[1]
        return topicsData

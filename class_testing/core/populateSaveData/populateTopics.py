from core.populate_save_data.populate_modules import populateModulesClass

import core


class populateTopicsClass(populateModulesClass):
    def __init__(self):
        super().__init__()
        self.topicsPath = core.dirCheck(f"{self.saveDataPath}/topicsData")
        self.topicsDataPaths = []
        self.topicsDict = {}


    def populateTopics(self):
        self.populateModules()
        self.topicsDataPaths = []

        topicsData = self.getTopicNames()

        for module in topicsData.keys():
            lmsTopicsCall = core.lmsCall(["wtc-lms", "topics", topicsData[module]])
            (lmsProblemsData, err) = core.systemCallComms(lmsTopicsCall)
            self.topicsDataPaths.append(f"{self.topicsPath}/{module}.txt")
            core.writeToFile(lmsProblemsData, self.topicsDataPaths[-1])


    def getTopics(self):
        if self.topicsDataPaths == []:
            topicsData = self.getTopicNames()
            for module in topicsData.keys():
                self.topicsDataPaths.append(f"{self.topicsPath}/{module}.txt")

        for topicPath in self.topicsDataPaths:
            grepTopicsCall = core.grepCall("-i", " \[", self.topicPath)
            (lmsTopicsData, err) = core.systemCallComms(grepTopicsCall)

            moduleName = ((topicPath.split("/"))[-1]).replace(".txt", '')

            topicsList = []
            for topic in lmsTopicsData.split(')\n'):
                if topic == '': continue
                topicsList.append((((topic.split(' ('))[0]).split(' ['))[0])
            self.topicsDict[moduleName] = topicsList


    def getTopicNames(self):
        grepModulesCall = core.grepCall("-i", " \[", self.modulesDataPath)
        (lmsTopicsData, err) = core.systemCallComms(grepModulesCall)

        lmsTopicsData = lmsTopicsData.split(')\n')
        topicsData = {}

        for string in lmsTopicsData:
            if string == '': continue
            topicsData[(((string.split(' ('))[0]).split(' ['))[0]] = string[1]
        return topicsData

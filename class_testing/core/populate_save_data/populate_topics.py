from core.populate_save_data.populate_modules import populateModulesClass

import core


class populateTopicsClass(populateModulesClass):
    def __init__(self):
        super().__init__()
        self.topicsPath = core.dirCheck(f"{self.saveDataPath}/topicsData")
        self.topicsDataPaths = []


    def populateTopics(self):
        self.populateModules()
        self.topicsDataPaths = []

        grepModulesCall = core.grepCall("-i", " \[", self.modulesDataPath)
        (lmsTopicsData, err) = core.systemCallComms(grepModulesCall)

        lmsTopicsData = lmsTopicsData.split(')\n')
        topicsData = {}

        for string in lmsTopicsData:
            if string == '': continue
            string = string.split(' (')
            topicsData[(string[0].split(' ['))[0]] = string[1]

        for moduleName in topicsData.keys():
            lmsTopicsCall = core.lmsCall(["wtc-lms", "topics", topicsData[moduleName]])
            (lmsProblemsData, err) = core.systemCallComms(lmsTopicsCall)
            self.topicsDataPaths.append(f"{self.topicsPath}/{moduleName}.txt")
            core.writeToFile(lmsProblemsData, self.topicsDataPaths[-1])

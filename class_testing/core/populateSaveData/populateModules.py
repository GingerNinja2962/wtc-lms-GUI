from baseClasses.basePopulateData import populateData

import core


class populateModulesClass(populateData):
    def __init__(self):
        super().__init__()
        self.modulesPath = core.dirCheck(f"{self.saveDataPath}/modulesData")
        self.modulesDataPath = f"{self.modulesPath}/modulesData.txt"
        self.modulesList = []


    def populateModules(self):
        self.openLoadingMessage("assignments")

        modulesDataProcess = core.lmsCall("modules")
        (modulesData, err) = core.systemCallComms(modulesDataProcess)

        core.writeToFile(modulesData, self.modulesDataPath)


    def getModules(self):
        grepModulesCall = core.grepCall("-i", " \[", self.modulesDataPath)
        (lmsModulesData, err) = core.systemCallComms(grepModulesCall)

        for Module in lmsModulesData.split(')\n'):
            if Module == '': continue
            self.modulesList.append(((Module.split(' ('))[0].split(' ['))[0])

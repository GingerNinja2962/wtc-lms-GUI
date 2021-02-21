import classTemplates

import core


class populateModulesClass(classTemplates.basePopulateDataClass):
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
        if not core.fileCheck(self.modulesDataPath):
            return False
        grepModulesCall = core.grepCall("-i", " \[", self.modulesDataPath)
        (lmsModulesData, err) = core.systemCallComms(grepModulesCall)

        for module in lmsModulesData.split(')\n'):
            if module == '': continue
            self.modulesList.append(((module.split(' ('))[0].split(' ['))[0])
        return True

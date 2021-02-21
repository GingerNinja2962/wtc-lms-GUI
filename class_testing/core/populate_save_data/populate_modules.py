from baseClasses.basePopulateData import populateData

import core


class populateModulesClass(populateData):
    def __init__(self):
        super().__init__()
        self.modulesPath = core.dirCheck(f"{self.saveDataPath}/modulesData")
        self.modulesDataPath = f"{self.modulesPath}/modulesData.txt"


    def populateModules(self):
        self.openLoadingMessage("assignments")

        modulesDataProcess = core.lmsCall("modules")
        lmsModulesGrep = core.grepSystemCall("-iA3", "]", modulesDataProcess)

        core.systemCallClose(modulesDataProcess)
        (modulesData, err) = core.systemCallComms(lmsModulesGrep)

        core.writeToFile(modulesData, self.modulesDataPath)

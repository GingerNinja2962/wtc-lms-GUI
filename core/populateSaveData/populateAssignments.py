from classTemplates.populateTemplate import basePopulateDataClass

from os import listdir

from core.lmsLogin import manageLogin
from core import dirCheck, writeToFile, tokensClass, fileCheck
from core import lmsCall, grepCall, systemCallComms


class populateAssignmentsClass(basePopulateDataClass):
    """
    A class to be used to manage population of the saved assignments
    data from wtc-lms.

    Parameters
    ----------
        basePopulateDataClass : class
            The base population data class to inherit from when
            working with the population of the assignments data.

    Attributes
    ----------
        modulesPath : str
            The path to the modules data folder.
        modulesDataPath : str
            The path to the modules data file.
        topicsPath : str
            The path to the topics data folder.
        problemsPath : str
            The path to the problems data file.
        topicNamesUUID : dict
            The dictionary of topic names linked to their UUIDS.
        problemNamesUUID : dict
            The dictionary of problme names linked to their UUIDS.
        topicFilePaths : list
            The list of topic file paths.
        problemFilePaths : list
            The list of problem file paths.

    Methods
    -------
        populateAssignments()
            Populates the assignments moudles, topic and problems
            data.
        populateModules()
            Populates the assignments moudles into the modules data
            file.
        populateTopics()
            Populates the assignments topic into the topics data
            files.
        populateProblems()
            Populates the assignments problems into the problems data.
        getTopicNamesUUID()
            Generates the dict of topics and the topic UUIDs.
        getProblemNamesUUID()
            Generates the dict of problems and the problem UUIDs.
    """
    def __init__(self):
        """
        The constructor for populateAssignmentsClass.
        """
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
        """
        Populates the assignments moudles, topic and problems data.

        Returns
        -------
            manageLoginStatus : boollean
                The status of the data population, false if the data
                was not updated, True if the data was updated.
        """
        if not manageLogin().run():
            return False

        self.populateModules()
        self.populateTopics()
        self.populateProblems()
        return True


    def populateModules(self):
        """
        Populates the assignments moudles into the modules data file.
        """
        self.openLoadingMessage("assignments")
        dirCheck(f"{dirCheck(self.saveDataPath)}/modulesData")

        modulesDataProcess = lmsCall("modules")
        (modulesData, err) = systemCallComms(modulesDataProcess)
        writeToFile(modulesData, self.modulesDataPath)


    def populateTopics(self):
        """
        Populates the assignments topic into the topics data files.
        """
        self.getTopicNamesUUID()
        dirCheck(f"{dirCheck(self.saveDataPath)}/topicsData")
        self.topicFilePaths = []

        for module in self.topicNamesUUID.keys():
            lmsTopicsCall = lmsCall(["wtc-lms", "topics", self.topicNamesUUID[
                module]])
            (lmsProblemsData, err) = systemCallComms(lmsTopicsCall)
            self.topicFilePaths.append(f"{self.topicsPath}/{module}.txt")
            writeToFile(lmsProblemsData, self.topicFilePaths[-1])


    def populateProblems(self):
        """
        Populates the assignments problems into the problems data.
        files.
        """
        self.getProblemNamesUUID()
        dirCheck(f"{dirCheck(self.saveDataPath)}/problemsData")
        self.problemFilePaths = []

        for topic in self.problemNamesUUID.keys():
            lmsProblemsCall = lmsCall(["wtc-lms", "problems",
                self.problemNamesUUID[topic]])
            (lmsAssignmentData, err) = systemCallComms(lmsProblemsCall)
            self.problemFilePaths.append(f"{self.problemsPath}/{topic}.txt")
            writeToFile(lmsAssignmentData, self.problemFilePaths[-1])

        assignmentstoken = tokensClass()
        assignmentstoken.forceTokenUpdate("Assignment")
        self.closeLoadingMessage()


    def getTopicNamesUUID(self):
        """
        Generates the dict of topics and the topic UUIDs.
        """
        self.topicNamesUUID = {}
        dirCheck(f"{dirCheck(self.saveDataPath)}/modulesData")
        grepModulesCall = grepCall("-i", " \[", self.modulesDataPath)
        (lmsTopicsData, err) = systemCallComms(grepModulesCall)

        for string in lmsTopicsData.split(')\n'):
            if string == '': continue
            self.topicNamesUUID[(((string.split(' ('))[0]).split(' ['))[0]] = (
                string.split(' ('))[1]


    def getProblemNamesUUID(self):
        """
        Generates the dict of problems and the problem UUIDs.
        """
        dirCheck(self.modulesPath)
        if not fileCheck(self.modulesDataPath):
            if not fileCheck(f"{self.saveDataPath}/tokens/loginF"):
                if not self.populateAssignments(): return False
            else: return False

        self.problemNamesUUID = {}
        self.topicFilePaths = []
        dirCheck(f"{dirCheck(self.saveDataPath)}/topicsData")

        for topicFile in listdir(self.topicsPath):
            self.topicFilePaths.append(f"{self.topicsPath}/{topicFile}")

        for topicFile in self.topicFilePaths:
            grepTopicsCall = grepCall("-i", " \[", topicFile)
            (lmsProblemsData, err) = systemCallComms(grepTopicsCall)

            for string in lmsProblemsData.split(')\n'):
                if string == '': continue
                self.problemNamesUUID[(((string.split(' ('))[0]).split(' ['))
                    [0]] = (string.split(' ('))[1]

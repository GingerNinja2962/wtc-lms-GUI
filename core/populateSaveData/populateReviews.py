import PySimpleGUI as sg

from classTemplates.populateTemplate import basePopulateDataClass

from core.lmsLogin import manageLogin
from core import tokensClass, dirCheck, fileCheck
from core import lmsCall, systemCallComms, grepCall, writeToFile


class populateReviewsClass(basePopulateDataClass):
    """
    A class to be used to manage population of the saved reviews
    data from wtc-lms.

    Parameters
    ----------
        basePopulateDataClass : class
            The base population data class to inherit from when
            working with the population of the reviews data.

    Attributes
    ----------
        reviewsDataPath : str
            The path to the reviews data folder.
        reviewsPath : str
            The path to the reviews data file.
        token : object
            The token object created from tokensClass to manage all
            token related data.
        reviewUUIDs : list
            A list of all review UUIDs.
        reviewsInvited : int
            An int value of the number of reviews you have been
            invited to.
        reviewsAssigned : int
            An int value of the number of reviews you have been
            assigned.
        reviewsGraded : int
            An int value of the number of reviews you have graded.
        reviewsBlocked : int
            An int value of the number of reviews you have been
            blocked from.

    Methods
    -------
        populateReviews()
            Updated the saved reviews data with an automatic message
            stating that.
        getReviewData()
            Retrive all the reviews data, count data and if there is
            no reviews data downloads it.
        getInvitedReviews()
            Count the total number of invited reviews.
        getAssignedReviews()
            Count the total number of assigned reviews.
        getGradedReviews()
            Count the total number of graded reviews.
        getAcceptanceBlockedReviews()
            Count the total number of blocked reviews.
        getReviewUUIDs()
            Create a list of all the review UUIDs.
    """
    def __init__(self):
        """
        The constructor for populateReviewsClass.
        """
        super().__init__()
        self.reviewsDataPath = dirCheck(f"{self.saveDataPath}/reviewsData")
        self.reviewsPath = f"{self.reviewsDataPath}/reviewsData.txt"
        self.token = tokensClass()
        self.reviewUUIDs = []

        self.reviewsInvited = 0
        self.reviewsAssigned = 0
        self.reviewsGraded = 0
        self.reviewsBlocked = 0


    def populateReviews(self):
        """
        Updated the saved reviews data with an automatic message
        stating that.

        Returns
        -------
            manageLoginStatus : boollean
                The status of the data population, false if the data
                was not updated, True if the data was updated.
        """
        if not manageLogin().run():
            return False

        self.openLoadingMessage("reviews")
        reviewsDataProcess = lmsCall("reviews")
        (reviewsData, err) = systemCallComms(reviewsDataProcess)

        writeToFile(reviewsData, self.reviewsPath)
        self.token.forceTokenUpdate("Review")
        self.closeLoadingMessage()
        return True


    def getReviewData(self):
        """
        Retrive all the reviews data, count data and if there is no
        reviews data downloads it.
        """
        dirCheck(self.reviewsDataPath)
        if not fileCheck(self.reviewsPath):
            if not fileCheck(f"{self.saveDataPath}/tokens/loginF"):
                if not self.populateReviews(): return False
            else: return False

        self.getInvitedReviews()
        self.getAssignedReviews()
        self.getGradedReviews()
        self.getAcceptanceBlockedReviews()
        self.getReviewUUIDs()
        return True


    def getInvitedReviews(self):
        """
        Count the total number of invited reviews.
        """
        grepInvitedProcess = grepCall("-ic", "Invited", self.reviewsPath)
        (reviewsInvited, err) = systemCallComms(grepInvitedProcess)
        self.reviewsInvited = reviewsInvited


    def getAssignedReviews(self):
        """
        Count the total number of assigned reviews.
        """
        grepAssignedProcess = grepCall("-ic", "Assigned", self.reviewsPath)
        (reviewsAssigned, err) = systemCallComms(grepAssignedProcess)
        self.reviewsAssigned = reviewsAssigned


    def getGradedReviews(self):
        """
        Count the total number of graded reviews.
        """
        grepGradedProcess = grepCall("-ic", "Graded", self.reviewsPath)
        (reviewsGraded, err) = systemCallComms(grepGradedProcess)
        self.reviewsGraded = reviewsGraded


    def getAcceptanceBlockedReviews(self):
        """
        Count the total number of blocked reviews.
        """
        grepBlockedProcess = grepCall("-ic", "AcceptanceBlocked",
            self.reviewsPath)
        (reviewsBlocked, err) = systemCallComms(grepBlockedProcess)
        self.reviewsBlocked = reviewsBlocked


    def getReviewUUIDs(self):
        """
        Create a list of all the review UUIDs.
        """
        self.reviewUUIDs = []

        grepUUIDsProcess = grepCall("-i", " (", self.reviewsPath)
        (reviewUUIDs, err) = systemCallComms(grepUUIDsProcess)

        for UUID in reviewUUIDs.split('\n'):
            if UUID == '': continue
            self.reviewUUIDs.append((((UUID.split(' ('))[1]).split(') '))[0])

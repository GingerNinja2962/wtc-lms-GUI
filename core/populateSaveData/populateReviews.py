from classTemplates.populateTemplate import basePopulateDataClass

import core


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
        self.reviewsDataPath = core.dirCheck(f"{self.saveDataPath}/reviewsData")
        self.reviewsPath = f"{self.reviewsDataPath}/reviewsData.txt"
        self.token = core.tokensClass()
        self.reviewUUIDs = []

        self.reviewsInvited = 0
        self.reviewsAssigned = 0
        self.reviewsGraded = 0
        self.reviewsBlocked = 0


    def populateReviews(self):
        """
        Updated the saved reviews data with an automatic message
        stating that.
        """
        self.openLoadingMessage("reviews")
        reviewsDataProcess = core.lmsCall("reviews")
        (reviewsData, err) = core.systemCallComms(reviewsDataProcess)

        core.writeToFile(reviewsData, self.reviewsPath)
        self.token.forceTokenUpdate("Review")
        self.closeLoadingMessage()


    def getReviewData(self):
        """
        Retrive all the reviews data, count data and if there is no
        reviews data downloads it.
        """
        core.dirCheck(self.reviewsDataPath)
        if not core.fileCheck(self.reviewsPath): self.populateReviews()
        self.getInvitedReviews()
        self.getAssignedReviews()
        self.getGradedReviews()
        self.getAcceptanceBlockedReviews()
        self.getReviewUUIDs()


    def getInvitedReviews(self):
        """
        Count the total number of invited reviews.
        """
        grepInvitedProcess = core.grepCall("-ic", "Invited", self.reviewsPath)
        (reviewsInvited, err) = core.systemCallComms(grepInvitedProcess)
        self.reviewsInvited = reviewsInvited


    def getAssignedReviews(self):
        """
        Count the total number of assigned reviews.
        """
        grepAssignedProcess = core.grepCall("-ic", "Assigned", self.reviewsPath)
        (reviewsAssigned, err) = core.systemCallComms(grepAssignedProcess)
        self.reviewsAssigned = reviewsAssigned


    def getGradedReviews(self):
        """
        Count the total number of graded reviews.
        """
        grepGradedProcess = core.grepCall("-ic", "Graded", self.reviewsPath)
        (reviewsGraded, err) = core.systemCallComms(grepGradedProcess)
        self.reviewsGraded = reviewsGraded


    def getAcceptanceBlockedReviews(self):
        """
        Count the total number of blocked reviews.
        """
        grepBlockedProcess = core.grepCall("-ic", "AcceptanceBlocked",
            self.reviewsPath)
        (reviewsBlocked, err) = core.systemCallComms(grepBlockedProcess)
        self.reviewsBlocked = reviewsBlocked


    def getReviewUUIDs(self):
        """
        Create a list of all the review UUIDs.
        """
        self.reviewUUIDs = []

        grepUUIDsProcess = core.grepCall("-i", " (", self.reviewsPath)
        (reviewUUIDs, err) = core.systemCallComms(grepUUIDsProcess)

        for UUID in reviewUUIDs.split('\n'):
            if UUID == '': continue
            self.reviewUUIDs.append((((UUID.split(' ('))[1]).split(') '))[0])

from classTemplates.populateTemplate import basePopulateDataClass

import core


class populateReviewsClass(basePopulateDataClass):
    def __init__(self):
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
        self.openLoadingMessage("reviews")
        reviewsDataProcess = core.lmsCall("reviews")
        (reviewsData, err) = core.systemCallComms(reviewsDataProcess)

        core.writeToFile(reviewsData, self.reviewsPath)
        self.token.forceTokenUpdate("Review")
        self.closeLoadingMessage()


    def getReviewData(self):
        core.dirCheck(self.reviewsDataPath)
        if not core.fileCheck(self.reviewsPath): self.populateReviews()
        self.getInvitedReviews()
        self.getAssignedReviews()
        self.getGradedReviews()
        self.getAcceptanceBlockedReviews()
        self.getReviewUUIDs()


    def getInvitedReviews(self):
        grepInvitedProcess = core.grepCall("-ic", "Invited", self.reviewsPath)
        (reviewsInvited, err) = core.systemCallComms(grepInvitedProcess)
        self.reviewsInvited = reviewsInvited


    def getAssignedReviews(self):
        grepAssignedProcess = core.grepCall("-ic", "Assigned", self.reviewsPath)
        (reviewsAssigned, err) = core.systemCallComms(grepAssignedProcess)
        self.reviewsAssigned = reviewsAssigned


    def getGradedReviews(self):
        grepGradedProcess = core.grepCall("-ic", "Graded", self.reviewsPath)
        (reviewsGraded, err) = core.systemCallComms(grepGradedProcess)
        self.reviewsGraded = reviewsGraded


    def getAcceptanceBlockedReviews(self):
        grepBlockedProcess = core.grepCall("-ic", "AcceptanceBlocked", self.reviewsPath)
        (reviewsBlocked, err) = core.systemCallComms(grepBlockedProcess)
        self.reviewsBlocked = reviewsBlocked


    def getReviewUUIDs(self):
        self.reviewUUIDs = []

        grepUUIDsProcess = core.grepCall("-i", " (", self.reviewsPath)
        (reviewUUIDs, err) = core.systemCallComms(grepUUIDsProcess)

        for UUID in reviewUUIDs.split('\n'):
            if UUID == '': continue
            self.reviewUUIDs.append((((UUID.split(' ('))[1]).split(') '))[0])

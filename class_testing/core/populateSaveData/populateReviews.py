from baseClasses.basePopulateData import populateData

import core


class populateReviewsClass(populateData):
    def __init__(self):
        super().__init__()
        self.reviewsDataPath = core.dirCheck(f"{self.saveDataPath}/reviewsData")
        self.reviewsPath = f"{self.reviewsDataPath}/reviewsData.txt"


    def populateReviews(self):
        self.openLoadingMessage("reviews")
        reviewsDataProcess = core.lmsCall("reviews")
        (reviewsData, err) = core.systemCallComms(reviewsDataProcess)

        core.writeToFile(reviewsData, self.reviewsPath)
        core.tokensClass.forceTokenUpdate("Review")
        self.closeLoadingMessage()

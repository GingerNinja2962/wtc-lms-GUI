import PySimpleGUI as sg


class framesClass:
    """
    A class to create a filter frame layout for the reviews window.

    Attributes
    ----------
        layout : list
            The layout of the window.
        mainWindow : object
            The PySimpleGUI window object that has been opened.

    Methods
    -------
        reviewFilterFrame()
            Return a filter frame with 4 review filters as checkboxes.
        reviewCounterFrame()
            Generate a PySimpleGUI frame that holds the wtc-lms
            reviews counter data.
        counterData()
            Calculate the counter data for reviews.
        updateCounterFrame()
            Update the review counter data.
    """
    def __init__(self, layout, mainWindow):
        """
        The constructor for framesClass.

        Parameters
        ----------
        layout : list
            The layout of the window. 
        mainWindow : object
            The PySimpleGUI window object that has been opened.
        """
        super().__init__()
        self.layout = layout
        self.mainWindow = mainWindow
        self.reviewFilterFrame()
        self.reviewCounterFrame()


    def reviewFilterFrame(self):
        """
        Return a filter frame with 4 review filters as checkboxes.
        """
        self.filterFrame = [
            [sg.CB('Search all', key='-TOGGLE-ALL-')],
            [sg.Text("-"*34)], # Can be changed to: [sg.HSep(pad=(0,10))],
            [sg.CB('Invited', key='-INVITED-')],
            [sg.CB('Assigned', key='-ASSIGNED-')],
            [sg.CB('Graded', key='-GRADED-')],
            [sg.CB('AcceptanceBlocked', key='-BLOCKED-')]
            ]


    def reviewCounterFrame(self):
        """
        Generate a PySimpleGUI frame that holds the wtc-lms reviews
        counter data.
        """
        self.counterData()
        self.CounterFrame = [
            [ sg.Text(f"Reviews Done:\t{self.reviewsGraded:0>2}",
                key='-REVIEWS-DONE-',pad=(5,0))],
            [ sg.Text(f"Reviews pending:\t{self.reviewsAssigned:0>2}",
                key='-REVIEWS-PENDING-',pad=(5,0))],
            [ sg.Text(f"Reviews needed:\t{self.reviewsNeeded:0>2}",
                key='-REVIEWS-NEEDED-',pad=(5,0))]
        ]


    def counterData(self):
        """
        Calculate the counter data for reviews.
        """
        self.layout.assignmentData.getProblemNamesUUID()
        if not self.layout.reviewsData.getReviewData():
            self.mainWindow.status = False
        else: self.mainWindow.status = True
        problemNames = self.layout.assignmentData.problemNamesUUID.keys()

        self.reviewsAssigned = self.layout.reviewsData.reviewsAssigned
        self.reviewsBlocked = self.layout.reviewsData.reviewsBlocked
        self.reviewsGraded = self.layout.reviewsData.reviewsGraded
        self.reviewsInvited = self.layout.reviewsData.reviewsInvited

        reviewsNeeded = (len(problemNames)* 3) - int(self.reviewsGraded)
        if reviewsNeeded < 1:self.reviewsNeeded = "0"
        else:self.reviewsNeeded = str(reviewsNeeded)


    def updateCounterFrame(self):
        """
        Update the review counter data.
        """
        self.counterData()
        self.mainWindow.window['-REVIEWS-DONE-'].update(
            f"Reviews Done:\t{self.reviewsGraded:0>2}")
        self.mainWindow.window['-REVIEWS-PENDING-'].update(
            f"Reviews pending:\t{self.reviewsAssigned:0>2}")
        self.mainWindow.window['-REVIEWS-NEEDED-'].update(
            f"Reviews needed:\t{self.reviewsNeeded:0>2}")

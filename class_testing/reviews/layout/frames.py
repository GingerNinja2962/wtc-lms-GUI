import PySimpleGUI as sg

from custom_inherit import DocInheritMeta

import os

import reviews
import core


class framesClass(metaclass=DocInheritMeta(style="numpy_with_merge", include_special_methods=True)):
    def __init__(self, layout, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow
        self.layout = layout
        self.reviewFilterFrame()
        self.reviewCounterFrame()


    def reviewFilterFrame(self):
        """
        returns a filter frame with 4 review filters

        :return filterFrame: a frame containing the filters for reviews
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
        returns a sg frame that holds the wtc-lms graded assignments counted data

        :return reviewCountFrame: the sg frame list that holds the review counter frame data
        """
        self.counterData()
        self.CounterFrame = [
            [ sg.Text(f"Reviews Done:\t{self.reviewsGraded:0>2}", key='-REVIEWS-DONE-',pad=(5,0))],
            [ sg.Text(f"Reviews pending:\t{self.reviewsAssigned:0>2}",key='-REVIEWS-PENDING-',pad=(5,0))],
            [ sg.Text(f"Reviews needed:\t{self.reviewsNeeded:0>2}",key='-REVIEWS-NEEDED-',pad=(5,0))]
        ]


    def counterData(self):
        """
        returns the calculationed counter data for reviews
        """
        self.layout.assignmentData.getProblemNamesUUID()
        self.layout.reviewsData.getReviewData()
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
        updates the counter information

        :param window: a sg object holding all the window contents and elements
        """
        self.counterData()
        self.mainWindow.window['-REVIEWS-DONE-'].update(f'Reviews Done:\t{self.reviewsGraded:0>2}')
        self.mainWindow.window['-REVIEWS-PENDING-'].update(f'Reviews pending:\t{self.reviewsAssigned:0>2}')
        self.mainWindow.window['-REVIEWS-NEEDED-'].update(f"Reviews needed:\t{self.reviewsNeeded:0>2}")

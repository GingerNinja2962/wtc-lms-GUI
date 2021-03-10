import PySimpleGUI as sg

import reviews
from core import lmsCall, grepSystemCall, systemCallClose, systemCallComms


def commentHandeler(probelmUUID):
    """
    check wether to add a comment or edit one

    Parameters
    ----------
        probelmUUID : str
            The UUID for the probelm that the comment will be added
            to or removed from.
    """
    commentReviewProcess = lmsCall(["wtc-lms","review_details",
        probelmUUID])
    grepedCommentProcess = grepSystemCall("-i","edit_comment",
        commentReviewProcess)
    systemCallClose(commentReviewProcess)
    (commentReviewData, err) = systemCallComms(grepedCommentProcess)

    if commentReviewData != "":
        return editOrDelComment(probelmUUID)
    addNewComment(probelmUUID)


def addNewComment(probelmUUID):
    """
    Handel the adding of new comments.

    Parameters
    ----------
        probelmUUID : str
            The UUID for the probelm that the comment will be added
            to.
    """
    event, values = sg.Window('WTC-LMS GUI add a comment',
                    [[sg.Text('Comment'), sg.InputText('',
                    tooltip='Check to see commands for UUid',
                    key='-COMMENT-INPUT-')], [sg.Button('Submit'),
                    sg.Button('Cancel')]],
                    location=(500,300)).read(close=True)

    if event == 'Submit':
        commentReviewProcess = lmsCall(["wtc-lms","add_comment",
        probelmUUID, values['-COMMENT-INPUT-']])
        (commentReviewProcess, err) = systemCallComms(commentReviewProcess)
        reviews.reviewHandeler.reviewDetailsPopup(probelmUUID)


def editOrDelComment(probelmUUID):
    """
    Handel the editing or deleting of comments.

    Parameters
    ----------
        probelmUUID : str
            The UUID for the probelm that the comment will be added
            to or removed from.
    """
    event, values = sg.Window('WTC-LMS GUI edit the comment',
                    layout=[[sg.Text('Comment'), sg.InputText('',
                    tooltip='Check to see commands for UUid',
                    key='-COMMENT-INPUT-')], [sg.Button('Submit'),
                    sg.Button('Cancel')]],location=(500, 300)).read(close=True)

    if event == 'Submit':
        commentReviewProcess = lmsCall(["wtc-lms","edit_comment",
        probelmUUID, values['-COMMENT-INPUT-']])
        (out, err) = systemCallComms(commentReviewProcess)
        reviews.reviewHandeler.reviewDetailsPopup(probelmUUID)

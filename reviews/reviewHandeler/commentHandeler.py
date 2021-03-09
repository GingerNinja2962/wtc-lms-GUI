import PySimpleGUI as sg

import reviews
import core


def commentHandeler(probelmUUID, window):
    """
    check wether to add a comment or edit one

    :param probelmUUID: the UUID for the probelm
    :param window: this is the window that holds all elements
    """
    commentReviewProcess = core.lmsCall(["wtc-lms","review_details", probelmUUID])
    grepedCommentProcess = core.grepSystemCall("-i","edit_comment", commentReviewProcess)
    core.systemCallClose(commentReviewProcess)
    (commentReviewData, err) = core.systemCallComms(grepedCommentProcess)

    if commentReviewData != "":
        return editOrDelComment(probelmUUID)
    addNewComment(probelmUUID)


def addNewComment(probelmUUID):
    """
    handels the adding of new comments

    :param probelmUUID: the UUID for the probelm
    """
    event, values = sg.Window('WTC-LMS GUI add a comment',
                    [[sg.Text('Comment'), sg.InputText('',
                    tooltip='Check to see commands for UUid',
                    key='-COMMENT-INPUT-')], [sg.Button('Submit'),
                    sg.Button('Cancel')]],
                    location=(500,300)).read(close=True)

    if event == 'Submit':
        commentReviewProcess = core.lmsCall(["wtc-lms","add_comment",
        probelmUUID, values['-COMMENT-INPUT-']])
        (commentReviewProcess, err) = core.systemCallComms(commentReviewProcess)
        reviews.reviewHandeler.reviewDetailsPopup(probelmUUID)


def editOrDelComment(probelmUUID):
    """
    handels the editing or deleting of coments

    :param probelmUUID: the UUID for the probelm
    """
    event, values = sg.Window('WTC-LMS GUI edit the comment',
                    layout=[[sg.Text('Comment'), sg.InputText('',
                    tooltip='Check to see commands for UUid',
                    key='-COMMENT-INPUT-')], [sg.Button('Submit'),
                    sg.Button('Cancel')]],location=(500, 300)).read(close=True)

    if event == 'Submit':
        commentReviewProcess = core.lmsCall(["wtc-lms","edit_comment",
        probelmUUID, values['-COMMENT-INPUT-']])
        (out, err) = core.systemCallComms(commentReviewProcess)
        reviews.reviewHandeler.reviewDetailsPopup(probelmUUID)

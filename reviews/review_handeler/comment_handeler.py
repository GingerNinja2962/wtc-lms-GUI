import PySimpleGUI as sg

import reviews
import core


def comment_handeler(probelm_uuid, window):
    """
    check wether to add a comment or edit one

    :param probelm_uuid: the UUID for the probelm
    :param window: this is the window that holds all elements
    """
    comment_review_process = core.lms_call(["wtc-lms","review_details", probelm_uuid])
    greped_comment_process = core.grep_system_call("-i","edit_comment", comment_review_process)
    core.system_call_close(comment_review_process)
    (grade_review_data, err) = core.system_call_comms(greped_comment_process)

    print(grade_review_data)

    if grade_review_data != "":
        edit_or_del_comment(probelm_uuid)

    else:
        add_new_comment(probelm_uuid)

    reviews.review_handeler.review_details(probelm_uuid, window)


def add_new_comment(probelm_uuid):
    """
    handels the adding of new comments

    :param probelm_uuid: the UUID for the probelm
    """
    event, values = sg.Window('WTC-LMS GUI add a comment',
                    [[sg.Text('Comment'), sg.InputText('',
                    tooltip='Check to see commands for UUid',
                    key='-COMMENT-INPUT-')], [sg.Button('Submit'),
                    sg.Button('Cancel')]],
                    location=(500,300)).read(close=True)

    if event == 'Submit':
        comment_review_process = core.lms_call(["wtc-lms","add_comment",
        probelm_uuid, values['-COMMENT-INPUT-']])
        (grade_review_data, err) = core.system_call_comms(comment_review_process)


def edit_or_del_comment(probelm_uuid):
    """
    handels the editing or deleting of coments

    :param probelm_uuid: the UUID for the probelm
    """
    event, values = sg.Window('WTC-LMS GUI edit the comment',
                    layout=[[sg.Text('Comment'), sg.InputText('',
                    tooltip='Check to see commands for UUid',
                    key='-COMMENT-INPUT-')], [sg.Button('Submit'),
                    sg.Button('Cancel')]],location=(500, 300)).read(close=True)

    if event == 'Submit':
        comment_review_process = core.lms_call(["wtc-lms","edit_comment",
        probelm_uuid, values['-COMMENT-INPUT-']])
        (grade_review_data, err) = core.system_call_comms(comment_review_process)

from pathlib import Path

import os

import reviews
import core


def get_new_topic_data(topic_uuid, save_file):
    """
    a simple function to return new topic data and store it

    :param topic_uuid: this is the uuid for the selected topic
    :param save_file: this is the file location to save the data to
    :return lms_topic_data: this data returned from the lms topics process call
    """
    lms_topics = core.lms_call(["wtc-lms","topics", topic_uuid])
    lms_topics_grep = core.grep_system_call("-iA3", "]", lms_topics)
    core.system_call_close(lms_topics)
    (lms_topics_data, err) = core.system_call_comms(lms_topics_grep)
    core.write_to_file(lms_topics_data, save_file)
    reviews.token_handeler.force_time_update()
    return lms_topics_data


def get_old_topic_data(save_file):
    """
    a simple function to get old topic data from a file

    :param save_file: this is the file location to save the data to
    :return lms_topic_data: this data returned from the read file
    """
    lms_topics_grep = core.grep_call("-iA3", "]", save_file)
    (lms_topics_data, err) = core.system_call_comms(lms_topics_grep)
    return lms_topics_data


def topics_listbox_contents(topic_uuid, window):
    """
    a simple function to check whether new data needs to be loaded or not

    :param topic_uuid: this is the uuid for the module holding the topics
    :param window: this is the window containing the elements to be updated
    :return problems_uuid_link: a dictionary linking the problem uuids to topics
    """
    save_path = f"{Path.home()}/bin/lms_GUI/problems_data/topics_data"
    save_file = f".{topic_uuid}topics.txt"

    if not os.path.isdir(save_path):
        os.mkdir(save_path)
        lms_topics_data = get_new_topic_data(topic_uuid, f"{save_path}/{save_file}")

    elif os.path.isfile(f"{save_path}/{save_file}") and not reviews.token_handeler.time_check():
        lms_topics_data = get_old_topic_data(f"{save_path}/{save_file}")

    else:
        lms_topics_data = get_new_topic_data(topic_uuid, f"{save_path}/{save_file}")

    lms_topics_data = lms_topics_data.replace("(", "\n")
    lms_topics_data = lms_topics_data.replace(")", "\n")
    lms_topics_data = lms_topics_data.split('\n')
    for item in lms_topics_data:
        if item == '': lms_topics_data.remove('')

    topics_uuid_link = {}
    for index, item in enumerate(lms_topics_data[0::4]):
        if item == '':
            continue
        topics_uuid_link[item] = lms_topics_data[(index*4)+1]

    window.FindElement('-TOPIC-').Update(
        values=[item for item in topics_uuid_link.keys() if item != ''])
    return topics_uuid_link

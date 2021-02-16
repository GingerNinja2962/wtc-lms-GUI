import os

import core


def populate_topics():
    """
    download all topics data and saves it
    """
    save_data_path = (f"{os.getcwd()}/.save_data")
    topics_data_path = core.dir_check(save_data_path + "/data_topics")

    if not os.path.exists(save_data_path + "/data_modules/.modules.txt"):
        core.populate_save_data.populate_modules()

    grep_modules_call = core.grep_call("-i", " \[", save_data_path + "/data_modules/.modules.txt")
    (lms_topics_data, err) = core.system_call_comms(grep_modules_call)

    lms_topics_data = lms_topics_data.split("\n")
    new_topics_data = {}

    for string in lms_topics_data:
        string = string.replace(')', '')
        string = string.split(" (")
        if string != ['']:
            new_topics_data[string[1]] = string[0]

    for topic_uuid in new_topics_data.keys():
        lms_topic_call = core.lms_call(["wtc-lms", "topics", topic_uuid])
        (lms_topics_data, err) = core.system_call_comms(lms_topic_call)

        core.write_to_file(lms_topics_data,
            topics_data_path + f"/{new_topics_data[topic_uuid]}.txt")

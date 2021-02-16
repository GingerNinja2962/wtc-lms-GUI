import os

import core


def populate_problems():
    """
    download all problems data and saves it
    """
    save_data_path = (f"{os.getcwd()}/.save_data")
    problems_data_path = core.dir_check(save_data_path + "/data_problems") 

    if not os.path.exists(save_data_path + "/data_topics"):
        core.populate_save_data.populate_topics()

    for topic_file in os.listdir(save_data_path + "/data_topics"):

        grep_topics_call = core.grep_call("-i", " \[",
                save_data_path + f"/data_topics/{topic_file}")
        (lms_problems_data, err) = core.system_call_comms(grep_topics_call)

        lms_problems_data = lms_problems_data.split("\n")
        new_problems_data = {}

        for string in lms_problems_data:
            string = string.replace(')', '')
            string = string.split(" (")
            if string != ['']:
                new_problems_data[string[1]] = string[0]

        for problem_uuid in new_problems_data.keys():
            lms_problem_call = core.lms_call(["wtc-lms", "problems", problem_uuid])
            (lms_problems_data, err) = core.system_call_comms(lms_problem_call)

            core.write_to_file(lms_problems_data,
                problems_data_path + f"/{new_problems_data[problem_uuid]}.txt")


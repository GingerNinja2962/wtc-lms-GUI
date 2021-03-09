from datetime import timedelta, datetime

import os

import core


def force_token_update(token_type):
    """
    force the saved time token to be updated

    :param token_type: the type of token to be updated
            e.g. 'assignment', 'review' or 'login'
    """
    save_data_path = core.dir_check(f"{os.getcwd()}/.save_data")
    save_data_path = core.dir_check(f"{save_data_path}/tokens")

    if token_type == "assignment":
        save_data_path = save_data_path + "/.token_assignment.txt"
    elif token_type == "review":
        save_data_path = save_data_path + "/.token_review.txt"
    else:
         save_data_path = save_data_path + "/.token_login.txt"

    current_time = datetime.now()
    core.write_to_file(datetime.strftime(current_time,
            "%Y-%m-%d %H:%M:%S"), save_data_path)


def token_check(token_type):
    """
    checks the current time and compares it against
            the saved time token

    :param token_type: the type of token to be updated
    :return boollean: true if the token expired and
            false if the token is valid 
    """
    save_data_path = core.dir_check(f"{os.getcwd()}/.save_data")
    save_data_path = core.dir_check(f"{save_data_path}/tokens")

    if token_type == "assignment":
        save_data_path = save_data_path + "/.token_assignment.txt"
    elif token_type == "review":
        save_data_path = save_data_path + "/.token_review.txt"
    else:
         save_data_path = save_data_path + "/.token_login.txt"

    if os.path.isfile(save_data_path):
        time_check_token = core.read_from_file(save_data_path)

        try:
            time_check_token = datetime.strptime(
                    time_check_token, "%Y-%m-%d %H:%M:%S")
        except:
            current_time = datetime.now()
            core.write_to_file(datetime.strftime(current_time,
                    "%Y-%m-%d %H:%M:%S"), save_data_path)
            return True

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if token_type == "login":
            if (time_check_token + timedelta(hours=4)) < datetime.strptime(
                                            current_time, "%Y-%m-%d %H:%M:%S"):
                core.write_to_file(current_time, save_data_path)
                return True

        elif token_type == "review":
            if (time_check_token + timedelta(minutes=5)) < datetime.strptime(
                                            current_time, "%Y-%m-%d %H:%M:%S"):
                core.write_to_file(current_time, save_data_path)
                return True

        elif token_type == "assignment":
            if (time_check_token + timedelta(days=7)) < datetime.strptime(
                                            current_time, "%Y-%m-%d %H:%M:%S"):
                core.write_to_file(current_time, save_data_path)
                return True
        return False

    current_time = datetime.now()
    core.write_to_file(datetime.strftime(current_time,
            "%Y-%m-%d %H:%M:%S"), save_data_path)
    return True

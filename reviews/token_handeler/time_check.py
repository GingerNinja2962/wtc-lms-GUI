from datetime import timedelta
from datetime import datetime
from pathlib import Path

import reviews
import core
import os


def force_time_update():
    """
    a small function to force a the saved time token to be updated
    """
    time_check_file = f"{Path.home()}/bin/lms_GUI/problems_data/.time_check_token.txt"
    current_time = datetime.now()
    core.write_to_file(datetime.strftime(current_time, "%Y-%m-%d %H:%M:%S"), time_check_file)


def time_check():
    """
    small function that checks the current time to the saved time token

    :return boollean: true if the toke expired and false if the token is valid 
    """
    time_check_file = f"{Path.home()}/bin/lms_GUI/problems_data/.time_check_token.txt"

    if os.path.isfile(time_check_file):
        time_check_token = core.read_from_file(time_check_file)

        try:
            time_check_token = datetime.strptime(time_check_token, "%Y-%m-%d %H:%M:%S")
        except:
            current_time = datetime.now()
            reviews.write_to_file(datetime.strftime(current_time, "%Y-%m-%d %H:%M:%S"), time_check_file)
            return True

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if (time_check_token + timedelta(minutes=5)) < datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S"):
            core.write_to_file(current_time, time_check_file)
            return True

        return False

    current_time = datetime.now()
    core.write_to_file(datetime.strftime(current_time, "%Y-%m-%d %H:%M:%S"), time_check_file)
    return True

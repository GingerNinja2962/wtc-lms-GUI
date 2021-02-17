import core
import os


def populate_save_data(prefered_data="ALL"):
    """
    check tokens and updates the reviews, 
    modules, topics, problems and assignments data accordingly

    :param prefered_data: the data to be populated e.g. 'assignments'
            or 'reviews', default if BOTH
    """
    save_data_path = f"{os.getcwd()}/.save_data"

    if not os.path.exists(save_data_path):
        os.mkdir( save_data_path )

        if prefered_data == "assignment":
            core.populate_save_data.populate_problems()
        elif prefered_data == "reviews":
            core.populate_save_data.populate_reviews()
        else:
            core.populate_save_data.populate_problems()
            core.populate_save_data.populate_reviews()
        return

    if prefered_data == "assignment":
        if core.token_check("assignment"):
            core.populate_save_data.populate_problems()
    elif prefered_data == "reviews":
        if core.token_check("review"):
            core.populate_save_data.populate_reviews()
    else:
        if (core.token_check("assignment")
        or not os.path.exists(save_data_path + "/data_modules")
        or not os.path.exists(save_data_path + "/data_topics")
        or not os.path.exists(save_data_path + "/data_problems")):
            core.populate_save_data.populate_problems()

        if (core.token_check("review")
        or not os.path.exists(save_data_path + "/data_reviews")):
            core.populate_save_data.populate_reviews()

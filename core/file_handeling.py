
def write_to_file(content, file_path):
    """
    simple function to write to file

    :param content: this is the message to be written
    :param file_path: this is the path to the file to be written to
    """
    with open(file_path, "w") as time_check_file:
        time_check_file.write(content)


def read_from_file(file_path):
    """
    simple function to read from a file

    :param file_path: this is the path to the file to be read from
    :return content: this is the contents of the read file
    """
    with open(file_path, "r") as time_check_file:
        content = time_check_file.read()
    return content

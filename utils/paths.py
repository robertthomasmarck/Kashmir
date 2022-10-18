import os


def get_path(file):
    path = os.path.realpath("./" + file)
    return path

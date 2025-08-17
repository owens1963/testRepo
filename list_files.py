import os


def list_files(directory):
    return os.listdir(directory)


print(list_files("."))

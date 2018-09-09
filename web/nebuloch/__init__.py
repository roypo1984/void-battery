import os


def datapath(filename):
    return os.path.join(
        os.path.abspath(os.path.dirname(__file__)), 'data', filename)


with open(datapath('version.txt')) as file:
    version = file.read()
del file

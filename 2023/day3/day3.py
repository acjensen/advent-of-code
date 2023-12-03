import os


def read_input_lines(filename):
    anchor = os.path.dirname(__file__)
    f = open(os.path.join(anchor, filename))
    lines = f.readlines()
    f.close()
    return lines

# This is a work in progress

import os

# Get the input data filepath.
input_filepath = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "input.txt")


def load_seats(filepath) -> str:
    with open(filepath, "r") as f:
        return [line for line in f.readlines()]


# Load the seats.
seats = load_seats(input_filepath)
print(seats)

import os
import re
from typing import NamedTuple

# Load the input file into memory.
filepath = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "input.txt")

# Transform the input file into a list of lists
class Map():
    def __init__(self):
        self.matrix = []
        with open(filepath, "r") as input:
            for line in input:
                self.matrix.append(list(line))
        if not matrix:
            raise Exception("The map did not load correctly")
        self.height = len(matrix[0])
        self.width = len(matrix[0][0])

class Position():
    def __init__(self):
        self.horizontal = 0
        self.vertical = 0

    def move_down(num_steps: int)
        self.vertical += num_steps

    def move_left(num_steps: int)
        self.horizontal -= num_steps

    def move_right(num_steps: int)
        self.horizontal += num_steps

class Game:
    def __init__(self, map: Map, pos: Position):
        self.map = map
        self.pos = pos

    def run(self, move_func):


def part_1():

    def right_3_down_1(pos: Position):
        pos.move_right(3)
        pos.move_down(1)

    map = Map()
    pos = Position()
    Game(map, pos)

    Game.run(right_3_down_1)

    while pos.vertical < map.height:
        if pos.horizontal > 
        right_3_down_1(p)


# Load the input file and count the number of valid passwords.
part_1_result = PasswordLoader(filepath).num_valid_passwords()
print(part_1_result)
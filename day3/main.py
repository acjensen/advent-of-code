import os
import re
from typing import NamedTuple, Callable


# Transform the input file into a list of lists
class Map():
    '''
    Store a 2D map of the slope. '#' is a tree, and '.' is no tree.

    The map repeats itself horizontally. 
    '''

    def __init__(self, filepath):
        # Load the map into a list of lists
        self.matrix = []
        with open(filepath, "r") as input:
            for line in input:
                self.matrix.append(list(line))
        if not self.matrix:
            raise Exception("The map did not load correctly")
        self.height = len(self.matrix)
        self.width = len(self.matrix[0])

    def __getitem__(self, tup: tuple):
        vertical = tup[0]
        horizontal = tup[1] % (self.width-1)  # map repeats horizontally
        return self.matrix[vertical][horizontal]

    def __repr__(self):
        return str(self.matrix)


class Position():
    '''
    Store the 2D position of the toboggan on the map and provide methods to move it.
    '''

    def __init__(self):
        self.vertical = 0
        self.horizontal = 0

    def move_down(self, num_steps: int):
        self.vertical += num_steps

    def move_left(self, num_steps: int):
        self.horizontal -= num_steps

    def move_right(self, num_steps: int):
        self.horizontal += num_steps

    def __repr__(self):
        return str((self.vertical, self.horizontal))


class Game():
    '''
    Run the game and count how many trees are hit as the toboggan travels down the slope.
    '''

    def __init__(self, map: Map, position: Position = None):
        self.map = map
        if position:
            self.position = position
        else:
            self.position = Position()

    def run(self, move_position: Callable):
        # Run the game according to the move function. Return the number of trees hit.
        tree_count = 0
        while (self.position.vertical < self.map.height):
            if self.map[self.position.vertical, self.position.horizontal] == '#':
                tree_count += 1
            move_position(self.position)
        return tree_count


# Get the input data filepath.
filepath = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "input.txt")

# Set up the map.
map = Map(filepath)


def part_1():

    # Define how the toboggan will go down the slope.
    def right_3_down_1(position: Position):
        position.move_right(3)
        position.move_down(1)

    # Start a new game.
    game = Game(map)

    # Run the game.
    return game.run(right_3_down_1)


def part_2():
    # Run the game with 5 different toboggan movements.

    moves = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    answer = 1
    for move in moves:

        # Start a new game.
        game = Game(map)

        # Define new movement function.
        def move_position(position: Position):
            position.move_right(move[0])
            position.move_down(move[1])

        answer = answer*game.run(move_position)

    return answer


print(part_1())
print(part_2())

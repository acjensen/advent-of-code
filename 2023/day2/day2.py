import os
from collections import defaultdict
import math


def read_input_lines(filename):
    anchor = os.path.dirname(__file__)
    f = open(os.path.join(anchor, filename))
    lines = f.readlines()
    f.close()
    return lines


for _input in ["input_example", "input"]:

    lines = read_input_lines(_input)

    def parse():
        dd = []

        for line in lines:
            d = []
            for picks in line.strip().split(':')[1].split(';'):
                _round = dict()
                for pick in picks.split(','):
                    stuff = pick.strip().split(' ')
                    _round[stuff[1]] = stuff[0]
                d.append(_round)
            dd.append(d)

        return dd

    dd = parse()

    def part_1():

        limits = {"red": 12, "green": 13, "blue": 14}

        result = 0

        for idx, game in enumerate(dd):
            good = True
            for _round in game:
                for color, count in _round.items():
                    if int(count) > limits[color]:
                        good = False
            if good:
                # print(idx + 1)
                result += idx + 1

        print("part 1", _input, result)

    def part_2():
        result = 0
        for idx, game in enumerate(dd):
            round_max = defaultdict(int)
            for _round in game:
                for color, count in _round.items():
                    round_max[color] = max(round_max[color], int(count))
            result += math.prod(round_max.values())

        print("part 2", _input, result)

    part_1()
    part_2()

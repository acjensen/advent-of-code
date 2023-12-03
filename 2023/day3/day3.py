import os
from dataclasses import dataclass, field
from collections import defaultdict
import math
import uuid


def read_input_lines(filename):
    anchor = os.path.dirname(__file__)
    f = open(os.path.join(anchor, filename))
    lines = [l.strip() for l in f.readlines()]
    f.close()
    return lines


for _input in ["input_example", "input"]:
    lines = read_input_lines(_input)
    width = len(lines[0])
    height = len(lines)

    @dataclass
    class CurrentNumber:
        is_part_number: bool = False
        number: str = ""
        gears: set = field(default_factory=set)

    def part_1_and_2():
        result_1 = 0
        gears = defaultdict(set)

        current_number = None
        for j, line in enumerate(lines):
            for i, c in enumerate(line):
                if c.isdigit():
                    if not current_number:
                        current_number = CurrentNumber()

                    current_number.number += c

                    def is_symbol_nearby():
                        for x, y in [
                                (-1, -1), (-1, 1), (1, 1), (1, -1), (0, 1), (1, 0), (-1, 0), (0, -1)]:
                            if i + x < width and j + y < height and i + x >= 0 and j + y >= 0:
                                char = lines[j + y][i + x]
                                if char == '*':
                                    current_number.gears.add((j + y, i + x))
                                if char != '.' and not char.isdigit():
                                    return True

                        return False

                    if is_symbol_nearby():
                        current_number.is_part_number = True

                if not c.isdigit() or i == width - 1:
                    if current_number:
                        if current_number.is_part_number:
                            result_1 += int(current_number.number)
                        for gear in current_number.gears:
                            gears[gear].add(
                                (uuid.uuid4(), current_number.number))
                        current_number = None

        result_2 = 0
        for gear, part_numbers in gears.items():
            if len(part_numbers) == 2:
                result_2 += math.prod([int(pn) for _, pn in part_numbers])

        print("part1:", _input, result_1)
        print("part2:", _input, result_2)

    part_1_and_2()

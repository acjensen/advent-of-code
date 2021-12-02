from typing import *
from os import path

with open(path.join(path.dirname(__file__), 'input.txt')) as f:
    _input = [int(n) for n in f.readlines()]

def count_increasing(winsize: int):
    count = 0
    for i in range(winsize, len(_input)):
        if _input[i] > _input[i-winsize]:
            count += 1
    return count

def part1():
    return count_increasing(winsize=1)

def part2():
    return count_increasing(winsize=3)

print(part1()) # 1564
print(part2()) # 1611
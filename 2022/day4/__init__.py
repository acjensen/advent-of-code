#!python3

from dataclasses import dataclass

@dataclass
class Range:
    min: int
    max: int

@dataclass
class Pair:
    first: Range
    second: Range

def _count(input_txt, criteria):
    count = 0
    lines = open(input_txt).read().splitlines()
    pairs = [Pair(*[Range(*range.split('-')) for range in line.split(',')]) for line in lines]
    for pair in pairs:
        if criteria(pair):
            count += 1
    return count

def part1(input_txt):
    def criteria(p: Pair):
        return (p.first.min >= p.second.min and p.first.max <= p.second.max) \
            or (p.first.min <= p.second.min and p.first.max >= p.second.max)
    return _count(input_txt, criteria)

def part2(input_txt):
    def criteria(p: Pair):
        return not (p.first.min > p.second.max or p.second.min > p.first.max)
    return _count(input_txt, criteria)

print('part1 example:', part1("2022/day4/example_input.txt"))
print('part1 answer', part1("2022/day4/input.txt"))
print('part2 example', part2("2022/day4/example_input.txt"))
print('part2 answer', part2("2022/day4/input.txt"))


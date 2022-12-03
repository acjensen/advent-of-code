#!python3

def part1(input_txt):
    elves = parse(input_txt)
    return sorted(map(sum, elves))[-1]

def part2(input_txt):
    elves = parse(input_txt)
    return sum(sorted(map(sum, elves))[-3:])

def parse(input_txt):
    elves = []
    calories = []
    for line in open(input_txt).read().splitlines():
        if line == '':
            elves.append(calories)
            calories = []
        else:
            calories.append(int(line))
    return elves

print('part1:', part1("2022/day1/example_input.txt"))
print('part1:', part1("2022/day1/input.txt"))
print('part2:', part2("2022/day1/example_input.txt"))
print('part2:', part2("2022/day1/input.txt"))
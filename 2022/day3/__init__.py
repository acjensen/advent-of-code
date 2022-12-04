#!python3

def value(item):
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38

def part1(input_txt):

    def parse(input_txt):
        return [
            (set(line[0:len(line)//2]), set(line[len(line)//2:len(line)]))
                for line in open(input_txt).read().splitlines()
        ]

    score = 0
    for rucksack_left, rucksack_right in parse(input_txt):
        common_item = rucksack_left.intersection(rucksack_right).pop()
        score += value(common_item)
    return score

def part2(input_txt):

    rucksacks = [set(line) for line in open(input_txt).read().splitlines()]
    score = 0
    i = 1
    buffer = rucksacks.pop()
    while rucksacks:
        if i % 3 != 0:
            buffer = buffer.intersection(rucksacks.pop())
        else:
            score += value(buffer.pop())
            buffer = rucksacks.pop()
        i += 1
    return score + value(buffer.pop())

assert(part1("2022/day3/example_input.txt") == 157)
print('part1:', part1("2022/day3/input.txt"))
assert(part2("2022/day3/example_input.txt") == 70)
print('part2:', part2("2022/day3/input.txt"))
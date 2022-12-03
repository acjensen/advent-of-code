#!python3

def part1(input_txt):
    max = 0
    s = 0
    for line in open(input_txt).readlines():
        if line == '\n' or line == '':
            if s > max:
                max = s
            s = 0
        else:
            s += int(line)
    return max

def part2(input_txt):
    sums = []
    s = 0

    for line in open(input_txt).readlines():
        if line == '\n' or line == '':
            sums.append(s)
            s = 0
        else:
            s += int(line)

    sums.sort()
    return sum(sums[-3:])

print('part1:', part1("2022/day1/example_input.txt"))
print('part1:', part1("2022/day1/input.txt"))

print('part2:', part2("2022/day1/example_input.txt"))
print('part2:', part2("2022/day1/input.txt"))
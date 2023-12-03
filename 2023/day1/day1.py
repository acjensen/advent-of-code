import os


def read_input_lines(filename):
    anchor = os.path.dirname(__file__)
    f = open(os.path.join(anchor, filename))
    lines = f.readlines()
    f.close()
    return lines


def part_1():
    _sum = 0

    for line in read_input_lines('input'):
        digits = [c for c in line if c.isdigit()]
        s = digits[0] + digits[-1]
        _sum += int(s)

    result = str(_sum)

    assert result == read_input_lines('part_1_answer')[0]


def part_2():
    lines = read_input_lines('input')

    digits = {"one": "1",
              "two": "2",
              "three": "3",
              "four": "4",
              "five": "5",
              "six": "6",
              "seven": "7",
              "eight": "8",
              "nine": "9"}

    def reverse_map(m):
        return {k[::-1]: v for k, v in m.items()}

    def first_digit(line, digits):
        buffer = ''
        for c in line.strip():
            buffer += c
            for k, v in digits.items():
                if k in buffer:
                    return v
            if c.isdigit():
                return c

    result = sum([int(first_digit(line, digits) + first_digit(line[::-1], reverse_map(digits)))
                  for line in lines])

    assert str(result) == read_input_lines('part_2_answer')[0]


part_1()
part_2()

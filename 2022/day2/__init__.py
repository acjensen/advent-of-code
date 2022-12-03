#!python3

shape_score = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

draw = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}

def part1(rounds):
    
    i_win = {
        ('A', 'Y'),
        ('B', 'Z'),
        ('C', 'X'),
    }

    total_score = 0
    for round in rounds:
        opponent_shape, my_shape = round
        round_score = 0
        if draw[opponent_shape] == my_shape:
            round_score += 3
        elif round in i_win:
            round_score += 6
        total_score += round_score + shape_score[my_shape]
    return total_score

def part2(rounds):

    i_win = {
        'A': 'Y',
        'B': 'Z',
        'C': 'X',
    }

    i_lose = {
        'A': 'Z',
        'B': 'X',
        'C': 'Y',
    }

    strategy = {
        'Y': (3, draw),
        'X': (0, i_lose),
        'Z': (6, i_win),
    }

    total_score = 0
    for opponent_shape, outcome in rounds:
        round_score, action = strategy[outcome]
        total_score += round_score + shape_score[action[opponent_shape]]
    return total_score

def parse(input_txt):
    return [tuple(line.split(' ')) for line in open(input_txt).read().splitlines()]

print('part1:', part1(parse("2022/day2/example_input.txt")))
print('part1:', part1(parse("2022/day2/input.txt")))
print('part2:', part2(parse("2022/day2/example_input.txt")))
print('part2:', part2(parse("2022/day2/input.txt")))
import os
from collections import deque

def parse(txt_file):
    filename = os.path.join(os.path.dirname(__file__), txt_file)
    f = open(filename)
    input = [[int(c) for c in l if c != '\n'] for l in f.readlines()]
    height = len(input)
    width = len(input[0])
    f.close()
    return input, height, width


def main(txt_file, num_steps, is_part_2):

    b, height, width = parse(txt_file)

    def adjacent(pair):
        result = []
        for p in [
            (-1, -1), (0, -1), (1, -1),
            (-1, 0 ), (1, 0 ),
            (-1, 1 ), (0, 1 ), (1, 1),
        ]:
            new_p = (pair[0] + p[0], pair[1] + p[1])
            px = new_p[0]
            py = new_p[1]
            if px >= 0 and px < width and py >= 0 and py < height:
                result.append(new_p)
        return result
        
    
    def step(b):

        stack = deque()
        flashed = set()

        for x, l in enumerate(b):
            for y, o in enumerate(l):
                stack.append((x, y))
    
        while stack:
            pair = stack.popleft()
            x, y = pair
            b[x][y] += 1
            if b[x][y] > 9 and pair not in flashed:
                stack += [p for p in adjacent(pair) if p not in flashed]
                flashed.add(pair)

        for f in flashed:
            x, y = f
            b[x][y] = 0

        num_flashed = len(flashed)
        return num_flashed

    def part1(num_steps):
        flash_count = 0
        for _ in range(num_steps):
            flash_count += step(b)
        return flash_count

    def part2(num_steps):

        def all_flashed(b):
            for x in range(width):
                for y in range(height): 
                    if b[x][y] != 0:
                        return False 
            return True

        for step_idx in range(num_steps):
            step(b)
            if all_flashed(b):
                return step_idx + 1

        return None


    if is_part_2:
        print(part2(num_steps))
    else:
        print(part1(num_steps))

for input_txt, num_steps, is_part_2 in [ 
    ('test_input.txt', 100, False),
    ('test_input_2.txt', 2, False),
    ('input.txt', 100, False),
    ('test_input.txt', 1000000, True),
    ('input.txt', 10000000, True),
]:
    main(input_txt, num_steps, is_part_2)
import os
from collections import deque

def parse(txt_file):
    filename = os.path.join(os.path.dirname(__file__), txt_file)
    f = open(filename)
    matrix = [[int(c) for c in l if c != '\n'] for l in f.readlines()]
    height = len(matrix)
    width = len(matrix[0])
    f.close()
    return matrix, height, width


def adjacent(coord, width, height):
    result = []
    for offset in [
        (-1, -1), (0, -1), (1, -1),
        (-1,  0),          (1,  0),
        (-1,  1), (0,  1), (1,  1),
    ]:
        x, y = adj_coord = (coord[0] + offset[0], coord[1] + offset[1])
        if x >= 0 and x < width and y >= 0 and y < height:
            result.append(adj_coord)
    return result


def solve(txt_file, num_steps, is_part_2):

    m, height, width = parse(txt_file)

    def step(m):

        stack = [] 
        flashed = set()

        for x in range(width):
            for y in range(height):
                stack.append((x, y))
    
        while stack:
            coord = stack.pop()
            x, y = coord
            m[x][y] += 1
            if m[x][y] > 9 and coord not in flashed:
                stack += [c for c in adjacent(coord, width, height) if c not in flashed]
                flashed.add(coord)

        for (x, y) in flashed:
            m[x][y] = 0

        return len(flashed) 


    def part1():

        flash_count = 0
        for _ in range(num_steps):
            flash_count += step(m)
        return flash_count


    def part2():

        def all_flashed(m):
            for x in range(width):
                for y in range(height): 
                    if m[x][y] != 0:
                        return False 
            return True

        for step_idx in range(num_steps):
            step(m)
            if all_flashed(m):
                return step_idx + 1

        return None

    if is_part_2:
        print(part2())
    else:
        print(part1())

for input_txt, num_steps, is_part_2 in [ 
    ('test_input.txt', 100, False),
    ('test_input_2.txt', 2, False),
    ('input.txt', 100, False),
    ('test_input.txt', 1000000, True),
    ('input.txt', 10000000, True),
]:
    solve(input_txt, num_steps, is_part_2)
#!python3

from dataclasses import dataclass
from collections import deque


@dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclass(frozen=True)
class State:
    point: Point
    count: int


def solve(input_txt):

    with open(input_txt) as f:
        heightmap = f.read().splitlines()

    x_lim = len(heightmap)
    y_lim = len(heightmap[0])

    def adjacent(x, y):
        return [(xx, yy) for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if xx >= 0 and xx < x_lim and yy >= 0 and yy < y_lim]

    def height_of(x, y):
        letter = heightmap[x][y]
        if letter == 'S':
            return ord('a')
        if letter == 'E':
            return ord('z')
        return ord(letter)

    def find_letter(letter):
        for line_number, line in enumerate(heightmap):
            if letter in line:
                return Point(line_number, line.index(letter))

    def bfs(start, stopping_criteria, get_next_moves):
        visited = set()
        queue = deque()
        queue.append(State(start, 0))
        count: int = None
        while queue:
            state = queue.pop()
            if stopping_criteria(state.point):
                count = state.count
                break
            if state.point in visited:
                continue
            visited.add(state.point)
            for s in [State(next_move, state.count+1) for next_move in get_next_moves(state.point.x, state.point.y)]:
                queue.appendleft(s)
        return count
    
    def part1():
        return bfs(
            start=find_letter('S'),
            stopping_criteria=lambda point: point == find_letter('E'),
            get_next_moves=lambda x, y: [Point(xx, yy) for xx, yy in adjacent(x, y) if height_of(xx, yy) <= height_of(x, y) + 1]
        )

    def part2():
        return bfs(
            start=find_letter('E'),
            stopping_criteria=lambda point: height_of(point.x, point.y) == ord('a'),
            get_next_moves=lambda x, y: [Point(xx, yy) for xx, yy in adjacent(x, y) if height_of(xx, yy) >= height_of(x, y) - 1]
        )
    
    print(input_txt, '|', 'part1', '|', part1())
    print(input_txt, '|', 'part2', '|', part2())

solve('2022/day12/example_input.txt')
solve('2022/day12/input.txt')

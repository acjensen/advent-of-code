#!python3

from ast import literal_eval
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

def parse(input_txt):
    with open(input_txt) as f:
        lines = f.read().splitlines()
    result = []
    for line in lines:
        line = line.replace("Sensor at x=", "(")
        line = line.replace(", y=", ",")
        line = line.replace(": closest beacon is at x=", "),(")
        line = line.replace(", y=", ",")
        line += ")"
        line = literal_eval(line)
        result.append((Point(*line[0]), Point(*line[1])))
    return result

def manhattan_distance(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)

def count_overlapping(ranges):
    # There's a smarter way to do this but I don't have time :)
    covered = set()
    for r in ranges:
        for i in range(r[0],r[1]):
            covered.add(i)
    return len(covered)

def part1(y=10):

    x_ranges_covered_at_y_line = []
    for line in parse("2022/day15/input.txt"):
        s, b = line
        md = manhattan_distance(s, b)
        if abs(s.y - y) < md: # Check if y is in range of the sensor.
            x_diff = md - abs(s.y - y)
            x_ranges_covered_at_y_line.append((s.x - x_diff, s.x + x_diff))

    return count_overlapping(x_ranges_covered_at_y_line)


def part2():

    # _max = 20
    # file = "2022/day15/example_input.txt"
    _max = 4000000
    file = "2022/day15/input.txt"

    def in_box(p: Point):
        return p.x >= 0 and p.x <= _max and p.y >= 0 and p.y <= _max

    def add_if_in_box(edge_points: set, p: Point):
        if in_box(p):
            edge_points.add(p)

    lines = parse(file)
    # only need to check just outside the range of each beacon!
    # in fact, it should be surrounded on all sides....
    edge_points = set()
    for line in lines:
        sensor, beacon = line
        md = manhattan_distance(sensor, beacon) + 1
        # if point in 0, 4000000:
        between = range(0, md + 1)
        points = set()
        for a, b in zip(between, reversed(between)):
            add_if_in_box(points, Point(sensor.x + a, sensor.y + b))
            add_if_in_box(points, Point(sensor.x - a, sensor.y + b))
            add_if_in_box(points, Point(sensor.x + a, sensor.y - b))
            add_if_in_box(points, Point(sensor.x - a, sensor.y - b))
            edge_points.update(points)
        # print()

    # print(edge_points)
    potential = edge_points.copy()
    for point in edge_points:
        for line in lines:
            s, b = line
            if manhattan_distance(s, point) <= manhattan_distance(s, b):
                if point == Point(14, 11):
                    print("???")
                if point in potential: potential.remove(point)

    print(potential)

        
part2()

# def part2():

#     x_max = 20
#     file = "2022/day15/example_input.txt"
#     # x_max = 4000000
#     # file = "2022/day15/input.txt"
    
#     lines = parse(file)
#     # 8000000 options
#     diagonal_range = []
#     for line in lines:
#         s, b = line
#         ss = manhattan_distance(Point(0, 0), s)
#         bb = manhattan_distance(s, b)
#         diagonal_range.append((max(0, ss - bb), min(x_max*2, ss + bb)))

#     for m in diagonal_range:
#         print(m)

#     return count_overlapping(diagonal_range)

# print(part2())






# def part2():

#     def count_overlapping(ranges):
#         # There's a smarter way to do this but I don't have time :)
#         covered = set()
#         for r in ranges:
#             for i in range(r[0],r[1]):
#                 covered.add(i)
#         return len(covered)

#     x_max = 20
#     file = "2022/day15/example_input.txt"
#     x_max = 4000000
#     file = "2022/day15/input.txt"

#     def part1(y=10):

#         x_ranges_covered_at_y_line = []
#         for line in parse(file):
#             s, b = line
#             md = manhattan_distance(s, b)
#             if abs(s.y - y) < md: # Check if y is in range of the sensor.
#                 x_diff = md - abs(s.y - y)
#                 x_ranges_covered_at_y_line.append((max(s.x - x_diff, 0), min(s.x + x_diff, x_max)))

#         return count_overlapping(x_ranges_covered_at_y_line)

#     min_ = 100000000000
#     ans = None
#     for y in range(0, x_max):
#         # print(part1(y))
#         asdf = part1(y)
#         if asdf < min_:
#             min_ = asdf
#             ans = y

#     return ans

    

# print(part2())
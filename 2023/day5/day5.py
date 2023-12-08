import os
from math import inf


def read_input_lines(filename):
    anchor = os.path.dirname(__file__)
    f = open(os.path.join(anchor, filename))
    lines = [l.strip() for l in f.readlines()]
    f.close()
    return lines


for _input in ["input_example", "input"]:

    def pt1():
        lines = read_input_lines(_input)

        seeds = [int(x) for x in lines[0].split(':')[1].strip().split()]

        def get_maps():
            # don't ask me to explain this
            def none_to_x(x):
                if not x:
                    return 'x'
                else:
                    return x
            return [[[int(asdf) for asdf in u.split()] for u in j] for j in [l.split('y') for l in 'y'.join([none_to_x(line) for line in lines[2:]
                                                                                                             if not line or not line[0].isalpha()]).split('yxy')]]

        maps = get_maps()

        def map_lookup(map, _input):
            for line in map:
                if _input >= line[1] and _input < line[1] + line[2]:
                    return _input - line[1] + line[0]
            return _input

        results = []
        for seed in seeds:
            for map in maps:
                seed = map_lookup(map, seed)
            results.append(seed)

        print(min(results))

    pt1()

    def pt2():

        lines = read_input_lines(_input)

        seeds = [int(x) for x in lines[0].split(':')[1].strip().split()]
        seeds = [seeds[i:i + 2] for i in range(0, len(seeds), 2)]

        def get_maps():
            # don't ask me to explain this
            def none_to_x(x):
                if not x:
                    return 'x'
                else:
                    return x
            maps = [[[int(asdf) for asdf in u.split()] for u in j] for j in [l.split('y') for l in 'y'.join([none_to_x(line) for line in lines[2:]
                                                                                                             if not line or not line[0].isalpha()]).split('yxy')]]
            return [sorted(map, key=lambda line: line[1]) for map in maps]

        maps = get_maps()

        def intersection(x, y, offset):
            res = max(x[0], y[0]), min(x[-1], y[-1])
            if res[0] < res[1]:
                return res[0] + offset, res[1] - res[0]
            return None

        intervals_in = seeds

        for map in maps:
            intervals_out = []
            for interval in intervals_in:
                s_a, s_b = interval[0], interval[0] + interval[1]
                i = intersection(
                    [s_a, s_b], [-inf, map[0][1]], 0)
                if i:
                    intervals_out.append(i)
                i = intersection(
                    [s_a, s_b], [map[-1][1] + map[-1][2], inf], 0)
                if i:
                    intervals_out.append(i)
                for line in map:
                    l_a, l_b = line[1], line[1] + line[2]
                    i = intersection([s_a, s_b], [l_a, l_b], line[0] - line[1])
                    if i:
                        intervals_out.append(i)
            intervals_in = intervals_out

        print(min([i[0] for i in intervals_in]))

    pt2()

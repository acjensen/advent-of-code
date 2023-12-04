import os
from functools import reduce
from math import factorial
from collections import defaultdict


def read_input_lines(filename):
    anchor = os.path.dirname(__file__)
    f = open(os.path.join(anchor, filename))
    lines = [l.strip() for l in f.readlines()]
    f.close()
    return lines


for _input in ["input_example", "input"]:
    lines = read_input_lines(_input)

    def pt1():
        result = 0
        for line in lines:
            left, right = line.split(':')[1].split('|')
            left = left.strip().split()
            right = right.strip().split()
            count = 0
            for r in right:
                if r in left:
                    count += 1
            if count > 0:
                result += 2**(count-1)
        print("pt1", _input, result) # 24706
    
    def pt2():
        result = 0
        d = defaultdict(int)
        for idx, line in enumerate(lines):
            left, right = line.split(':')[1].split('|')
            left = left.strip().split()
            right = right.strip().split()
            count = 0
            for r in right:
                if r in left:
                    count += 1
            for copy_idx in range(idx + 1, idx + 1 + count):
                if copy_idx < len(lines):
                    d[copy_idx] += (d[idx] + 1)
        result = len(lines) + sum(d.values())
        print("pt2", _input, result) # 13114317

    pt1()
    pt2()
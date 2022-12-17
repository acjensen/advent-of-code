#!python3

from dataclasses import dataclass
from ast import literal_eval


with open("2022/day13/example_input.txt") as f:
    lines = f.read().splitlines()

lines = [literal_eval(line) for line in lines if line]

def compare(first, second):
    f_idx = 0
    s_idx = 0
    while True:
        if type(first[f_idx]) == int and type(second[s_idx]) == int:
            if first[f_idx] == second[s_idx]:
                if f_idx == len(first)-1 and s_idx == len(second)-1:
                    if len(first) < len(second):
                        return True
                    elif len(second) < len(first):
                        return False
                    return "continue"
                if f_idx < len(first)-1:
                    f_idx += 1
                if s_idx < len(second)-1:
                    s_idx += 1
            elif first[f_idx] <= second[s_idx]:
                return True
            else:
                return False
        if type(first[f_idx]) == list or type(second[s_idx]) == list:
            result = compare(listIfNot(first[f_idx]), listIfNot(second[s_idx]))
            if result != "continue":
                return result
            if f_idx < len(first)-1:
                f_idx += 1
            if s_idx < len(first)-1:
                s_idx += 1

def listIfNot(x):
    if type(x) != list:
        return [x]
    return x

# print(compare(
#     first = [1,1,3,1,1],
#     second = [1,1,5,1,1],
# ))

# print(compare(
#     first = [[1],[2,3,4]],
#     second = [[1],4],
# ))

# print(compare(
#     first = [9],
#     second = [[8,7,6]],
# ))

# print(compare(
#     first = [[4,4],4,4],
#     second = [[4,4],4,4,4],
# ))

print(compare(
    first = [],
    second = [3],
))

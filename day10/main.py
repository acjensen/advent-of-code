import os
from collections import defaultdict

# Get the input data filepath.
input_filepath = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "input.txt")


def load_adapters(filepath) -> str:
    with open(filepath, "r") as f:
        return [int(line) for line in f.readlines()]


adapters = load_adapters(input_filepath)
adapters = sorted(adapters)
print(adapters)

differences = []


for i in range(len(adapters) - 1):
    differences.append(adapters[i+1]-adapters[i])

differences.append(adapters[0]-0)  # wall to adapter
differences.append(3)  # addapter to phone

print(differences)

num_of_1s = len([d for d in differences if d == 1])
num_of_3s = len([d for d in differences if d == 3])
print('Num 1s:', num_of_1s)
print('Num 3s:', num_of_3s)
print('Part 1:', num_of_1s*num_of_3s)

# Part 2.... What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?

last_i = len(adapters)

# idea: index/cache the numbers if already followed
# build adjacency list or matrix
# then you're just finding paths to the
# we know there is a path from every node already
# so...

# 1. sort list
# 2. count how many option to the next ones
# 3. multiply resulting array


# def get_compatible(i):
#     while (True):
#         if i == last_i:
#             # Connected to wall.
#             return True
#         diff = adapters[i+1] - adapters[i]
#         if diff < 3:
#             return get_compatible(i+1)
#         if diff == 3:
#             break
# 19208
things = []
n = 3
for i in range(len(adapters)):
    j = 1
    num_compatible = 0
    while True:
        if i + j > len(adapters)-1:
            break
        if adapters[i+j] - adapters[i] > n:
            break
        num_compatible += 1
        j += 1
    things.append(num_compatible)

print(things)

mults = []
for i, t in enumerate(things):
    m = 1
    for j in range(t):
        if things[i+j] == 0:
            break
        m *= things[i+j]
    mults.append(m)

print(mults)

things.pop()
answer = 1
for m in things:
    answer *= m
print(answer)


# This is a Directed Acyclic Graph (DAG).
# We'll perform the following algorithm:
# 0. Topologically sort the graph (already done).
# 1. scan the vertices from the target backwards to the source.
# 2. For each vertex v, keep a count of the number of paths from v to the target.
# 3. When you get to the source, the value of that count is the answer.
# Complexity is O(V+E).
n = 3
adjacency_list = []
for i in range(len(adapters)):
    j = 1
    adjacency = []
    while True:
        if i + j > len(adapters)-1:
            break
        if adapters[i+j] - adapters[i] > n:
            break
        adjacency.append(i+j)
        j += 1
    adjacency_list.append(adjacency)

print(adjacency_list)


def default_value():
    return []


# reverse the adjacency list
reverse_adjacency_list = defaultdict(default_value)
for u in range(len(adjacency_list)):
    for v in adjacency_list[u]:
        reverse_adjacency_list[v].append(u)


# find all paths on the DAG from 1 to 30
# if visited, just stop and add 1 to counter
visited = [0]*len(adjacency_list)
n_target = len(adjacency_list)
n_start = 30


def dfs(n, visited):
    visited[n] += 1
    for m in reverse_adjacency_list[n]:
        if m == n_target:
            visited[m] += 1
        if visited[m]:
            # count += 1
            visited[m] += 1
        else:
            dfs(m, visited)


dfs(30, visited)
print(visited)

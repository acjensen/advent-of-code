import os
from collections import defaultdict

# Get the input data filepath.
input_filepath = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "input.txt")


def load_adapters(filepath) -> str:
    with open(filepath, "r") as f:
        return [int(line) for line in f.readlines()]


# Load the adapters and sort them.
adapters = load_adapters(input_filepath)
adapters = sorted(adapters)


def part_1():
    '''In part 1:
    Simply loop through the ordered list of adapters and calculate the difference.
    '''

    differences = []

    for i in range(len(adapters) - 1):
        differences.append(adapters[i+1]-adapters[i])

    differences.append(adapters[0]-0)  # wall to adapter
    differences.append(3)  # adapter to phone

    num_of_1s = len([d for d in differences if d == 1])
    num_of_3s = len([d for d in differences if d == 3])
    print(f'Part 1: {num_of_1s*num_of_3s}')


def part_2():
    '''In part 2:
    1. Create an graph of possible configurations with an adjacency list.
    2. Run a depth-first-search on the graph while keeping track of the number of paths to the phone at each node of the graph.
    '''

    # Largest possible adapter connection joltage difference.
    n = 3

    # Put the 0 jolt wall connection at the front of the list,
    # and the phone with adapter+3 jolts at the end.
    adapters.insert(0, 0)
    adapters.append(adapters[-1]+n)

    # Create an adacency list to represent a Directed Acyclic Graph (DFS)
    # of all possible adapter combinations.
    #
    # We'll loop through adapters `i` and try consecutive adapters `i+j`.
    # Break if we reach the end of the list, or if we encounter an incompatible adapter.
    adjacency_list = {}
    for i in range(len(adapters)):
        j = 1
        adjacency = []
        while True:
            # Check if we've reach the end of the adapter list.
            if i + j > len(adapters)-1:
                break
            # If the difference between this node `i` and other node `i+j`
            # is greater than possible adapter connection, stop looking for
            # compatible adapters.
            if adapters[i+j] - adapters[i] > n:
                break
            adjacency.append(i+j)
            j += 1
        adjacency_list[i] = adjacency

    # The number of paths from node A to node B is the sum of
    # number of paths of A's children to node B.
    #
    # Here we use a depth first search from `start_n` to `target_n`.
    # We store each node's `path_count` to avoid expensive recalculations.

    start_n = 0
    target_n = len(adjacency_list)-1
    path_count = defaultdict(lambda: 0)  # missing keys default to value of 0

    def depth_first_search(n):
        if n == target_n:
            return 1
        else:
            # If we haven't counted paths to n, go get them. Otherwise just return the path count for n.
            if n not in path_count:
                # The paths from n to target_n is sum of number of paths of n's children to the target.
                for m in adjacency_list[n]:
                    path_count[n] += depth_first_search(m)
            return path_count[n]

    total_path_count = depth_first_search(start_n)
    print(f'Part 2: {total_path_count}')


part_1()
part_2()

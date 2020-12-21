'''
Re-write main.py to show that dicts, or key/value pairs, or pointers, are also classes with composition, which are themselves types, which in data will form an object graph
We'll avoid using key/values and lists here and instead recreate the object graph from the stored data in the input.txt. We're implicity filling out a 'typed dict' upon loading.
All possible objects form a set.
'''

import os
import re
from collections import defaultdict
from typing import List

# everything maps back to raw data...


# will be challenging to access this object without a hashmap on the color name
class Color():
    def __init__(self):
        pass

# a bag is a node in the directed graph


class Contains():
    ''' directed edge '''

    def __init__(self, value, bag: Bag):
        self.value = value
        self.bag = bag


class Bag():
    def __init__(self, color: Color, contains: Contains):
        self.color = color
        self.contains = contains


def absolute_path(filepath_relative_to_this_file):
    '''Get the absolute filepath to filepath relative to this .py module file.'''
    return os.path.join(os.path.dirname(
        os.path.abspath(__file__)), filepath_relative_to_this_file)


def read_lines(filepath) -> str:
    '''Get a list of lines from a file.'''
    with open(filepath, "r") as f:
        return [line for line in f.readlines()]


def parse_rules(rules):
    '''Load the rules with some lazy, hacked-together regex.'''
    rules_dict = {}
    for rule in rules:
        lhs_rhs = re.split(r" contain ", rule)
        lhs = lhs_rhs[0].replace('bags', '').replace('bag', '').strip()
        rhs = re.split(r",", lhs_rhs[1])
        thingys = []
        for r in rhs:
            is_no_bag = False
            thingy = re.match(r"\w?(\d)+\s([\w\s]*)", r.strip())
            if not thingy:
                thingy = re.match(r"no other bags", r)
                is_no_bag = True
            if not thingy:
                raise ValueError(f"can't parse line {r}")
            rhs_new = thingy.group().replace(
                'bags', '').replace('bag', '').strip()
            if is_no_bag == False:
                rhs_new = re.match(r"\w?(\d)+\s([\w\s]*)", rhs_new).groups()
            else:
                rhs_new = (None, None)
            thingys.append(rhs_new)
        rules_dict[lhs] = thingys
    return rules_dict


rules_dict = parse_rules(read_lines(absolute_path('input.txt')))


def part_1(rules_dict):
    '''
    The rules_dict is a directed graph with:
    1. Nodes as bag types.
    2. Edges that represent 'contains' with edge values = # of bags contained.

    To ask the question "How many colors can, eventually, contain at least one shiny gold bag?" is to
    ask "How many bag nodes are reachable via 'contains' edges leaving the 'shiny gold bag' node?"

    We'll represent the graph as an adjaceny list and implement a depth-first-search. The sum of all visited
    nodes will be our answer.
    '''
    # Reverse the 'rules dict' which is an adjacency list
    adjacency_list = defaultdict(list)
    for bag, contains in rules_dict.items():
        for c in contains:
            contains_num, contains_bag = c
            adjacency_list[contains_bag].append((bag, contains_num))

    # Depth First Search from starting node to all end nodes and marking whether the node is visited
    start_n = "shiny gold"
    visited = {key: False for key in adjacency_list.keys()}

    def depth_first_search(n):
        # Reached a bag that is not 'contained' by any other bag.
        if n not in adjacency_list:
            visited[n] = True
        else:
            if not visited[n]:
                visited[n] = True
                for m_name, _ in adjacency_list[n]:
                    depth_first_search(m_name)

    depth_first_search(start_n)

    # The answer is the sum of the visited bags.
    num_bags_visited = sum([1 for _, value in visited.items() if value])
    # don't count the shiny bag itself as an option - it must be carried by another bag.
    num_bags_visited -= 1

    print(f'Part 1: {num_bags_visited}')


def part_2(rules_dict):
    """
    Part 2 uses the adjacency list representation of the edge-weighted digraph, `rules_dict`, directly.

    The example says:
        faded blue bags contain 0 other bags.
        dotted black bags contain 0 other bags.
        vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
        dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.
        single shiny gold bag contains x other bags: 1 dark olive bag and 2 vibrant plum bags.

    With the conclusion that:
        A single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

    In other words:
        1*(3*(1)+4*(1))+2*(5*(1)+6*(1))

    Edge-weighted digraph looks super interesting. See https://en.wikipedia.org/wiki/Flow_network for some cool examples.
    Maybe it could be used to build an object graph. Like: 'x' has y of 'z', or 'engine' has 2 of 'turbos'.
    """

    # Depth First Search from starting node, stopping at end nodes (an end node is a bag that contains no other bags).
    # Store edge counts along the way to prevent re-calculations.
    start_n = "shiny gold"
    edge_count = defaultdict(lambda: 1)

    def depth_first_search_part_2(n):
        if n not in edge_count:
            for m_count, m_name in rules_dict[n]:
                if m_count:
                    edge_count[n] += int(m_count) * \
                        depth_first_search_part_2(m_name)
        return edge_count[n]

    # -1 because the shiny bag itself doesn't count
    answer = depth_first_search_part_2(start_n) - 1
    print('Part 2:', answer)


part_1(rules_dict)
part_2(rules_dict)

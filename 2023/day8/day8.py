import os

def read_input_lines(filename):
    anchor = os.path.dirname(__file__)
    f = open(os.path.join(anchor, filename))
    lines = [l.strip() for l in f.readlines()]
    f.close()
    return lines

def pt1():

    lines = read_input_lines("input_example_2")
    lines = read_input_lines("input")

    RL = lines[0]

    d = dict()
    for line in lines[2:]:
        lhs, rhs = line.split('=')
        l, r = rhs.replace('(', '').replace(')', '').strip().split(', ')
        d[lhs.strip()] = [l, r]

    print(d)
    count = 0
    curr = 'AAA'
    i = 0
    while True:
        rl = RL[i]
        print(curr, count, rl)
        count += 1
        lhs_rhs = d[curr]
        if rl == 'L':
            curr = lhs_rhs[0]
        elif rl == 'R':
            curr = lhs_rhs[1]
        else:
            Exception("nooo")
        if curr == 'ZZZ':
            return count
        i += 1
        if i == len(RL):
            i = 0
        
print(pt1()) # 11567 too low

def pt2():
    
    lines = read_input_lines("input_example_2")
    lines = read_input_lines("input")

    RL = lines[0]

    d = dict()
    for line in lines[2:]:
        lhs, rhs = line.split('=')
        l, r = rhs.replace('(', '').replace(')', '').strip().split(', ')
        d[lhs.strip()] = [l, r]

    starting_nodes = [node for node in d.keys() if node[2] == 'A']
    dd = dict()

    print(d)
    count = 0
    i = 0
    while True:
        for node in starting_nodes:
            rl = RL[i]
            print(curr, count, rl)
            count += 1
            lhs_rhs = d[curr]
            if rl == 'L':
                curr = lhs_rhs[0]
            elif rl == 'R':
                curr = lhs_rhs[1]
            else:
                Exception("nooo")
            if curr == 'ZZZ':
                return count
            i += 1
            if i == len(RL):
                i = 0
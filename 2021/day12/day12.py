import os
from collections import deque
f = open(os.path.join(os.path.dirname(__file__),"test_input.txt"))
lines = f.readlines()
d = dict()
for l in lines:
    l, r = l.replace("\n","").split("-")
    d[l] = r
f.close()

queue = deque()
visited = set()
lowers = set()


while True:
    c = queue.pop()
    if c not in visited:

    else:
        paths_from(c) += 1 


queue.append()
c = queue.pop()
if c.islower():
    if c not in lowers():
        lowers.add(c)

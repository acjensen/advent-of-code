lines = open("2022/day5/example_input.txt").read().splitlines()
# lines = [l.replace("] [", " ") for l in lines]
# lines = [l.replace("[", "") for l in lines]
# lines = [l.replace("]", "") for l in lines]
# print(lines)

# out = re.compile("").findall()
# print(out)

max_stack_height = 0
for line in lines:
    print(line[1])
    if (not line) or (line[1] == 1):
        print('breaking')
        break
    max_stack_height += 1

stacks = [[],[],[]]
i = 1
idxs = []
while i < len(lines[0]):
    idxs.append(i)
    i += 4

for stack_id, idx in enumerate(idxs):
    for line in lines:
        if line[1] == 1:
            break
        stacks[stack_id].append(line[idx])

print(stacks)

# for stack_id, stack in enumerate(stacks):
#     i = 1
#     if i > length:
#         continue
    
#     i += 4


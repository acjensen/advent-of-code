# #!python3

# from dataclasses import dataclass
# from ast import literal_eval


# with open("2022/day13/example_input.txt") as f:
#     lines = f.read().splitlines()

# lines = [literal_eval(line) for line in lines if line]

# flipflop = True
# for line in lines:
#     if flipflop:
#         flipflop = not flipflop

# def compare(first, second):

#     result = True
#     stack = []
#     idx = 0
#     stack.append((first, second, idx))
#     while stack:
#         if type(first[idx]) == int and type(second[idx]) == int:
#             if first < second:
#                 return True
#             if second < first:
#                 return False
#             # stack.append((
#             #     first,
#             #     second,
#             #     idx+1
#             # ))
#         else:
#             stack.append((
#                 [first[idx]] if type(first[idx]) == int else first[idx],
#                 [second[idx]] if type(second[idx]) == int else second[idx],
#                 0
#             ))
#         idx += 1
#         if idx < len(first) and idx < len(second):
#             first = first[idx]
#             second = second[idx]
#         else:
#             first, second, idx = stack.pop()
    
#     return result

# # print(compare(
# #     first = [1,1,3,1,1],
# #     second = [1,1,5,1,1],
# # ))

# print(compare(
#     first = [[1],[2,3,4]],
#     second = [[1],4],
# ))
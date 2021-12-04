from collections import defaultdict

n = 5 # Board size.

def parse(filename):
    num_to_board_map = defaultdict(list) # Maps num -> (board, row, col).
    board_contents = defaultdict(set) # Maps board -> set(num).
    board = 0
    row = 0
    with open(filename) as f:
        drawn_nums = f.readline().rstrip('\n').split(",")
        f.readline()
        while True:
            line_txt = f.readline()
            line = line_txt.rstrip('\n').split()
            if line_txt == '\n': # End of a board.
                board += 1
                row = 0
            elif not line: # End of file.
                break
            else: # Within a board.
                for col, num in enumerate(line):
                    num_to_board_map[num].append((board, row, col))
                    board_contents[board].add(num)
                row += 1
    num_boards = board + 1
    return drawn_nums, num_boards, board_contents, num_to_board_map

def board_score(remaining_nums, board_idx, winning_number):
    return sum([int(num) for num in remaining_nums[board_idx]])*int(winning_number)

def solve(filename, is_part_1=False):

    drawn_nums, num_boards, board_contents, num_to_board_map = parse(filename)

    boards_that_won = []
    row_col_count = [([0]*n,[0]*n) for _ in range(num_boards)]
    for num in drawn_nums:
        for (board, row, col) in num_to_board_map[num]:
            if board not in boards_that_won:
                if num in board_contents[board]:
                    board_contents[board].remove(num)
                row_col_count[board][0][row] += 1
                row_col_count[board][1][col] += 1
                if row_col_count[board][0][row] == n or row_col_count[board][1][col] == n:
                    boards_that_won.append(board)
                    if is_part_1:
                        return board_score(board_contents, board, num)
                    else:
                        winning_number = num
    return board_score(board_contents, boards_that_won[-1], winning_number)

print("Part 1 test input:", solve("test_input.txt", is_part_1=True))
print("Part 1 answer:", solve("input.txt", is_part_1=True))
print("Part 2 test input:", solve("test_input.txt", is_part_1=False))
print("Part 2 answer:", solve("input.txt", is_part_1=False))
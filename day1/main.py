from itertools import combinations
from operator import mul
from functools import reduce
from typing import List
import os

# Load the expense file into memory.
def load_expenses(filepath) -> List[int]:
    with open(filepath, "r") as f:
        # Deserialize the expense file into a list of integers.
        return [int(line) for line in f]

# Get the product of n entries that sum to |target_sum|
def product_of_n_entries_that_sum_to_s(expenses: List[int], num_entries: int, target_sum: int) -> int:
    # Loop through all sets of combinations of size |n|.
    for c in combinations(expenses, num_entries):
        if sum(c) == target_sum:
            return reduce(mul, c)


if __name__ == "__main__":

    # Load the expense file into memory.
    filepath = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "expenses.txt")
    expenses = load_expenses(filepath)

    # Get the product of n entries that sum to 2020
    part_1_result = product_of_n_entries_that_sum_to_s(
        expenses, num_entries=2, target_sum=2020)
    part_2_result = product_of_n_entries_that_sum_to_s(
        expenses, num_entries=3, target_sum=2020)

    print(part_1_result)
    print(part_2_result)

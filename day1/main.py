# Load the expense file into memory.
expense_file = open("expenses.txt", "r")

# Deserialize the expense file into a list of integers.
expenses = [int(line) for line in expense_file]


def get_product_of_two_entries_that_sum_to_2020(expenses):
    # Look through expenses. Compare 2 entries at a time without repeating any comparisons.
    while expenses:
        e1 = expenses.pop()
        if e1 >= 2020:
            pass
        else:
            for e2 in expenses:
                if e1+e2 == 2020:
                    return e1*e2
    return False


answer = get_product_of_two_entries_that_sum_to_2020(expenses)
print(answer)

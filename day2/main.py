import os
import re
from typing import List


class Password(object):

    ''' A data structure to parse, store, and validate passwords.'''

    def __init__(self, low, high, limited_char, password):
        self.low = int(low)
        self.high = int(high)
        self.limited_char = str(limited_char)
        self.password = str(password)

    def is_valid(self):
        num_limited_char = self.password.count(self.limited_char)
        if num_limited_char >= self.low and num_limited_char <= self.high:
            return True
        else:
            return False

    # Enable pretty-printing of this data structure
    def __repr__(self):
        return str(self.__dict__)


class PasswordLoader(object):

    ''' Loads and stores passwords from a file. '''

    regular_expression = r"(\w*)-(\w*) (\w): (\w*)"

    def __init__(self, filepath):
        self.passwords = self.load_passwords(filepath)

    # Load passwords from a file.
    @staticmethod
    def load_passwords(filepath) -> List[Password]:
        with open(filepath, "r") as input:
            regex_result = []
            for line in input:
                r = re.match(PasswordLoader.regular_expression, line)
                if r:
                    regex_result.append(r)
                else:
                    raise Exception(
                        f"There was an error parsing line '{line}' in the input file.")
            passwords = [Password(*s.groups()) for s in regex_result]
            return passwords

    # Get the number of valid passwords
    def num_valid_passwords(self) -> int:
        num_valid_passwords = 0
        for p in self.passwords:
            if p.is_valid():
                num_valid_passwords += 1
        return num_valid_passwords


# Get the full path to the input file.
filepath = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "input.txt")

# Load the input file and count the number of valid passwords.
part_1_result = PasswordLoader(filepath).num_valid_passwords()
print(part_1_result)

# For part 2, we need to edit the 'is_valid' function in the Password class.
# Lets just monkey-patch it here.
def is_valid_2(self):
    # Each policy describes two positions in the password, where 1 means the first
    # character, 2 means the second character, and so on, with indexing starting from 1.
    # Exactly one of these positions must contain the given letter.

    def password_has_char_at_index(password_index: int) -> bool:
        password_index -= 1
        if password_index < len(self.password):
            return self.password[password_index] != self.limited_char
        else:
            return True

    return password_has_char_at_index(self.high) ^ password_has_char_at_index(self.low)

Password.is_valid = is_valid_2 # Monkey patch
part_2_result = PasswordLoader(filepath).num_valid_passwords()
print(part_2_result)
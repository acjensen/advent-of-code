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


if __name__ == "__main__":

    # Load the input file into memory.
    filepath = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "input.txt")

    # Load the input file and count the number of valid passwords.
    part_1_result = PasswordLoader(filepath).num_valid_passwords()
    print(part_1_result)

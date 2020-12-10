import os
from typing import List, Tuple
import re


# Define data validators.

def is_year_in_range(value: str, inclusive_range: Tuple[int, int]) -> bool:
    # Check if year is 4 digits long.
    if not re.compile(r"^\d{4}$").match(value):
        return False
    year = int(value)
    # Check if year is in range.
    return year >= inclusive_range[0] and year <= inclusive_range[1]


def is_birth_year(value: str) -> bool:
    return is_year_in_range(value, (1920, 2002))


def is_issue_year(value: str) -> bool:
    return is_year_in_range(value, (2010, 2020))


def is_expiration_year(value: str) -> bool:
    return is_year_in_range(value, (2020, 2030))


def is_height(value: str) -> bool:
    # Check for malformed input.
    parsed = re.compile(r"^(\d{1,3})([a-z]{2})$").match(value)
    if not parsed:
        return False

    # Parse the input and validate.
    quantity = int(parsed.groups()[0])
    unit = parsed.groups()[1]
    if unit == 'cm':
        return 150 <= quantity <= 193
    elif unit == 'in':
        return 59 <= quantity <= 76
    else:
        return False


def is_hair_color(value: str) -> bool:
    return bool(re.compile(r"^#[\da-f]{6}$").match(value))


def is_eye_color(value: str):
    return value in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}


def is_passport_id(value: str):
    return re.compile(r"^\d{9}$").match(value)

# Define required fields and assign validators.


required_fields = {
    'byr': is_birth_year,
    'iyr': is_issue_year,
    'eyr': is_expiration_year,
    'hgt': is_height,
    'hcl': is_hair_color,
    'ecl': is_eye_color,
    'pid': is_passport_id,
    # 'cid' is optional.
}


def load_passports(filepath) -> str:
    with open(filepath, "r") as f:
        return f.read()


# Get the input data filepath.
input_filepath = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "input.txt")

# Import the passport form data to a list of key-value stores.
passports_string = load_passports(input_filepath)
passport_forms = re.compile(r"\n\n").split(passports_string)
passport_field_pattern = re.compile(r"([a-z]{3}):([^(\s|(\n))]*)")
passport_forms_parsed = [passport_field_pattern.findall(
    form) for form in passport_forms]
passports = [{field: value for field, value in form}
             for form in passport_forms_parsed]


def has_valid_fields(passport):
    '''Validate passport field values.'''
    for field, validator in required_fields.items():
        if not validator(passport[field]):
            return False
    return True


def is_valid_passport(passport, validate_values=False):
    '''Validate passport form fields with optional field value validation.'''
    if not set(required_fields.keys()).issubset(set(passport.keys())):
        return False
    if validate_values:
        return has_valid_fields(passport)
    return True


def get_num_valid_passports(validate_values=False):
    '''Count the number of valid passports.'''
    num_valid_passports = 0
    for passport in passports:
        if is_valid_passport(passport, validate_values):
            num_valid_passports += 1
    return num_valid_passports


print('Part 1:', get_num_valid_passports(validate_values=False))
print('Part 2:', get_num_valid_passports(validate_values=True))

import re

file_path = 'validation_data.txt'
# file_path = 'test_input_invalid_validation.txt'
# file_path = 'test_input_valid_validation.txt'
# file_path = 'test_input.txt'

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def validate_range_keys(value, min_value, max_value):
    if int(min_value) <= int(value) <= int(max_value):
        return True
    else:
        print(f'Incorrect value: {value}')
        return False


def validate_keys(current_key, value):
    if current_key == 'byr':
        return validate_range_keys(value, 1920, 2002)
    elif current_key == 'iyr':
        return validate_range_keys(value, 2010, 2020)
    elif current_key == 'eyr':
        return validate_range_keys(value, 2020, 2030)
    elif current_key == 'hgt':
        if str(value).strip():
            if 'cm' in value:
                return validate_range_keys(int(value[:-2]), 150, 193)
            elif 'in' in value:
                return validate_range_keys(int(value[:-2]), 59, 76)
            else:
                print(f'Incorrect {current_key}, value: {value}')
                return False
    elif current_key == 'hcl':
        matched = re.match("#[abcdef\\d]{6}", str(value))
        if bool(matched):
            return True
        else:
            print(f'Incorrect {current_key}, value: {value}')
            return False
    elif current_key == 'ecl':
        if str(value).strip() in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return True
        else:
            print(f'Incorrect {current_key}, value: {value}')
            return False
    elif current_key == 'pid':
        matched = re.match("[0]{0,}[\\d]{1,}", str(value))
        if bool(matched) and len(str(value).strip()) == 9:
            return True
        else:
            print(f'Incorrect {current_key}, value: {value}')
            return False
    else:
        return False


def validate_passport(input_dict: dict) -> bool:
    count_of_required = 0
    for field in required_fields:
        if field in input_dict.keys():
            if validate_keys(field, input_dict[field]):
                count_of_required += 1
    if count_of_required == len(required_fields):
        return True
    else:
        return False


with open(file_path, 'r') as file:
    result_list = []
    current_dict = {}
    for line in file.readlines():
        if line.strip():
            current_line = [x.strip() for x in line.replace('\n', '').split()]
            for element in current_line:
                current_dict[element[:3]] = element[4:]
        else:
            result_list.append(current_dict)
            current_dict = {}
    result_list.append(current_dict)
    valid_passports_count = 0
    for passport in result_list:
        if validate_passport(passport):
            valid_passports_count += 1
    print(f'Part 1 result: {valid_passports_count}')

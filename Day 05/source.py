import math

file_path = 'validation_data.txt'
# file_path = 'test_input.txt'


def split(input_list: list, lower_or_higher='F') -> list:
    half_value = math.ceil(len(input_list)/2)
    # print(half_value)
    if lower_or_higher == 'F' or lower_or_higher == 'L':
        return input_list[:half_value]
    else:
        return input_list[half_value:]


def calculate_row_or_place(min_place, max_place, sequence: str) -> int:
    # print(sequence)
    current_list = list(range(min_place, max_place))
    # print(current_list)
    for el in sequence:
        # print(el)
        current_list = split(current_list, el)
        # print(current_list)
    return current_list[0]


def calculate_seat_id(sequence, len_of_rows=7):
    current_row = calculate_row_or_place(0, 128, sequence[:len_of_rows])
    current_column = calculate_row_or_place(0, 8, sequence[len_of_rows:])
    return current_row, current_column, (current_row * 8) + current_column


with open(file_path, 'r') as file:
    result = []
    for line in file.readlines():
        row, col, score = calculate_seat_id(line.strip())
        result.append(score)
    print(f'part I result: {max(result)}')
    result = sorted(result)
    for element in result:
        if element + 2 in result and element +1 not in result:
            print(element + 1)

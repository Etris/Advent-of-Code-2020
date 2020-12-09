file_result = 'validation_data.txt'
file_test = 'test_input.txt'


def validate(current_value: int, possible_elements: list) -> bool:
    state = False
    for ix_main, value_main in enumerate(possible_elements):
        for ix_sec, value_sec in enumerate(possible_elements):
            if ix_main == ix_sec:
                continue
            else:
                if value_main + value_sec == current_value:
                    state = True
    return state


def part_1_solution(current_data: list, starting_position: int) -> int:
    for ix in range(len(current_data)):
        if ix < starting_position:
            continue
        # print(f'Position: {ix}, start_range: {ix - starting_position}')
        if not validate(current_data[ix], current_data[ix - starting_position:ix]):
            return current_data[ix]


def part_2_solution(current_data, result_to_find) -> int:
    for ix in range(len(current_data)):
        current_sum = current_data[ix]
        for sub_ix in range(len(current_data)):
            if sub_ix != ix and sub_ix > ix:
                current_sum += current_data[sub_ix]
                #print(f'Current start ix: {ix}, sub: {sub_ix}, sum: {current_sum}')
            if current_sum == result_to_find:
                return min(current_data[ix: sub_ix+1]) + max(current_data[ix: sub_ix+1])
            elif current_sum > result_to_find:
                break


with open(file_test, 'r') as file:
    print('Test: ')
    data = [int(x) for x in file.readlines()]
    part_1_result = part_1_solution(data.copy(), 5)
    print(f'Part I solution: {part_1_result}')
    print(f'Part II solution: {part_2_solution(data.copy(), part_1_result)}')


with open(file_result, 'r') as file:
    print('Scored: ')
    data = [int(x) for x in file.readlines()]
    part_1_result = part_1_solution(data.copy(), 25)
    print(f'Part I solution: {part_1_result}')
    print(f'Part II solution: {part_2_solution(data.copy(), part_1_result)}')



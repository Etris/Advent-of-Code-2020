file_path = 'validation_data.txt'
# file_path = 'test_input.txt'


def run_line(line, current_ix, acc_value):
    if visited[current_ix] == 1:
        print(f'Part I result: {acc_value}')
    else:
        visited[current_ix] = 1
        if 'nop' in line:
            run_line(data_list[current_ix + 1], current_ix + 1, acc_value)
        elif 'acc' in line:
            value = int(str(line).split(' ')[1])
            run_line(data_list[current_ix + 1], current_ix + 1, acc_value + value)
        elif 'jmp' in line:
            value = int(str(line).split(' ')[1])
            run_line(data_list[current_ix + value], current_ix + value, acc_value)


def run_line_part_2(line, current_ix, acc_value, current_visited, current_data_list, current_path):
    if current_ix >= len(current_data_list):
        print(f'Part II result: {acc_value}')
    elif current_visited[current_ix] == 1:
        return False
    else:
        current_visited[current_ix] = 1
        current_path.append(current_ix)
        if 'nop' in line:
            if current_ix + 1 >= len(current_data_list):
                print(f'Part II result: {acc_value}')
            else:
                run_line_part_2(current_data_list[current_ix + 1], current_ix + 1, acc_value,
                                current_visited, current_data_list, current_path)
        elif 'acc' in line:
            value = int(str(line).split(' ')[1])
            acc_value += value
            if current_ix + 1 >= len(current_data_list):
                print(f'Part II result: {acc_value}')
                print(f'Path: {current_path}')
            else:
                run_line_part_2(current_data_list[current_ix + 1], current_ix + 1, acc_value,
                                current_visited, current_data_list, current_path)
        elif 'jmp' in line:
            value = int(str(line).split(' ')[1])
            if current_ix + value >= len(current_data_list):
                print(f'Part II result: {acc_value}')
                print(f'Path: {current_path}')
            else:
                run_line_part_2(current_data_list[current_ix + value], current_ix + value, acc_value,
                                current_visited, current_data_list, current_path)


def try_all_permutations():
    for ix in range(len(data_list)):
        if 'jmp' in data_list[ix] or 'nop' in data_list[ix]:
            current_copy_of_data_list = data_list.copy()
            if 'jmp' in current_copy_of_data_list[ix]:
                current_copy_of_data_list[ix] = current_copy_of_data_list[ix].replace('jmp', 'nop')
            elif 'jmp' in current_copy_of_data_list[ix]:
                current_copy_of_data_list[ix] = current_copy_of_data_list[ix].replace('jmp', 'nop')
            run_line_part_2(current_copy_of_data_list[0], 0, 0,
                            [0 for x in range(len(current_copy_of_data_list))],
                            current_copy_of_data_list,
                            [])


with open(file_path, 'r') as file:
    data_list = [str(x) for x in file.readlines()]
    visited = [0 for x in range(len(data_list))]
    run_line(data_list[0], 0, 0)
    try_all_permutations()

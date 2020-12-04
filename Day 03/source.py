file_path = 'validation_data.txt'
# file_path = 'test_input.txt'


def multiply_list(data: list) -> int:
    result = 1
    for element in data:
        result *= element
    return result


def find_count_of_trees_on_path(data: list, right: int, down: int) -> int:
    current_x = 0
    tree_counter = 0
    for current_y in range(0, len(data), down):
        if data[current_y][current_x] == '#':
            tree_counter += 1
        current_x = (current_x + right) % len(data[current_y])
    return tree_counter


with open(file_path, 'r') as file:
    lines = [str(x).strip() for x in file.read().splitlines()]
    print(f'Part 1 result: {find_count_of_trees_on_path(lines, 3, 1)}')
    slopes = [
        find_count_of_trees_on_path(lines, 1, 1),
        find_count_of_trees_on_path(lines, 3, 1),
        find_count_of_trees_on_path(lines, 5, 1),
        find_count_of_trees_on_path(lines, 7, 1),
        find_count_of_trees_on_path(lines, 1, 2)
    ]
    print(f'Part 2 result: {multiply_list(slopes)}')

file_path = 'validation_data.txt'
#file_path = 'test_input.txt'
with open(file_path, 'r') as file:
    lines = [int(x) for x in file.readlines()]
    for ix_first, element in enumerate(lines):
        for ix_second, second_element in enumerate(lines[ix_first + 1:]):
            for third_element in lines[ix_second + 1:]:
                if sum([element, second_element, third_element]) == 2020:
                    print(f'Result: {element * second_element * third_element}')
from typing import Union

file_path = 'validation_data.txt'
# file_path = 'test_input.txt'

rules = {}


def add_to_rules(main_key: str, value_key: Union[int, str], value) -> None:
    rules[main_key.strip()] = rules.get(main_key.strip(), []) + [{'bag': value_key, 'amount': value}]


def add_all_rules(input_data: list) -> None:
    for row in input_data:
        current_key = row[:row.find('bags contain')].strip()
        rest_of_data = row[row.find('bags contain') + 12:].strip()
        if ',' in row:
            single_elements = [str(x).strip() for x in rest_of_data.split(',')]
            for element in single_elements:
                current_bag = [str(x).strip() for x in element.split()]
                bag_name = ' '.join(current_bag[1:-1])
                add_to_rules(current_key, bag_name, int(current_bag[0]))
        elif 'no other' in row:
            add_to_rules(current_key, 0, 0)
        else:
            current_bag = [str(x).strip() for x in rest_of_data.split()]
            bag_name = ' '.join(current_bag[1:-1])
            add_to_rules(current_key, bag_name, int(current_bag[0]))


def count_all_possible_placements(current_key, key_to_find='shiny gold') -> int:
    current_data = rules.get(current_key, [])
    counter = 0
    if len(current_data) > 0:
        for sub_dict in current_data:
            if sub_dict['bag'] == key_to_find:
                return 1
            else:
                counter += count_all_possible_placements(sub_dict['bag'])
        return counter
    else:
        return 0


def count_result() -> int:
    counter = 0
    for key in rules.keys():
        current_counter = count_all_possible_placements(key)
        if current_counter:
            counter += 1
    return counter


def count_part_two(key):
    current_data = rules.get(key, [])
    counter = 1
    if len(current_data) > 0:
        for sub_dict in current_data:
            #print(key, ',', sub_dict)
            if sub_dict['bag'] != 0:
                counter += int(sub_dict['amount']) * int(count_part_two(sub_dict['bag']))
            else:
                return 1
        return counter
    else:
        return 1


with open(file_path, 'r') as file:
    data = [str(x)[:-1] for x in file.readlines()]
    add_all_rules(data)
    print(rules)
    print(count_result())
    print(count_part_two('shiny gold') - 1)

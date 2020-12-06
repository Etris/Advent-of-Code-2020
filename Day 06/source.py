file_path = 'validation_data.txt'
# file_path = 'test_input.txt'


def count_unique_from_group(group: list) -> int:
    result_set = set()
    for element in group:
        for sub_element in element:
            result_set.add(sub_element)
    return len(result_set)


def count_if_all_answered_positive(group: list) -> int:
    answers_dict = {}
    for element in group:
        for sub_element in element:
            answers_dict[sub_element] = answers_dict.get(sub_element, 0) + 1
    scoring = 0
    for key in answers_dict.keys():
        if answers_dict[key] == len(group):
            scoring += 1
    return scoring


with open(file_path, 'r') as file:
    result_list = []
    result_list_all_positive = []
    current_group = []
    for line in file.readlines():
        if line.strip():
            current_group.append(line.strip())
        else:
            score = count_unique_from_group(current_group)
            score_second = count_if_all_answered_positive(current_group)
            result_list.append(score)
            result_list_all_positive.append(score_second)
            current_group = []
    score = count_unique_from_group(current_group)
    score_second = count_if_all_answered_positive(current_group)
    result_list.append(score)
    result_list_all_positive.append(score_second)
    print(f'Part 1 result: {sum(result_list)}')
    print(f'Part 2 result: {sum(result_list_all_positive)}')

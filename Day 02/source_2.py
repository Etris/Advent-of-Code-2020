file_path = 'validation_data.txt'
#file_path = 'test_input.txt'
with open(file_path, 'r') as file:
    lines = [str(x) for x in file.readlines()]
    count_of_valid = 0
    for line in lines:
        allowed_range, phrase, password = [str(x) for x in line.split(' ')]
        first_position, second_position = [int(x) - 1 for x in allowed_range.split('-')]
        phrase = phrase[:-1]
        if password[first_position] == phrase:
            if password[second_position] == phrase:
                continue
            else:
                count_of_valid += 1
        else:
            if password[second_position] == phrase:
                count_of_valid += 1
            else:
                continue
    print(f'Result: {count_of_valid}')

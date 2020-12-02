file_path = 'validation_data.txt'
#file_path = 'test_input.txt'
with open(file_path, 'r') as file:
    lines = [str(x) for x in file.readlines()]
    count_of_valid = 0
    for line in lines:
        allowed_range, phrase, password = line.split(' ')
        min_range, max_range = [int(x) for x in allowed_range.split('-')]
        current_count = str(password).count(str(phrase)[:-1])
        if min_range <= current_count <= max_range:
            count_of_valid += 1
    print(f'Result: {count_of_valid}')

import re

# ================================================================================================
# Part 1

def check_game_validity(game_data):
    red_count = 0
    green_count = 0
    blue_count = 0

    for subset in game_data.split(';'):
        for cube in subset.split(','):
            count, color = cube.strip().split(' ')
            count = int(count)

            if color == 'red':
                red_count += count
            elif color == 'green':
                green_count += count
            else:
                blue_count += count

        if red_count > 12 or green_count > 13 or blue_count > 14:
            return False

        red_count = 0
        green_count = 0
        blue_count = 0

    return True


def calculate_valid_game_ids(input_data):
    valid_game_ids = []
    for line in input_data.splitlines():
        game_id, game_data = line.split(': ', 1)
        game_id = int(re.findall(r"\d+", game_id)[0])

        if check_game_validity(game_data):
            valid_game_ids.append(game_id)

    return valid_game_ids


# ================================================================================================
# Part 2
def fewest_numbers(game_data):
    red_number = 0
    green_number = 0
    blue_number = 0

    for subset in game_data.split(';'):
        for cube in subset.split(','):
            count, color = cube.strip().split(' ')
            count = int(count)

            if color == 'red':
                if count > red_number:
                    red_number = count
            elif color == 'green':
                if count > green_number:
                    green_number = count
            else:
                if count > blue_number:
                    blue_number = count

    return red_number * green_number * blue_number


def calculate_fewest_numbers(input_data):
    valid_game_ids = []
    for line in input_data.splitlines():
        game_id, game_data = line.split(': ', 1)
        game_id = int(re.findall(r"\d+", game_id)[0])

        valid_game_ids.append(fewest_numbers(game_data))

    return valid_game_ids

# ================================================================================================
def main():
    with open('inputs/Day2.txt', 'r') as input_file:
        input_data = input_file.read()

    valid_game_ids = calculate_valid_game_ids(input_data)
    valid_game_ids2 = calculate_fewest_numbers(input_data)
    print("Part 1: ", sum(valid_game_ids))
    print("Part 2: ", sum(valid_game_ids2))


if __name__ == '__main__':
    main()

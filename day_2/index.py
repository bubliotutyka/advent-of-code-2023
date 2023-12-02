import os

max_cube = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def get_data():
    lines = []
    data_file_path = os.path.join(os.path.dirname(__file__), 'data')
    with open(data_file_path, 'r') as file:
        for line in file:
            lines.append(line.strip())

    return lines


def get_games():
    games = []

    for line in get_data():
        sets = line.split(': ')[1].split('; ')
        game = []

        for set in sets:
            parsed_set_colors = set.split(', ')
            set_objet = {}

            for color in parsed_set_colors:
                parsed_color = color.split(' ')
                set_objet[parsed_color[1]] = int(parsed_color[0])

            game.append(set_objet)

        games.append(game)

    return games


def is_valid_set(set):
    for color in set:
        if set[color] > max_cube[color]:
            return False

    return True


def is_valid_game(game):
    for set in game:
        if not is_valid_set(set):
            return False

    return True


def get_result():
    valid_games_ids = []
    games = get_games()

    i = 0

    while i < len(games):
        if (is_valid_game(games[i])):
            valid_games_ids.append(i + 1)

        i += 1

    return sum(valid_games_ids)


print(get_result())

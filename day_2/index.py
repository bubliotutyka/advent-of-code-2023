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



def get_game_power(game):
    minimum_red_cubes = 0
    minimum_green_cubes = 0
    minimum_blue_cubes = 0

    for set in game:
        if "red" in set and set["red"] > minimum_red_cubes:
            minimum_red_cubes = set["red"]

        if "green" in set and set["green"] > minimum_green_cubes:
            minimum_green_cubes = set["green"]

        if "blue" in set and set["blue"] > minimum_blue_cubes:
            minimum_blue_cubes = set["blue"]

    return minimum_red_cubes * minimum_green_cubes * minimum_blue_cubes

def get_result():
    games_power = []
    games = get_games()

    for game in games:
        games_power.append(get_game_power(game))

    return sum(games_power)


print(get_result())

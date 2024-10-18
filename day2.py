import re


def parse_games(input_text):
    games_info = []
    games = input_text.split('\n')

    for game in games:
        game_data = game.split(': ')
        game_id = re.search(r'\d+', game.split(':')[0]).group()
        sets_info = game_data[1].split('; ')
        sets_pulled = []

        for set_info in sets_info:
            colors = set_info.split(', ')
            colors_count = {'r': 0, 'g': 0, 'b': 0}
            for color in colors:
                count, col = color.split()
                colors_count[col[0]] += int(count)
            sets_pulled.append(colors_count)

        games_info.append({game_id : sets_pulled})

    return games_info


def filter_invalid_games(games_info, max):
    return [
        game for game in games_info if all(
            set['r'] <= max['r'] and set['g'] <= max['g'] and set['b'] <= max['b'] for set in list(game.values())[0]
        )
    ]


games = parse_games(open("inputs/day2", "r").read())

print(sum(int(list(dictionary.keys())[0]) for dictionary in filter_invalid_games(games, {'r': 12, 'g': 13, 'b': 14})))

max_values = [
    max(set[color] for set in list(game.values())[0]) for game in games for color in ['r', 'g', 'b']
]
print(sum([max_values[i] * max_values[i + 1] * max_values[i + 2] for i in range(0, len(max_values), 3)]))
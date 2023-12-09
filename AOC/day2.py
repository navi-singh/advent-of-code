import re
import os
from collections import namedtuple

Game = namedtuple('Game', ['id', 'draws_data'])
Draw = namedtuple('Draw', ['blue', 'red', 'green'])


def readInput():
    file_path = os.path.join(os.getcwd(), 'Input', 'day2.txt')
    with open(file_path, 'r') as file:
        data = file.read().strip()
    lines = data.split("\n")
    return lines


def generateGames(lines):
    games = []
    for line in lines:
        metadata = line.strip().split(': ')
        draws = metadata[1].split(';')
        draws_data = []

        for draw in draws:
            temp_draw = Draw(blue=0, red=0, green=0)
            for matches in re.findall(r'((\d+) (blue|red|green))+', draw.strip()):
                temp_draw = temp_draw._replace(**{matches[2]: int(matches[1])})
                draws_data.append(temp_draw)

        games.append(Game(int(re.findall(r'\d+', metadata[0])[0]), draws_data))
    return games


def part1(games):
    valid_id_sum = 0
    for game in games:
        if all(draw.blue <= 14 and draw.red <= 12 and draw.green <= 13 for draw in game.draws_data):
            valid_id_sum = valid_id_sum + game.id
    return valid_id_sum


def part2(games):
    power = 0
    for game in games:
        power = power + max(draw.green for draw in game.draws_data) * max(
            draw.blue for draw in game.draws_data) * max(draw.red for draw in game.draws_data)
    return power


lines = readInput()
games = generateGames(lines)
print(part1(games))
print(part2(games))

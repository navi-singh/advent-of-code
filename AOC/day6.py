import re
import os


def readInput():
    file_path = os.path.join(os.getcwd(), 'Input', 'day6.txt')
    with open(file_path, 'r') as file:
        data = file.read().strip()
    lines = data.split("\n")
    return lines


def part1(lines):
    result = 1
    times = [int(value) for value in re.findall(r'\d+', lines[0])]
    distances = [int(value) for value in re.findall(r'\d+', lines[1])]
    for race_num, time in enumerate(times):
        result *= sum((time-t)*t > distances[race_num] for t in range(1, time))
    return result


def part2(lines):
    result = 0
    _, time = lines[0].split(": ")
    _, distance = lines[1].split(": ")
    time = int(time.replace(" ", ""))
    distance = int(distance.replace(" ", ""))
    result = sum(((time - t) * t) > distance for t in range(1, time))
    return result


lines = readInput()
print(part1(lines))
print(part2(lines))

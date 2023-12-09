import math
import re
import os


def readInput():
    file_path = os.path.join(os.getcwd(), 'Input', 'day8.txt')
    with open(file_path, 'r') as file:
        data = file.read().strip()
    lines = data.split("\n")
    return lines


def part1(lines):
    directions = [x for x in lines[0]]
    dict = {}
    for line in lines[2:]:
        matches = re.findall(r'(\w+)\s*=\s*\((.*?)\)', line)
        dict[matches[0][0]] = [value.strip()
                               for value in matches[0][1].split(',')]
    key, index, steps = 'AAA', 0, 0

    while key != 'ZZZ':
        steps += 1
        key = dict[key][directions[index] == 'R']
        index = (index + 1) % len(directions)
    return steps


def part2(lines):
    directions = [x for x in lines[0]]
    dict = {}
    start_keys = []
    for line in lines[2:]:
        matches = re.findall(r'(\w+)\s*=\s*\((.*?)\)', line)
        dict[matches[0][0]] = [value.strip()
                               for value in matches[0][1].split(',')]
        if matches[0][0].endswith("A"):
            start_keys.append(matches[0][0])

    steps_for_keys = []
    for key in start_keys:
        index, steps = 0, 0
        while not key.endswith("Z"):
            steps += 1
            key = dict[key][directions[index] == 'R']
            index = (index + 1) % len(directions)
        ans.append(steps)
    return math.lcm(*steps_for_keys)


lines = readInput()
print(part1(lines))
print(part2(lines))

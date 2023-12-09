import math
import os


def readInput():
    file_path = os.path.join(os.getcwd(), 'Input', 'day9.txt')
    with open(file_path, 'r') as file:
        data = file.read().strip()
    lines = data.split("\n")
    return lines


def generate_list(line):
    input = []
    input.append([int(value) for value in line.split()])
    for i in range(0, len(input[0])):
        list = []
        for j in range(1, len(input[i])):
            list.append(input[i][j] - input[i][j-1])
        if all(elem == 0 for elem in list):
            break
        input.append(list)
    return input


def get_next(grid):
    result = 0
    for i in range(len(grid)-1, -1, -1):
        last_index = len(grid[i])-1
        result += grid[i][last_index]
    return result


def get_previous(grid):
    res = sum(row[0] for row in reversed(grid))
    result = 0
    for i in range(len(grid)-1, -1, -1):
        result = grid[i][0] - result
    return result


def part1(lines):
    result = 0
    for x in lines:
        grid = generate_list(x)
        next = get_next(grid)
        result += next
    return result


def part2(lines):
    result = 0
    for x in lines:
        grid = generate_list(x)
        next = get_previous(grid)
        result += next
    return result


lines = readInput()
print(part1(lines))
print(part2(lines))

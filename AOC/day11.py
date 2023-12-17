from itertools import combinations
import sys
import re
import os
import os
from copy import deepcopy
from math import gcd
from collections import defaultdict, Counter, deque


def readInput():
    file_path = os.path.join(os.getcwd(), 'Input', 'day11.txt')
    with open(file_path, 'r') as file:
        data = file.read().strip()
    lines = data.split("\n")
    return lines


def p1(lines):
    grid = [line.strip() for line in lines]
    dbl_i = {i for i, line in enumerate(grid) if "#" not in line}
    dbl_j = {j for j in range(len(grid[0])) if "#" not in [
        line[j] for line in grid]}
    pts = {(i, j) for i, l in enumerate(grid)
           for j, c in enumerate(l) if c == "#"}

    sum = 0
    for p, q in combinations(pts, 2):
        sum += abs(p[0] - q[0])
        sum += abs(p[1] - q[1])
        sum += len(dbl_i & set(range(min(p[0], q[0]), max(p[0], q[0]) + 1)))
        sum += len(dbl_j & set(range(min(p[1], q[1]), max(p[1], q[1]) + 1)))
    return sum


def part1(lines):
    empty_rows = set()
    empty_columns = set()
    galaxy_coordinates = set()
    for row_num, line in enumerate(lines):
        if "#" not in line:
            empty_rows.add(row_num)
    for col_num in range(len(lines[0])):
        if "#" not in [line[col_num] for line in lines]:
            empty_columns.add(col_num)

    for i, l in enumerate(lines):
        for j, c in enumerate(l):
            if c == "#":
                galaxy_coordinates.add((i, j))

    paths = 0
    for source, destination in combinations(galaxy_coordinates, 2):
        paths += abs(source[0] - destination[0]) + \
            abs(source[1] - destination[1])
        paths += len(empty_rows &
                     set(range(min(source[0], destination[0]), max(source[0], destination[0]) + 1)))
        paths += len(empty_columns &
                     set(range(min(source[1], destination[1]), max(source[1], destination[1]) + 1)))
    return paths


def p2(f):
    grid = [line.strip() for line in f]
    dbl_i = {i for i, line in enumerate(grid) if "#" not in line}
    dbl_j = {j for j in range(len(grid[0])) if not any(
        line[j] == "#" for line in grid)}
    pts = {(i, j) for i, l in enumerate(grid)
           for j, c in enumerate(l) if c == "#"}

    return sum(
        abs(p[0] - q[0])
        + abs(p[1] - q[1])
        + 999999 *
        len(dbl_i & set(range(min(p[0], q[0]), max(p[0], q[0]) + 1)))
        + 999999 *
        len(dbl_j & set(range(min(p[1], q[1]), max(p[1], q[1]) + 1)))
        for p, q in combinations(pts, 2)
    )


lines = readInput()
print(p1(lines))
print(part1(lines))
print(p2(lines))

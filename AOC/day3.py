import re
import os
from collections import namedtuple
from collections import defaultdict


def readInput():
    file_path = os.path.join(os.getcwd(), 'Input', 'day3.txt')
    with open(file_path, 'r') as file:
        data = file.read().strip()
    lines = data.split("\n")
    return lines


Range = namedtuple('Range', ['line_number', 'start', 'end'])
def isSymbol(x): return x != "."


def test1(lines):
    result = 0
    for idx, line in enumerate(lines):
        for match in re.finditer(r"\d+", line):
            foundSymbol = False
            if (match.start() > 0 and isSymbol(lines[idx][match.start() - 1])) or (match.end() < len(lines[idx]) and isSymbol(lines[idx][match.end()])):
                foundSymbol = True
            else:
                ranges = [Range(idx - 1, match.start() - 1, match.end() + 1)] + \
                    [Range(idx + 1, match.start() - 1, match.end() + 1)]
                for r in ranges:
                    for x in range(r.start, r.end):
                        if 0 <= r.line_number < len(lines) and 0 <= x < len(lines[r.line_number]) and isSymbol(lines[r.line_number][x]):
                            foundSymbol = True
            if foundSymbol:
                result += int(match.group())
    return result


def test2(lines):
    result = 0
    adj = defaultdict(list)
    for idx, line in enumerate(lines):
        for match in re.finditer(r"\d+", line):
            if (match.start() > 0 and isSymbol(lines[idx][match.start() - 1])):
                adj[idx, match.start()-1].append(match.group())
            if (match.end() < len(lines[idx]) and isSymbol(lines[idx][match.end()])):
                adj[idx, match.end()].append(match.group())
            ranges = [Range(idx - 1, match.start() - 1, match.end() + 1)] + \
                [Range(idx + 1, match.start() - 1, match.end() + 1)]
            for current_range in ranges:
                for index in range(current_range.start, current_range.end):
                    if 0 <= current_range.line_number < len(lines) and 0 <= index < len(lines[current_range.line_number]) and isSymbol(lines[current_range.line_number][index]):
                        adj[current_range.line_number,
                            index].append(match.group())

    for match_gears in adj.values():
        if len(match_gears) == 2:
            result += int(match_gears[0]) * int(match_gears[1])
    return result


lines = readInput()
print(test1(lines))
print(test2(lines))

from collections import defaultdict
import re


def readInput():
    with open('/Users/nmehrok/Desktop/python/AOC/Input/day4.txt', 'r') as file:
        data = file.read().strip()
    lines = data.split("\n")
    return lines


def part1(lines):
    result = 0
    for line in lines:
        _, input = line.split(": ")
        winning_line, selected_line = input.split(" | ")
        winners = re.findall(r'\d+', winning_line)
        numbers = re.findall(r'\d+', selected_line)
        matches = sum(numbers.count(num) for num in winners)
        if matches > 0:
            result += 2 ** (matches - 1)
    return result


def part2(f):
    cards = defaultdict(int)
    for idx, line in enumerate(f):
        cards[idx] += 1
        _, input = line.split(": ")
        winning_line, selected_line = input.split(" | ")
        winners = re.findall(r'\d+', winning_line)
        numbers = re.findall(r'\d+', selected_line)
        matches = sum(numbers.count(num) for num in winners)
        for delta in range(matches):
            cards[idx+delta+1] += cards[idx]
    return sum(cards.values())


lines = readInput()
print(part1(lines))
print(part2(lines))

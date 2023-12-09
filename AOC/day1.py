
from math import inf


def readInput():
    with open('/Users/nmehrok/Desktop/python/AOC/Input/day1.txt', 'r') as file:
        data = file.read().strip()
    lines = data.split("\n")
    return lines


def findDigitNumber(line):
    from_start_digit = next((x for x in line if x.isdigit()), 0)
    from_end_digit = next((x for x in line[::-1] if x.isdigit()), 0)
    number = int(from_start_digit) * 10 + int(from_end_digit)
    return number

def part1(lines):
    ans = 0
    for line in lines:
        ans += findDigitNumber(line)
    return ans


def part2(lines):
    ans = 0
    nums = "0 zero 1 one 2 two 3 three 4 four 5 five 6 six 7 seven 8 eight 9 nine".split()
    for line in lines:
        first = min(nums, key=lambda x: line.index(x) if x in line else inf)
        last = min(
            nums, key=lambda x: line[::-1].index(x[::-1]) if x in line else inf)
        ans += nums.index(first) // 2 * 10 + nums.index(last) // 2
    return ans


lines = readInput()
print(part1(lines))
print(part2(lines))

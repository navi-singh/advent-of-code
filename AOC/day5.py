from collections import defaultdict
import re
import os


def readInput():
    file_path = os.path.join(os.getcwd(), 'Input', 'day5.txt')
    with open(file_path, 'r') as file:
        data = file.read().strip()
    return data


def find_destination(ranges, input):
    result = next((destination.start + input - source.start for destination,
                  source in ranges if input in source), input)
    return result


#     # for destination, source in ranges:
#     #     if input in source:
#     #         return destination.start + input - source.start


def p1(lines):
    seeds, *mappings = lines.split("\n\n")
    seeds = seeds.split(": ")[1]
    seeds = [int(x) for x in seeds.split()]
    for m in mappings:
        _, *ranges = m.splitlines()
        ranges = [[int(x) for x in r.split()] for r in ranges]
        ranges = [(range(a, a + c), range(b, b + c)) for a, b, c in ranges]

        seeds = [next((destination.start + input - source.start for destination,
                      source in ranges if input in source), input) for input in seeds]

    return min(seeds)


def p2(lines):
    def pairs(l):
        it = iter(l)
        return zip(it, it)
    seeds, *mappings = lines.split("\n\n")
    seeds = seeds.split(": ")[1]
    seeds = [int(x) for x in seeds.split()]
    seeds = [range(a, a + b) for a, b in pairs(seeds)]

    for m in mappings:
        _, *ranges = m.splitlines()
        ranges = [[int(x) for x in r.split()] for r in ranges]
        ranges = [(range(a, a + c), range(b, b + c)) for a, b, c in ranges]
        new_seeds = []

        for r in seeds:
            for tr, fr in ranges:
                offset = tr.start - fr.start
                if r.stop <= fr.start or fr.stop <= r.start:
                    continue
                ir = range(max(r.start, fr.start), min(r.stop, fr.stop))
                lr = range(r.start, ir.start)
                rr = range(ir.stop, r.stop)
                if lr:
                    seeds.append(lr)
                if rr:
                    seeds.append(rr)
                new_seeds.append(range(ir.start + offset, ir.stop + offset))
                break
            else:
                new_seeds.append(r)

        seeds = new_seeds

    return min(x.start for x in seeds)


def part2(f):
    result = 0
    cards = defaultdict(int)

    return result


lines = readInput()
print(p1(lines))
# print(part1(lines))
# print(p2(lines))

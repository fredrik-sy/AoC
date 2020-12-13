import math
import re
import request


def chinese_remainder(n, a):
    p = math.prod(n)
    total = sum(y * pow(p // x, -1, x) * (p // x) for x, y in zip(n, a))
    return total % p


def part_one(schedule):
    (departtime, timestamp) = schedule
    earliesttime = [time - (departtime % time) for time, _ in timestamp]
    i = earliesttime.index(min(earliesttime))
    return timestamp[i][0] * earliesttime[i]


def part_two(schedule):
    (departtime, timestamp) = schedule
    return chinese_remainder([time[0] for time in timestamp], [time[1] for time in timestamp])


if __name__ == '__main__':
    text = request.get('https://adventofcode.com/2020/day/13/input')
    inputs = tuple(int(line) if line.isdigit() else
                   [(int(match.group()), int(match.group()) - i) for i, match in
                    enumerate(re.finditer(r'(\d+|x)', line)) if
                    match.group().isdigit()]
                   for line in text.strip().split('\n'))

    print(part_one(inputs))
    print(part_two(inputs))

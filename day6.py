from functools import reduce
from operator import or_, and_
import request


def part_one(groups):
    return sum(len(reduce(or_, forms)) for forms in groups)


def part_two(groups):
    return sum(len(reduce(and_, forms)) for forms in groups)


if __name__ == '__main__':
    text = request.get('https://adventofcode.com/2020/day/6/input')

    if text:
        inputs = [[set(form) for form in group.split()] for group in text.split('\n\n')]
        print(part_one(inputs))
        print(part_two(inputs))

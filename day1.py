import request


def part_one(entries):
    for a in entries:
        b = 2020 - a

        if b in inputs:
            return a * b


def part_two(entries):
    while entries:
        a = entries.pop()

        for b in entries:
            c = 2020 - a - b

            if c in inputs:
                return a * b * c


if __name__ == '__main__':
    text = request.get('https://adventofcode.com/2020/day/1/input')

    if text:
        inputs = set([int(entry) for entry in text.split()])
        print(part_one(inputs))
        print(part_two(inputs))

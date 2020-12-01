import request


def part_one(entries):
    while entries:
        a = entries.pop()
        b = 2020 - a

        if b in inputs:
            print(a * b)
            return


def part_two(entries):
    while entries:
        a = entries.pop()

        for b in entries:
            c = 2020 - a - b

            if c in inputs:
                print(a * b * c)
                return


if __name__ == '__main__':
    text = request.get('https://adventofcode.com/2020/day/1/input')

    if text:
        inputs = set([int(entry) for entry in text.split()])
        part_one(inputs)
        part_two(inputs)

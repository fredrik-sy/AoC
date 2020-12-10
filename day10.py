import request


def count_ones(numbers):
    count = 0

    for n in numbers:
        if n == 1:
            count += 1
        else:
            yield count
            count = 0


def distinct_arrangements(numbers):
    arrangements = 1

    for n in count_ones(numbers):
        if n == 2:
            arrangements *= 2
        elif n == 3:
            arrangements *= 4
        elif n == 4:
            arrangements *= 7

    return arrangements


if __name__ == '__main__':
    text = request.get('https://adventofcode.com/2020/day/10/input')
    inputs = [int(number) for number in text.strip().split('\n')]
    inputs.extend([0, max(inputs) + 3])
    inputs.sort()
    differences = list(map(lambda a, b: b - a, inputs[0:], inputs[1:]))
    print(differences.count(1) * differences.count(3))
    print(distinct_arrangements(differences))

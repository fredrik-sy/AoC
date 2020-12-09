import request
import itertools


def part_one(numbers):
    preamble = 25

    for i in range(preamble, len(numbers)):
        combinations = set(sum(j) for j in itertools.combinations(numbers[i - preamble:i], 2))

        if numbers[i] not in combinations:
            return numbers[i]


def part_two(numbers):
    invalid_number = part_one(numbers)

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            subset = numbers[i:j + 1]
            subset_sum = sum(subset)

            if subset_sum == invalid_number:
                return min(subset) + max(subset)
            elif subset_sum > invalid_number:
                break


if __name__ == '__main__':
    text = request.get('https://adventofcode.com/2020/day/9/input')
    inputs = [int(number) for number in text.strip().split('\n')]
    print(part_one(inputs))
    print(part_two(inputs))

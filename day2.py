import re
import request


def part_one(passwords):
    valid_passwords = 0

    for (min_count, max_count, letter, password) in passwords:
        count = password.count(letter)

        if min_count <= count <= max_count:
            valid_passwords += 1

    return valid_passwords


def part_two(passwords):
    valid_passwords = 0

    for (i, j, letter, password) in passwords:
        if (password[i - 1] == letter) != (password[j - 1] == letter):
            valid_passwords += 1

    return valid_passwords


if __name__ == '__main__':
    text = request.get('https://adventofcode.com/2020/day/2/input')

    if text:
        inputs = [(int(match.group(1)), int(match.group(2)), match.group(3), match.group(4)) for match in
                  re.finditer(r'(\d+)-(\d+) (\w): (\w+)', text)]
        print(part_one(inputs))
        print(part_two(inputs))

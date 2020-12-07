import re
import request


def part_one(bags):
    count = 0
    stack = ['shiny gold']
    unique = set()

    while stack:
        color = stack.pop()

        for bag, content in bags.items():
            if color in content and bag not in unique:
                unique.add(bag)
                stack.append(bag)
                count += 1

    return count


def part_two(bags, color):
    if bags[color]:
        count = 0

        for color, number in bags[color].items():
            count += number + number * part_two(bags, color)

        return count
    else:
        return 0


def split(content):
    return dict((color, int(number)) for number, color in re.findall(r'(\d+) ([a-z ]+) bags?', content))


if __name__ == '__main__':
    text = request.get('https://adventofcode.com/2020/day/7/input')
    inputs = dict((color, split(content)) for color, content in [tuple(line.split(' bags contain ')) for line in text.strip().split('\n')])
    print(part_one(inputs))
    print(part_two(inputs, 'shiny gold'))

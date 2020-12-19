import request
import re


def part_one(rules, messages):
    patterns = to_patterns(rules)
    count = 0

    for message in messages:
        if re.fullmatch(patterns['0'], message):
            count += 1

    return count


def part_two(rules, messages):
    rules['8'] = '(42)+'
    rules['11'] = ' | '.join([' '.join(['42'] * i) + ' ' + ' '.join(['31'] * i) for i in range(1, 10)])
    patterns = to_patterns(rules)
    count = 0

    for message in messages:
        if re.fullmatch(patterns['0'], message):
            count += 1

    return count


def to_rules(text):
    rules = {}

    for line in text.splitlines():
        (key, value) = line.split(': ')
        rules[key] = value

    return rules


def to_patterns(rules):
    patterns = {}
    items = list(rules.items())

    while items:
        for i in reversed(range(len(items))):
            key, value = items[i]

            if not re.search(r'\d', value):
                if re.search(r'\|', value):
                    patterns[key] = f'({value.replace(" ", "")})'
                else:
                    patterns[key] = value.replace(' ', '')

                items.pop(i)

        for key, value in patterns.items():
            for i in reversed(range(len(items))):
                k, v = items[i]
                m = re.sub(fr'(^|(?<=\(|\s)){key}((?=\s|\))|$)', value, v)

                if m:
                    items[i] = (k, m)

    return patterns


def main():
    text = request.get('https://adventofcode.com/2020/day/19/input')
    inputs = text.strip().replace('"', '').split('\n\n')
    rules = to_rules(inputs[0])
    messages = inputs[1].splitlines()
    print('* Part One:', part_one(rules, messages))
    print('** Part Two:', part_two(rules, messages))


if __name__ == '__main__':
    main()

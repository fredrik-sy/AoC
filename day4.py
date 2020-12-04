import re
import request


def part_one(passports):
    valid = 0

    for passport in passports:
        if {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}.issubset(passport.keys()):
            valid += 1

    return valid


def part_two(passports):
    valid = 0

    for passport in passports:
        if ('byr' in passport and 1920 <= int(passport['byr']) <= 2002
                and 'iyr' in passport and 2010 <= int(passport['iyr']) <= 2020
                and 'eyr' in passport and 2020 <= int(passport['eyr']) <= 2030
                and 'hgt' in passport and re.fullmatch(r'(1[5-8]\d|19[0-3])cm|(59|[6-7]\d|7[0-6])in', passport['hgt'])
                and 'hcl' in passport and re.fullmatch(r'#[0-9a-f]{6}', passport['hcl'])
                and 'ecl' in passport and re.fullmatch(r'amb|blu|brn|gry|grn|hzl|oth', passport['ecl'])
                and 'pid' in passport and re.fullmatch(r'\d{9}', passport['pid'])):
            valid += 1

    return valid


if __name__ == '__main__':
    text = request.get('https://adventofcode.com/2020/day/4/input')

    if text:
        inputs = [dict((pair.group(1), pair.group(2)) for pair in re.finditer(r'(\w+):([^ \n]+)', data)) for data in text.split('\n\n')]
        print(part_one(inputs))
        print(part_two(inputs))

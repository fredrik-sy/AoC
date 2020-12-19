import request

from algorithm import shunting_yard
from operator import add, mul


def main():
    text = request.get('https://adventofcode.com/2020/day/18/input')
    inputs = [line.replace(' ', '') for line in text.strip().split('\n')]

    print('* Part One:',
          sum([shunting_yard(string=line,
                             isoperator=lambda a: a in ('+', '*'),
                             operatorgt=lambda a, b: a != '(',
                             operatordict={'+': add, '*': mul}) for line in inputs]))

    print('** Part Two:',
          sum([shunting_yard(string=line,
                             isoperator=lambda a: a in ('+', '*'),
                             operatorgt=lambda a, b: a == '+' and b == '*',
                             operatordict={'+': add, '*': mul}) for line in inputs]))


if __name__ == '__main__':
    main()

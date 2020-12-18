import request
from math import prod


class Interpreter:
    def __init__(self):
        self.i = None
        self.inputs = None
        self.numbers = []
        self.operators = []
        self.operator_precedence = False

    def parse_int(self):
        h = self.i

        while self.i < len(self.inputs) and self.inputs[self.i].isdigit():
            self.i += 1

        self.numbers.append(int(self.inputs[h:self.i]))

    def parse_operator(self):
        self.operators.append(self.inputs[self.i])
        self.i += 1

    def parse_parentheses(self):
        stack = [True]
        self.i += 1
        h = self.i

        while self.i < len(self.inputs) and stack:
            if self.inputs[self.i] == '(':
                stack.append(True)
            elif self.inputs[self.i] == ')':
                stack.pop()

            self.i += 1

        self.numbers.append(Interpreter().interpret(self.inputs[h:self.i - 1], self.operator_precedence))

    def clear(self):
        self.i = 0
        self.operators.clear()
        self.numbers.clear()

    def interpret(self, inputs, operator_precedence=False):
        self.clear()
        self.inputs = inputs
        self.operator_precedence = operator_precedence

        while self.i < len(self.inputs):
            if self.inputs[self.i].isdigit():
                self.parse_int()
            elif self.inputs[self.i] in ('*', '+'):
                self.parse_operator()
            elif self.inputs[self.i] == '(':
                self.parse_parentheses()
            else:
                self.i += 1

        if operator_precedence:
            return self.exec_ordered_operator()
        else:
            return self.exec_operator()

    def exec_operator(self):
        for i in range(len(self.operators)):
            if self.operators[i] == '+':
                self.numbers[i + 1] = self.numbers[i] + self.numbers[i + 1]
            else:
                self.numbers[i + 1] = self.numbers[i] * self.numbers[i + 1]

        return self.numbers.pop()

    def exec_ordered_operator(self):
        for i in reversed(range(len(self.operators))):
            if self.operators[i] == '+':
                self.numbers[i] = self.numbers[i] + self.numbers[i + 1]
                self.numbers.pop(i + 1)
                self.operators.pop(i)

        return prod(self.numbers)


def main():
    text = request.get('https://adventofcode.com/2020/day/18/input')
    interpreter = Interpreter()
    inputs = [line.replace(' ', '') for line in text.strip().split('\n')]
    print(f'Part 1: {sum([interpreter.interpret(line) for line in inputs])}')
    print(f'Part 2: {sum([interpreter.interpret(line, True) for line in inputs])}')


if __name__ == '__main__':
    main()

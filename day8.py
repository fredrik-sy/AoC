import request

accumulator = 0
address = 0


def acc(value):
    global accumulator, address
    accumulator += value
    address += 1


def nop(value):
    global address
    address += 1


def jmp(offset):
    global address
    address += offset


def part_one(instructions):
    global accumulator, address
    accumulator = 0
    address = 0
    executed = set()

    while address < len(instructions):
        if address in executed:
            return accumulator
        else:
            executed.add(address)

        operation, argument = instructions[address]
        operation(argument)

    return True


def part_two(instructions):
    for i in range(len(instructions)):
        operation, argument = instructions[i]

        if operation == nop:
            instructions[i] = jmp, argument

            if part_one(instructions) is True:
                return accumulator

            instructions[i] = nop, argument
        elif operation == jmp:
            instructions[i] = nop, argument

            if part_one(instructions) is True:
                return accumulator

            instructions[i] = jmp, argument


def to_instruction(instruction):
    return int(instruction) if instruction[0] == '-' or instruction[0] == '+' else globals()[instruction]


if __name__ == '__main__':
    text = request.get('https://adventofcode.com/2020/day/8/input')
    inputs = [tuple(map(to_instruction, instruction.split())) for instruction in text.strip().split('\n')]
    print(part_one(inputs))
    print(part_two(inputs))

import request
from itertools import product

mem1 = {}
mem2 = {}


def bitvalue(iter1, iter2):
    value = 0

    for bit, shift in zip(iter1, iter2):
        value |= bit << shift

    return value


def mask(value):
    mask0 = int(value.replace('X', '0'), 2)
    mask1 = int(value.replace('0', '1').replace('X', '0'), 2)
    bitprod = list(product([0, 1], repeat=value.count('X')))
    bitshifts = [tuple(idx for idx, bit in enumerate(reversed(list(value))) if bit == 'X')] * len(bitprod)
    mask2 = list(bitvalue(bits, shifts) for bits, shifts in zip(bitprod, bitshifts))
    return mask0, mask1, mask2


def mem(address, value, mask0, mask1, mask2):
    mem1[address] = (value & ~mask1) | mask0

    for ma2 in mask2:
        decoded_address = (address & mask1) | mask0 | ma2
        mem2[decoded_address] = value


def run(inputs):
    for line in inputs.strip().split('\n'):
        if line.startswith('mask'):
            mask0, mask1, mask2 = mask(line.replace('mask = ', ''))
        else:
            memory = line.replace('mem[', '').split('] = ')
            mem(int(memory[0]), int(memory[1]), mask0, mask1, mask2)


if __name__ == '__main__':
    text = request.get('https://adventofcode.com/2020/day/14/input')
    run(text)
    print(sum(mem1.values()))
    print(sum(mem2.values()))

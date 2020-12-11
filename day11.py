import request
import sys
from functools import lru_cache
from copy import deepcopy

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


@lru_cache()
def adjacent(x, y, maxsteps):
    adj = []

    for vx, vy in directions:
        ax = x + vx
        ay = y + vy
        steps = 0

        while 0 <= ay < len(inputs) and 0 <= ax < len(inputs[ay]) and steps < maxsteps:
            if inputs[ay][ax] != '.':
                adj.append((ax, ay))
                break

            ax += vx
            ay += vy
            steps += 1

    return adj


def adjacent_occupied(seats, x, y, maxsteps):
    count = 0
    adj = list(adjacent(x, y, maxsteps))

    for ax, ay in adj:
        if seats[ay][ax] == '#':
            count += 1

    return count


def fill_seats(seats, rule=4, maxsteps=1):
    changed = True
    next_seats = deepcopy(seats)

    while changed:
        changed = False

        for y in range(len(seats)):
            for x in range(len(seats[y])):
                if seats[y][x] == '#':
                    if adjacent_occupied(seats, x, y, maxsteps) >= rule:
                        next_seats[y][x] = 'L'
                        changed = True
                    else:
                        next_seats[y][x] = seats[y][x]
                elif seats[y][x] == 'L':
                    if adjacent_occupied(seats, x, y, maxsteps) == 0:
                        next_seats[y][x] = '#'
                        changed = True
                    else:
                        next_seats[y][x] = seats[y][x]

        temp = seats
        seats = next_seats
        next_seats = temp

    return seats


def part_one(seats):
    return sum(row.count('#') for row in fill_seats(seats))


def part_two(seats):
    return sum(row.count('#') for row in fill_seats(seats, 5, maxsteps=sys.maxsize))


if __name__ == '__main__':
    text = request.get('https://adventofcode.com/2020/day/11/input')
    inputs = [list(row) for row in text.strip().split('\n')]
    print(part_one(inputs))
    print(part_two(inputs))

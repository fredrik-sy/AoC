import request
from functools import lru_cache


@lru_cache()
def adjacent3(x, y, z):
    adj = set()

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                if not dx == dy == dz == 0:
                    adj.add((x + dx, y + dy, z + dz))

    return adj


@lru_cache()
def adjacent4(x, y, z, w):
    adj = set()

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dw in range(-1, 2):
                    if not dx == dy == dz == dw == 0:
                        adj.add((x + dx, y + dy, z + dz, w + dw))

    return adj


def next_cycle(active_cubes, adjacent):
    cubes = set().union(*(adjacent(*v) for v in active_cubes))
    next_active = set()

    for cube in cubes:
        adj = adjacent(*cube).intersection(active_cubes)

        if (cube in active_cubes and 2 <= len(adj) <= 3) or len(adj) == 3:
            next_active.add(cube)

    active_cubes.clear()
    active_cubes.update(next_active)


def part_one(cubes):
    active_cubes = set()

    for y in range(len(cubes)):
        for x in range(len(cubes[y])):
            if cubes[y][x] == '#':
                active_cubes.add((x, y, 0))

    for i in range(6):
        next_cycle(active_cubes, adjacent3)

    return len(active_cubes)


def part_two(cubes):
    active_cubes = set()

    for y in range(len(cubes)):
        for x in range(len(cubes[y])):
            if cubes[y][x] == '#':
                active_cubes.add((x, y, 0, 0))

    for i in range(6):
        next_cycle(active_cubes, adjacent4)

    return len(active_cubes)


def main():
    text = request.get('https://adventofcode.com/2020/day/17/input')
    inputs = list(map(lambda line: list(line), text.split()))
    print(f'Part 1: {part_one(inputs)}')
    print(f'Part 2: {part_two(inputs)}')


if __name__ == '__main__':
    main()

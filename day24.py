import request
import numpy as np
import re


def part_one(tiles, instructions):
    for instruction in instructions:
        y = tiles.shape[0] // 2
        x = tiles.shape[1] // 2

        for direction in instruction:
            if direction == 'e':
                x += 2
            elif direction == 'w':
                x -= 2
            else:
                y += 1 if direction[0] == 's' else -1
                x += 1 if direction[1] == 'e' else -1

        tiles[y, x] = not tiles[y, x]

    return tiles.sum()


def part_two(tiles):
    black_tiles = set(tuple(a) for a in np.transpose(tiles.nonzero()))
    white_tiles = set()
    next_black_tiles = set()
    adjacent = {}
    days = 100

    while days > 0:
        for y, x in black_tiles:
            adj = adjacent.setdefault((y, x), {(y, x + 2), (y, x - 2),
                                               (y + 1, x + 1), (y + 1, x - 1),
                                               (y - 1, x + 1), (y - 1, x - 1)})
            black_adj = adj.intersection(black_tiles)
            black_count = len(black_adj)
            white_tiles.update(adj - black_adj)

            if not (black_count == 0 or black_count > 2):
                next_black_tiles.add((y, x))

        for y, x in white_tiles:
            adj = adjacent.setdefault((y, x), {(y, x + 2), (y, x - 2),
                                               (y + 1, x + 1), (y + 1, x - 1),
                                               (y - 1, x + 1), (y - 1, x - 1)})
            black_count = len(adj.intersection(black_tiles))

            if black_count == 2:
                next_black_tiles.add((y, x))

        black_tiles.clear()
        black_tiles.update(next_black_tiles)
        white_tiles.clear()
        next_black_tiles.clear()
        days -= 1

    return len(black_tiles)


def main():
    text = request.get('https://adventofcode.com/2020/day/24/input')
    inputs = [re.findall('e|se|sw|w|nw|ne', line) for line in text.strip().splitlines()]
    tiles = np.zeros((200, 200), np.bool)
    print('* Part One:', part_one(tiles, inputs))
    print('** Part Two:', part_two(tiles))


if __name__ == '__main__':
    main()

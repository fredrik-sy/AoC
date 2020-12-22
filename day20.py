import numpy as np
import heapq
import request

from collections import deque


def adjacent_add(adjacent, tileid, tileside):
    adjacent.setdefault(tuple(tileside), set()).add(tileid)
    adjacent.setdefault(tuple(reversed(tileside)), set()).add(tileid)


def connect_adjacent(tiles):
    possible_adjacent = {}
    adjacent = {}
    adjacent_tileside = {}

    for tileid, tile in tiles.items():
        adjacent_add(possible_adjacent, tileid, tile[0])
        adjacent_add(possible_adjacent, tileid, tile[-1])
        adjacent_add(possible_adjacent, tileid, tile[:, 0])
        adjacent_add(possible_adjacent, tileid, tile[:, -1])

    for tileside, (tileid1, tileid2) in filter(lambda item: len(item[1]) == 2, possible_adjacent.items()):
        adjacent.setdefault(tileid1, set()).add(tileid2)
        adjacent.setdefault(tileid2, set()).add(tileid1)
        adjacent_tileside.setdefault(tileid1, set()).add(tileside)
        adjacent_tileside.setdefault(tileid2, set()).add(tileside)

    return adjacent, adjacent_tileside


def next_border_adjacent(adjacent, tileid):
    pq = []

    for next_tileid in adjacent[tileid]:
        heapq.heappush(pq, (len(adjacent[next_tileid]), next_tileid))

    _, next_tileid = heapq.heappop(pq)
    adjacent[tileid].remove(next_tileid)
    adjacent[next_tileid].remove(tileid)
    return next_tileid


def identify_tileid(adjacent, tileid_image, x, y):
    adjacent_tileids = {tileid_image[y, x] for x, y in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)] if
                        tileid_image[y, x] > 0}

    for tileid, tileids in adjacent.items():
        if tileids.intersection(adjacent_tileids) == adjacent_tileids:
            for adjacent_tileid in adjacent_tileids:
                adjacent[adjacent_tileid].remove(tileid)

            adjacent[tileid].symmetric_difference_update(adjacent_tileids)
            return tileid


def reassemble_tileid_image(adjacent):
    corner = [item[0] for item in adjacent.items() if len(item[1]) == 2]
    tileid = corner.pop(0)
    stack = deque([tileid, next_border_adjacent(adjacent, tileid)])

    while stack[0] != stack[-1]:
        stack.append(next_border_adjacent(adjacent, stack[-1]))

    stack.pop()
    size = min([stack.index(tileid) for tileid in corner]) + 1
    tileid_image = np.zeros((size, size), dtype=np.int64)
    coord = deque()
    coord.extend((x, 0) for x in range(size))
    coord.extend((size - 1, y) for y in range(1, size))
    coord.extend((x, size - 1) for x in range(size - 2, -1, -1))
    coord.extend((0, y) for y in range(size - 2, 0, -1))

    while stack:
        x, y = coord.popleft()
        tileid_image[y, x] = stack.popleft()

    for y in range(1, size - 1):
        for x in range(1, size - 1):
            tileid_image[y, x] = identify_tileid(adjacent, tileid_image, x, y)

    return tileid_image


def reassemble_image(tiles, tileid_image, adjacent_tileside):
    tsize = tileid_image.shape[0]
    size = tsize * (next(iter(tiles.values())).shape[0] - 2)
    image = np.zeros((size, size), dtype=int)

    for y in range(tsize):
        for x in range(tsize - 1):
            align_rotation(tiles, tileid_image, adjacent_tileside, x, y, 1)

    for y in range(tsize):
        align_rotation(tiles, tileid_image, adjacent_tileside, tsize - 1, y, -1, True)

    for x in range(tsize):
        for y in range(tsize - 1):
            align_flipping(tiles, tileid_image, adjacent_tileside, x, y, 1)

    for x in range(tsize):
        align_flipping(tiles, tileid_image, adjacent_tileside, x, tsize - 1, -1, True)

    for y in range(tsize):
        for x in range(tsize):
            tile = tiles[tileid_image[y, x]]
            padding = tile.shape[0] - 2
            image[y * padding:y * padding + padding, x * padding:x * padding + padding] = tile[1:-1, 1:-1]

    return image


def align_flipping(tiles, tileid_image, adjacent_tileside, x, y, yo, reflect=False):
    tile = tiles[tileid_image[y, x]]
    tilepattern = adjacent_tileside[tileid_image[y + yo, x]]

    if reflect:
        while tuple(tile[0]) not in tilepattern:
            tile = np.flip(tile, 0)
    else:
        while tuple(tile[-1]) not in tilepattern:
            tile = np.flip(tile, 0)

    tiles[tileid_image[y, x]] = tile


def align_rotation(tiles, tileid_image, adjacent_tileside, x, y, xo, reflect=False):
    tile = tiles[tileid_image[y, x]]
    tilepattern = adjacent_tileside[tileid_image[y, x + xo]]

    if reflect:
        while tuple(tile[:, 0]) not in tilepattern:
            tile = np.rot90(tile)
    else:
        while tuple(tile[:, -1]) not in tilepattern:
            tile = np.rot90(tile)

    tiles[tileid_image[y, x]] = tile


def to_tiles(strings):
    tiles = {}

    for string in strings:
        tileid, tile = string.split(':', 1)
        tile = [list(map(lambda char: 1 if char == '#' else 0, line)) for line in tile.strip().split('\n')]
        tiles[int(tileid)] = np.array(tile)

    return tiles


def part_one(tileid_image):
    return tileid_image[0, 0] * tileid_image[0, -1] * tileid_image[-1, 0] * tileid_image[-1, -1]


def part_two(tiles, adjacent_tileparts, tileid_image):
    image = reassemble_image(tiles, tileid_image, adjacent_tileparts)
    size = image.shape[0]
    seamonster_count = 0
    seamonster_pattern = '00000000000000000010\n10000110000110000111\n01001001001001001000'
    seamonster = np.array([list(line) for line in seamonster_pattern.split('\n')]).astype(np.int)
    max_rot90 = 8

    while not seamonster_count and max_rot90:
        for y in range(size - seamonster.shape[0]):
            for x in range(size - seamonster.shape[1]):
                if np.all(image[y:y + seamonster.shape[0], x:x + seamonster.shape[1]] & seamonster == seamonster):
                    seamonster_count += 1

        max_rot90 -= 1
        image = np.rot90(image)

        if max_rot90 == 4:
            image = np.flip(image, 0)

    return np.sum(image) - (seamonster_count * np.sum(seamonster))


def main():
    text = request.get('https://adventofcode.com/2020/day/20/input')
    inputs = text.strip().replace('Tile ', '').split('\n\n')
    tiles = to_tiles(inputs)
    adjacent, adjacent_tileside = connect_adjacent(tiles)
    tileid_image = reassemble_tileid_image(adjacent)
    print('* Part One:', part_one(tileid_image))
    print('** Part Two:', part_two(tiles, adjacent_tileside, tileid_image))


if __name__ == '__main__':
    main()

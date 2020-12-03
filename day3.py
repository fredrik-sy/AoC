import request


def part_one(grid, xstep, ystep):
    x = 0
    trees = 0

    for y in range(0, len(grid), ystep):
        if grid[y][x] == '#':
            trees += 1

        x = (x + xstep) % 31

    return trees


def part_two(grid):
    return (part_one(grid, 1, 1) *
            part_one(grid, 3, 1) *
            part_one(grid, 5, 1) *
            part_one(grid, 7, 1) *
            part_one(grid, 1, 2))


if __name__ == '__main__':
    text = request.get('https://adventofcode.com/2020/day/3/input')

    if text:
        inputs = [[point for point in maprow] for maprow in text.split()]
        print(part_one(inputs, 3, 1))
        print(part_two(inputs))

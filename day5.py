import request


def calculate_seatid(boardingpass):
    seatid = 8
    lowerrows = 0
    upperrows = 127
    lowercolumns = 0
    uppercolumns = 7

    for i in range(6):
        if boardingpass[i] == 'F':
            upperrows -= int(round((upperrows - lowerrows) / 2))
        elif boardingpass[i] == 'B':
            lowerrows += int(round((upperrows - lowerrows) / 2))

    for i in range(7, 9):
        if boardingpass[i] == 'L':
            uppercolumns -= int(round((uppercolumns - lowercolumns) / 2))
        elif boardingpass[i] == 'R':
            lowercolumns += int(round((uppercolumns - lowercolumns) / 2))

    seatid *= lowerrows if boardingpass[6] == 'F' else upperrows
    seatid += lowercolumns if boardingpass[9] == 'L' else uppercolumns
    return seatid


def part_one(boardingpasses):
    highest_seatid = 0

    for boardingpass in boardingpasses:
        seatid = calculate_seatid(boardingpass)

        if highest_seatid < seatid:
            highest_seatid = seatid

    return highest_seatid


def part_two(boardingpasses):
    seatids = []

    for boardingpass in boardingpasses:
        seatids.append(calculate_seatid(boardingpass))

    seatids.sort()

    for i in range(len(seatids) - 1):
        if seatids[i] + 1 != seatids[i + 1]:
            return seatids[i] + 1


if __name__ == '__main__':
    text = request.get('https://adventofcode.com/2020/day/5/input')

    if text:
        inputs = [passes for passes in text.split()]
        print(part_one(inputs))
        print(part_two(inputs))

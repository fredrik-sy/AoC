import request


def loop_size(key):
    lsize = 1
    subnumber = 7

    while key != subnumber:
        subnumber = (subnumber * 7) % 20201227
        lsize += 1

    return lsize


def main():
    text = request.get('https://adventofcode.com/2020/day/25/input')
    card_key, door_key = list(map(int, text.strip().splitlines()))
    card_lsize = loop_size(card_key)
    door_lsize = loop_size(door_key)
    ekey = pow(door_key, card_lsize, 20201227)
    print('* Part One:', ekey)


if __name__ == '__main__':
    main()

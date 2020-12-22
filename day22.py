import request

from collections import deque
from operator import mul
from itertools import islice


def read_starting_decks(text):
    decks = []

    for player in text.strip().split('\n\n'):
        cards = player.split(':\n')[1]
        decks.append(deque(map(int, cards.split('\n'))))

    return decks


def play_regular(deck1, deck2):
    while deck1 and deck2:
        card1 = deck1.popleft()
        card2 = deck2.popleft()

        if card1 > card2:
            deck1.extend((card1, card2))
        else:
            deck2.extend((card2, card1))

    winning_deck = deck1 if deck1 else deck2
    return sum(map(mul, winning_deck, range(len(winning_deck), 0, -1)))


def play_recursive(deck1, deck2, subgame=False):
    log = set()

    while deck1 and deck2:
        config = tuple(deck1) + tuple('|') + tuple(deck2)

        if config in log:
            return True
        else:
            log.add(config)

        card1 = deck1.popleft()
        card2 = deck2.popleft()

        if card1 <= len(deck1) and card2 <= len(deck2):
            player1_win = play_recursive(deque(islice(deck1, card1)), deque(islice(deck2, card2)), True)
        else:
            player1_win = card1 > card2

        if player1_win:
            deck1.extend((card1, card2))
        else:
            deck2.extend((card2, card1))

    if subgame:
        return deck1

    winning_deck = deck1 if deck1 else deck2
    return sum(map(mul, winning_deck, range(len(winning_deck), 0, -1)))


def main():
    text = request.get('https://adventofcode.com/2020/day/22/input')
    deck1, deck2 = read_starting_decks(text)
    print('* Part One:', play_regular(deck1.copy(), deck2.copy()))
    print('** Part Two:', play_recursive(deck1, deck2))


if __name__ == '__main__':
    main()

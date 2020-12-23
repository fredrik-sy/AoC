class Node(object):
    def __init__(self, value):
        self.next: Node = None
        self.value = value

    def __repr__(self):
        return self.value.__repr__()

    def pickup(self):
        sequence = set()
        node = self.next

        for _ in range(3):
            sequence.add(node.value)
            node = node.next

        return sequence


def iterate(node, stop):
    while stop:
        node = node.next
        stop -= 1

    return node


def move(cups, head, pickup, destination):
    current = cups[destination]
    pickup_end = iterate(pickup, 2)
    head.next = pickup_end.next
    pickup_end.next = current.next
    current.next = pickup


def play(cups, current, moves):
    maxv = len(cups) - 1

    while moves > 0:
        pickup = current.pickup()
        destination = current.value - 1

        while destination in pickup or destination < 1:
            destination -= 1

            if destination < 1:
                destination = maxv

        move(cups, current, current.next, destination)
        current = current.next
        moves -= 1


def part_one(inputs):
    cups = [Node(i) for i in range(10)]
    head = None
    previous = None
    node = None

    for value in map(int, inputs):
        node = cups[value]

        if head is None:
            head = node

        if previous:
            previous.next = node

        previous = node

    node.next = head
    play(cups, head, 100)
    answer = []
    current = cups[1].next

    while current.value != 1:
        answer.append(current.value)
        current = current.next

    return ''.join(map(str, answer))


def part_two(inputs):
    cups = [Node(i) for i in range(1000001)]
    values = list(map(int, inputs))
    values.extend(range(10, 1000001))
    head = None
    previous = None
    node = None

    for value in values:
        node = cups[value]

        if head is None:
            head = node

        if previous:
            previous.next = node

        previous = node

    node.next = head
    play(cups, head, 10000000)
    return cups[1].next.value * cups[1].next.next.value


def main():
    print('* Part One:', part_one('853192647'))
    print('** Part Two:', part_two('853192647'))


if __name__ == '__main__':
    main()

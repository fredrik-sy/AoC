import numpy
import request
from scipy.ndimage.interpolation import shift

E = 0
S = 1
W = 2
N = 3


class Ship(object):
    def __init__(self):
        self._distance = numpy.array([0, 0, 0, 0])

    def answer(self, navigation):
        for action, value in navigation:
            getattr(self, action)(value)

        return abs(self._distance[N] - self._distance[S]) + abs(self._distance[E] - self._distance[W])


class Part1Ship(Ship):
    def __init__(self):
        super().__init__()
        self._direction = numpy.array([1, 0, 0, 0])

    def N(self, value):
        self._distance[N] += value

    def S(self, value):
        self._distance[S] += value

    def E(self, value):
        self._distance[E] += value

    def W(self, value):
        self._distance[W] += value

    def L(self, value):
        value /= -90
        self._direction = shift(self._direction, value) + shift(self._direction, len(self._direction) + value)

    def R(self, value):
        value /= 90
        self._direction = shift(self._direction, value) + shift(self._direction, -len(self._direction) + value)

    def F(self, value):
        self._distance += self._direction * value


class Part2Ship(Ship):
    def __init__(self):
        super().__init__()
        self._waypoint = numpy.array([10, 0, 0, 1])

    def N(self, value):
        self._waypoint[N] += value

    def S(self, value):
        self._waypoint[S] += value

    def E(self, value):
        self._waypoint[E] += value

    def W(self, value):
        self._waypoint[W] += value

    def L(self, value):
        value /= -90
        self._waypoint = shift(self._waypoint, value) + shift(self._waypoint, len(self._waypoint) + value)

    def R(self, value):
        value /= 90
        self._waypoint = shift(self._waypoint, value) + shift(self._waypoint, -len(self._waypoint) + value)

    def F(self, value):
        self._distance += self._waypoint * value


if __name__ == '__main__':
    text = request.get('https://adventofcode.com/2020/day/12/input')
    inputs = [(line[0], int(line[1:])) for line in text.strip().split('\n')]
    print(Part1Ship().answer(inputs))
    print(Part2Ship().answer(inputs))

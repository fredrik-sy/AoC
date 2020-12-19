from collections import deque
from typing import Callable


def shunting_yard(string: str,
                  isoperator: Callable[[str], bool],
                  operatorgt: Callable[[str, str], bool],
                  operatordict: dict,
                  islbracket: Callable[[str], bool] = lambda a: a == '(',
                  isrbracket: Callable[[str], bool] = lambda a: a == ')') -> deque:
    stack = []
    queue = deque()
    i = 0
    maxsize = len(string)

    while i < maxsize:
        if string[i].isdigit():
            j = i
            i += 1

            while i < maxsize and string[i].isdigit():
                i += 1

            queue.append(int(string[j:i]))
        else:
            if isoperator(string[i]):
                while stack and operatorgt(stack[-1], string[i]):
                    queue.append(stack.pop())

                stack.append(string[i])
            elif islbracket(string[i]):
                stack.append(string[i])
            elif isrbracket(string[i]):
                while not islbracket(stack[-1]):
                    queue.append(stack.pop())

                stack.pop()

            i += 1

    while stack:
        queue.append(stack.pop())

    # Evaluate Reverse Polish notation
    while queue:
        while queue and not isoperator(queue[0]):
            stack.append(queue.popleft())

        b = stack.pop()
        a = stack.pop()
        stack.append(operatordict[queue.popleft()](a, b))

    return stack.pop()

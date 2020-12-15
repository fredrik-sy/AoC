def find(start, stop):
    i = start

    while i <= stop:
        last_nspoken = inputs[-1]
        spoken = nspoken[last_nspoken]

        if len(nspoken[last_nspoken]) == 1:
            inputs.append(0)
            nspoken[0].append(i)
        else:
            value = spoken[-1] - spoken[-2]
            inputs.append(value)

            if value in nspoken:
                nspoken[value].append(i)
            else:
                nspoken[value] = [i]

        i += 1

    return inputs[-1]


if __name__ == '__main__':
    inputs = [None, 18, 11, 9, 0, 5, 1]
    nspoken = dict(zip(inputs[1:], ([j] for j in range(1, len(inputs)))))
    print(f'Part 1: {find(len(inputs), 2020)}')
    print(f'Part 2: {find(len(inputs), 30000000)}')

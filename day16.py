import request


def part_one(fields, tickets):
    error_rate = []
    valid_fields = set()

    for field in fields.values():
        valid_fields.update(field)

    for i in reversed(range(len(tickets))):
        error = set(tickets[i]).difference(valid_fields)
        error_rate.extend(error)

        if error:
            tickets.pop(i)

    return sum(error_rate)


def part_two(fields, your, nearby):
    valid_fields = dict((field, []) for field in fields.keys())

    for i in range(len(nearby)):
        for j in range(len(nearby[i])):
            for field in fields.keys():
                if nearby[i][j] in fields[field]:
                    valid_fields[field].append(j)

    fieldindices = find_indices(valid_fields)

    departure_location = fieldindices['departure location']
    departure_station = fieldindices['departure station']
    departure_platform = fieldindices['departure platform']
    departure_track = fieldindices['departure track']
    departure_date = fieldindices['departure date']
    departure_time = fieldindices['departure time']

    return (your[departure_location]
            * your[departure_station]
            * your[departure_platform]
            * your[departure_track]
            * your[departure_date]
            * your[departure_time])


def find_indices(fields):
    fieldnames = fields.keys()
    probabilities = [None] * (len(fieldnames) + 1)
    remove_idx = set()
    result = {}

    for fieldname in fieldnames:
        probability = [fields[fieldname].count(i) for i in range(len(fieldnames))]
        maxv = max(probability)
        probability = {i for i, count in enumerate(probability) if maxv == count}
        probabilities[len(probability)] = fieldname, probability

    for fieldname, probability in probabilities[1:]:
        probability.difference_update(remove_idx)
        remove_idx.update(probability)
        result[fieldname] = probability.pop()

    return result


def parse_fields(string):
    fields = {}

    for line in string.split('\n'):
        words = line.replace('-', ' ').replace('or ', '').split(': ')
        iterator = iter(words[1].split())
        fields[words[0]] = {j for i in iterator for j in range(int(i), int(next(iterator)) + 1)}

    return fields


def parse_tickets(string):
    return [[int(i) for i in line.split(',')] for line in string.split('\n')[1:]]


if __name__ == '__main__':
    text = request.get('https://adventofcode.com/2020/day/16/input').strip().split('\n\n')
    ticket_fields = parse_fields(text[0])
    your_ticket = parse_tickets(text[1])[0]
    nearby_tickets = parse_tickets(text[2])
    print(f'Part 1: {part_one(ticket_fields, nearby_tickets)}')
    print(f'Part 2: {part_two(ticket_fields, your_ticket, nearby_tickets)}')

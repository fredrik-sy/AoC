import request

from collections import Counter


def part_one(foods):
    allergens = {}
    allergens_counter = {}
    ingredients_counter = []
    possible_allergens = []
    count = 0

    for allergen, ingredient in foods:
        ingredients_counter.extend(ingredient)

        for food in allergen:
            allergens.setdefault(food, []).extend(ingredient)

    for allergen, ingredient in allergens.items():
        allergens_counter[allergen] = Counter(ingredient)

    for allergen, ingredient in allergens_counter.items():
        maxx = max(ingredient.values())
        possible_allergens.extend(map(lambda x: (allergen, x[0]), filter(lambda x: x[1] == maxx, ingredient.items())))

    ingredients_counter = Counter(ingredients_counter)
    correct_allergens = {ingredient for allergen, ingredient in possible_allergens}

    for ingredient, counter in ingredients_counter.items():
        if ingredient not in correct_allergens:
            count += counter

    return possible_allergens, count


def part_two(allergens):
    counter = {}
    correct_allergens = {}

    for allergen, ingredient in allergens:
        counter.setdefault(allergen, set()).add(ingredient)

    while counter:
        allergen, ingredient = min(counter.items(), key=lambda item: len(item[1]))
        ingredient = counter.pop(allergen).pop()
        correct_allergens[allergen] = ingredient

        for value in counter.values():
            value.discard(ingredient)

    return ','.join([correct_allergens[key] for key in list(sorted(correct_allergens.keys()))])


def main():
    text = request.get('https://adventofcode.com/2020/day/21/input')
    inputs = [(set(ingredient[1].split()), set(ingredient[0].split())) for ingredient in
              [line.split(' (contains ') for line in text.strip().replace(')', '').replace(',', '').split('\n')]]
    allergens, count = part_one(inputs)
    print('* Part One:', count)
    print('** Part Two:', part_two(allergens))


if __name__ == '__main__':
    main()

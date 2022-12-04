from collections import Counter


def get_priority(s: str):
    # ord('a') => 97 ... should be 1
    # ord('z') => 122 ... should be 26

    if s.islower():
        return ord(s) - 96

    # ord('A') => 65 ... should be 27
    # ord('Z') => 90 ... should be 52
    if s.isupper():
        return ord(s) - 38

    raise ValueError('Unable to parse string')


def find_shared(first, second):
    # use only unique characters from each half
    first_unique = set(first)
    second_unique = set(second)

    # concat first and half together
    concatted = ''.join(first_unique) + ''.join(second_unique)

    # get duplicate letter
    counter = Counter(concatted)

    # get shared character
    [(letter, count)] = counter.most_common(1)
    assert count == 2

    return letter


def find_shared_badge(group: list):
    # use only unique characters from each rucksack
    unique_rucksacks = list(map(set, group))

    # convert from set to string
    str_rucksacks = list(map(lambda x: ''.join(x), unique_rucksacks))

    # concat all rucksacks together
    concatted = ''.join(str_rucksacks)

    # get duplicate letter
    counter = Counter(concatted)

    # get shared character
    [(letter, count)] = counter.most_common(1)
    assert count == 3

    return letter


with open('input/input.txt') as f:
    sum = 0
    group_lines = []

    for line in f:
        group_lines.append(line.strip())
        if len(group_lines) >= 3:
            badge = find_shared_badge(group_lines)
            sum += get_priority(badge)
            group_lines = []

    print(sum)

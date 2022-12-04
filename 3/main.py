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


with open('input/input.txt') as f:
    lines = f.readlines()

    sum = 0

    for line in lines:
        line = line.strip()

        length = len(line)
        half = int(length / 2)

        first = line[0:half]
        second = line[half:]

        shared = find_shared(first, second)
        priority = get_priority(shared)

        sum += priority

    print(sum)

def rock(s):
    return s == 'A' or s == 'X'


def paper(s):
    return s == 'B' or s == 'Y'


def scissors(s):
    return s == 'C' or s == 'Z'


def points_for_shape(s):
    if rock(s):
        return 1
    if paper(s):
        return 2
    if scissors(s):
        return 3


def points_for_outcome(o, y):
    if rock(y):
        if paper(o):
            return 0
        if scissors(o):
            return 6
        if rock(o):
            return 3

    if paper(y):
        if rock(o):
            return 6
        if scissors(o):
            return 0
        if paper(o):
            return 3

    if scissors(y):
        if rock(o):
            return 0
        if paper(o):
            return 6
        if scissors(o):
            return 3


with open('input/input.txt') as f:
    lines = f.readlines()

    points = 0

    for i, line in enumerate(lines):
        o, y = line.split(' ')
        yourself = y.strip()
        opponent = o.strip()

        points += points_for_shape(yourself)
        points += points_for_outcome(opponent, yourself)

    print(points)

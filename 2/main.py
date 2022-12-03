ROCK = 'A'
PAPER = 'B'
SCISSORS = 'C'

WIN = 'Z'
LOSE = 'X'
DRAW = 'Y'


def rock(s):
    return s == ROCK


def paper(s):
    return s == PAPER


def scissors(s):
    return s == SCISSORS


def lose(s):
    return s == LOSE


def draw(s):
    return s == DRAW


def win(s):
    return s == WIN


def determine_shape(outcome, opponent):
    if win(outcome):
        if rock(opponent):
            return PAPER
        if paper(opponent):
            return SCISSORS
        if scissors(opponent):
            return ROCK

    if draw(outcome):
        if rock(opponent):
            return ROCK
        if paper(opponent):
            return PAPER
        if scissors(opponent):
            return SCISSORS

    if lose(outcome):
        if rock(opponent):
            return SCISSORS
        if paper(opponent):
            return ROCK
        if scissors(opponent):
            return PAPER


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
        _opponent, _outcome = line.split(' ')
        outcome = _outcome.strip()
        opponent = _opponent.strip()

        yourself = determine_shape(outcome, opponent)

        points += points_for_shape(yourself)
        points += points_for_outcome(opponent, yourself)

    print(points)

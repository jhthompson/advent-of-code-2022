COLUMNS = 40
ROWS = 6
OFF = '.'
ON = '#'


def run_cycles(instructions: list):

    crt = [
        [OFF for _ in range(COLUMNS)] for _ in range(ROWS)
    ]

    cycle = 1
    x = 1

    while (len(instructions) > 0):
        instruction: str = instructions.pop(0).strip()

        if instruction.startswith('noop'):
            if visible(cycle - 1, x):
                turn_on(crt, cycle - 1)

            cycle += 1

        if instruction.startswith('addx'):
            _, amount = instruction.split(' ')
            amount = int(amount)

            if visible(cycle - 1, x):
                turn_on(crt, cycle - 1)

            # does work, nothing changes yet
            cycle += 1

            if visible(cycle - 1, x):
                turn_on(crt, cycle - 1)

            # does work, value changes after the cycles completes
            cycle += 1
            x += amount

    return crt


def visible(pixel, sprite_position):
    # only care about x position from 0 - 39
    modified_pixel = pixel % COLUMNS

    return sprite_position - 1 <= modified_pixel <= sprite_position + 1


def turn_on(crt, pixel):
    print(pixel)
    row = (pixel // COLUMNS) % ROWS
    column = pixel % COLUMNS

    crt[row][column] = ON


def print_crt(crt):
    for row in crt:
        row_string = ''
        for column in row:
            row_string += column
        print(row_string)


with open('input/input.txt') as f:

    lines = f.readlines()

    crt = run_cycles(lines)

    print_crt(crt)

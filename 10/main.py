def run_cycles(instructions: list):

    cycle = 1
    x = 1
    signal_strength = 0

    while (len(instructions) > 0):
        instruction: str = instructions.pop(0).strip()

        if instruction.startswith('noop'):
            if (cycle - 20) % 40 == 0:
                signal_strength += cycle * x
            cycle += 1

        if instruction.startswith('addx'):
            _, amount = instruction.split(' ')
            amount = int(amount)

            if (cycle - 20) % 40 == 0:
                # print(cycle)
                signal_strength += cycle * x

            # does work, nothing changes yet
            cycle += 1

            # does work, value changes after the cycles completes
            if (cycle - 20) % 40 == 0:
                # print(cycle)
                signal_strength += cycle * x

            cycle += 1
            x += amount

    return signal_strength


with open('input/input.txt') as f:

    lines = f.readlines()

    signal_strength = run_cycles(lines)

    print(signal_strength)

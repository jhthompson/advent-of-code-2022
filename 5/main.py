from collections import deque
import re


def move_crates(stacks: list, steps: list) -> list:
    num_stacks = (len(stacks[0]) + 1) // 4
    deques = [deque() for i in range(num_stacks)]

    # build up each deque
    for line in stacks:
        for index, character in enumerate(line):
            if (index - 1) % 4 == 0:
                # we're on a stack
                if character != ' ':
                    deque_index = (index + 1) // 4
                    deques[deque_index].appendleft(character)

    step_pattern = re.compile(r'move (\d+) from (\d+) to (\d+)')
    # go through each step and alter the deques
    for step in steps:
        m = step_pattern.match(step)
        num_crates = int(m.group(1))
        starting_stack = int(m.group(2))
        ending_stack = int(m.group(3))

        # move the crates
        for _ in range(num_crates):
            top_crate = deques[starting_stack-1].pop()
            deques[ending_stack-1].append(top_crate)

    return deques


with open('input/input.txt') as f:
    lines = f.readlines()

    separator_index = lines.index('\n')

    initial_stacks = lines[:separator_index-1]
    steps = lines[separator_index+1:]

    final_stacks = move_crates(initial_stacks, steps)

    top_crates = ''
    for i in final_stacks:
        top_crates += i[-1]

    print(top_crates)

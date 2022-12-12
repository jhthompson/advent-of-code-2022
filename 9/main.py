def calculate_number_of_tiles_visited(lines) -> int:
    # treat each point as tuple of (x, y)
    number_of_knots = 10
    knots = [(0, 0) for _ in range(number_of_knots)]

    visited_tiles = set()
    visited_tiles.add((0, 0))

    for line in lines:
        line = line.strip()
        direction, amount = line.split(' ')
        amount = int(amount)

        for _ in range(amount):
            updated_head = move_head(direction, 1, knots[0])
            knots[0] = updated_head

            # move all knots behind the head
            for index, knot in enumerate(knots[1:]):
                # print(f'Moving knot #{index +1} from {knot} to keep up with {knots[index]}')
                updated_knot = move_tail(knots[index], knot)
                knots[index+1] = updated_knot

                if index == len(knots) - 2:
                    visited_tiles.add(updated_knot)

    return len(visited_tiles)


def move_head(direction, amount, head):
    assert direction == 'U' or direction == 'R' or direction == 'D' or direction == 'L'

    x, y = head

    if direction == 'U':
        return (x, y + amount)

    if direction == 'R':
        return (x + amount, y)

    if direction == 'D':
        return (x, y - amount)

    if direction == 'L':
        return (x - amount, y)


def move_tail(head, tail):
    x_head, y_head = head
    x_tail, y_tail = tail

    if touching(head, tail):
        return tail

    # how the tail would need to move to meet the head (x, y)
    vector = (x_head - x_tail, y_head - y_tail)
    x_vector, y_vector = vector

    # up, down, left, or right
    if x_vector == 0:
        return (x_tail, y_tail + 1 if y_vector > 0 else y_tail - 1)
    elif y_vector == 0:
        return (x_tail + 1 if x_vector > 0 else x_tail - 1, y_tail)
    # diagonal
    else:
        # remove one from abs value of largest change
        # add vector to tail to move it
        if abs(x_vector) > abs(y_vector):
            x_vector_to_move = x_vector - 1 if x_vector > 0 else x_vector + 1
            y_vector_to_move = y_vector
        elif abs(y_vector) > abs(x_vector):
            x_vector_to_move = x_vector
            y_vector_to_move = y_vector - 1 if y_vector > 0 else y_vector + 1
        else:
            x_vector_to_move = x_vector - 1 if x_vector > 0 else x_vector + 1
            y_vector_to_move = y_vector - 1 if y_vector > 0 else y_vector + 1

        return (x_tail + x_vector_to_move, y_tail + y_vector_to_move)


def touching(head, tail):
    x_head, y_head = head
    x_tail, y_tail = tail

    return x_tail - 1 <= x_head <= x_tail + 1 and y_tail - 1 <= y_head <= y_tail + 1


with open('input/input.txt') as f:
    lines = f.readlines()

    # calculate number of tiles visited
    print(calculate_number_of_tiles_visited(lines))

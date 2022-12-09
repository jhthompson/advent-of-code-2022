def construct_2d_array(lines: list):
    width = height = len(lines[0].strip())
    trees = [
        [] for _ in range(width)
    ]

    for line_index, line in enumerate(lines):
        line = line.strip()

        for char_index, char in enumerate(line):
            trees[line_index].append(int(char))

    return trees


def compute_best_scenic_score(trees):
    best_scenic_score = 0

    for row_index, row in enumerate(trees):
        for column_index, column in enumerate(row):
            scenic_score = compute_scenic_score(row_index, column_index, trees)
            if scenic_score > best_scenic_score:
                best_scenic_score = scenic_score

    return best_scenic_score


def compute_scenic_score(row_index, column_index, trees) -> int:
    grid_size = len(trees[0])

    tree = trees[row_index][column_index]

    # check left
    i = column_index - 1
    visible_left = 0
    while i >= 0:
        neighbour = trees[row_index][i]
        visible_left += 1

        if neighbour >= tree:
            break

        i -= 1

    # check up
    i = row_index - 1
    visible_up = 0
    while i >= 0:
        neighbour = trees[i][column_index]
        visible_up += 1

        if neighbour >= tree:
            break

        i -= 1

    # check right
    i = column_index + 1
    visible_right = 0
    while i < grid_size:
        neighbour = trees[row_index][i]
        visible_right += 1

        if neighbour >= tree:
            break

        i += 1

    # check down
    i = row_index + 1
    visible_down = 0
    while i < grid_size:
        neighbour = trees[i][column_index]
        visible_down += 1

        if neighbour >= tree:
            break

        i += 1

    return visible_left * visible_up * visible_right * visible_down


with open('input/input.txt') as f:
    lines = f.readlines()

    # construct 2d array
    trees = construct_2d_array(lines)

    # compute number of visible trees
    scenic_score = compute_best_scenic_score(trees)

    print(scenic_score)

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


def compute_visible_trees(trees):
    grid_size = len(trees[0])

    num_visible_trees = 0

    for row_index, row in enumerate(trees):
        for column_index, column in enumerate(row):
            if tree_is_visible(row_index, column_index, trees):
                num_visible_trees += 1

    return num_visible_trees


def tree_is_visible(row_index, column_index, trees):
    grid_size = len(trees[0])

    # tree is on an edge
    if row_index == 0 or column_index == 0 or row_index == grid_size - 1 or column_index == grid_size - 1:
        return True

    tree = trees[row_index][column_index]

    # check left
    i = column_index - 1
    visible_left = True
    while i >= 0 and visible_left:
        neighbour = trees[row_index][i]

        if neighbour >= tree:
            visible_left = False

        i -= 1

    # check up
    i = row_index - 1
    visible_up = True
    while i >= 0 and visible_up:
        neighbour = trees[i][column_index]

        if neighbour >= tree:
            visible_up = False

        i -= 1

    # check right
    i = column_index + 1
    visible_right = True
    while i < grid_size and visible_right:
        neighbour = trees[row_index][i]

        if neighbour >= tree:
            visible_right = False

        i += 1

    # check down
    i = row_index + 1
    visible_down = True
    while i < grid_size and visible_down:
        neighbour = trees[i][column_index]

        if neighbour >= tree:
            visible_down = False

        i += 1

    return visible_left or visible_up or visible_right or visible_down


with open('input/input.txt') as f:
    lines = f.readlines()

    # construct 2d array
    trees = construct_2d_array(lines)

    # compute number of visible trees
    num_visible = compute_visible_trees(trees)

    print(num_visible)

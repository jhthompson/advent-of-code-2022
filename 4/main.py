def fully_contained_range(first: str, second: str) -> bool:
    first_lower, first_upper = map(int, first.split('-'))
    second_lower, second_upper = map(int, second.split('-'))

    # is first contained in second?
    if first_lower >= second_lower and first_upper <= second_upper:
        return True

    # is second contained in first?
    if second_lower >= first_lower and second_upper <= first_upper:
        return True

    # otherwise
    return False


with open('input/input.txt') as f:
    lines = f.readlines()

    num_fully_contained_ranges = 0

    for line in lines:
        line = line.strip()
        first, second = line.split(',')

        if fully_contained_range(first, second):
            print(line)
            num_fully_contained_ranges += 1

    print(num_fully_contained_ranges)

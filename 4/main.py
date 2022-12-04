def overlap(first: str, second: str) -> bool:
    first_lower, first_upper = map(int, first.split('-'))
    second_lower, second_upper = map(int, second.split('-'))

    return (first_lower <= second_upper) and (first_upper >= second_lower)


with open('input/input.txt') as f:
    lines = f.readlines()

    num_overlapping_ranges = 0

    for line in lines:
        line = line.strip()
        first, second = line.split(',')

        if overlap(first, second):
            num_overlapping_ranges += 1

    print(num_overlapping_ranges)

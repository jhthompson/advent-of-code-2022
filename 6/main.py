

from collections import Counter


def find_first_unique_occurence(line: str, window_size: int):
    window = ''

    for index, char in enumerate(line):
        window += char

        if len(window) > window_size:
            window = window[1:]

        if len(window) == window_size:
            freq = Counter(window)

            if (len(freq) == len(window)):
                return index + 1

    return -1


with open('input/input.txt') as f:
    line = f.readline().strip()

    print(find_first_unique_occurence(line, 14))

with open('input/input.txt') as f:
    lines = f.readlines()

    highest = 0
    current = 0

    for line in lines:
        line = line.strip()
        if line:
            current += int(line)
        else:
            if current > highest:
                highest = current
            current = 0

    print(highest)

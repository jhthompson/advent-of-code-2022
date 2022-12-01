with open('input/input.txt') as f:
    lines = f.readlines()

    totals = []
    current = 0

    for line in lines:
        line = line.strip()
        if line:
            current += int(line)
        else:
            totals.append(current)
            current = 0

    totals.sort(reverse=True)
    print(sum(totals[:3]))

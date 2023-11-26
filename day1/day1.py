# INPUT_FILE = 'demo_part1.txt'
INPUT_FILE = 'part1.txt'

total_cals = []
with open(INPUT_FILE, 'r') as fh:
    tot = 0
    for line in fh:
        if line == '\n':
            total_cals.append(tot)
            tot = 0
        else:
            tot += int(line.strip())

print('Solution part 1:')
print(max(total_cals))

print('Solution part 2:')
# print(total_cals)
total_cals.sort(reverse=True)
print(sum(total_cals[:3]))

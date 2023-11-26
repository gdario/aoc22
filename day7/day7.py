from collections import Counter

# INPUT_FILE = 'demo_part1.txt'
INPUT_FILE = 'part1.txt'

with open(INPUT_FILE, 'r') as fh:
    lines = [line.strip() for line in fh.readlines()]
lines = [line.split(' ') for line in lines]

stack = []
sizes = Counter()

for line in lines:
    # breakpoint()
    if line[0].isdigit():
        for d in stack:
            sizes[d] += int(line[0])
    if line[1] == 'cd':
        d = line[2]
        if d == '..':
            stack.pop()
        elif d == '/':
            sizes[d] = 0
            stack.append(d)
        else:
            stack.append(stack[-1] + d + '/')

# print(sizes)
# print(sum([v for v in sizes.values() if v <= 100000]))
tot_avail = 70_000_000
free_space = tot_avail - sizes['/']
needed = 30_000_000
min_size = min([v for v in sizes.values() if v+free_space >= needed])
print(min_size)

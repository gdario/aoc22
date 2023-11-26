from string import ascii_lowercase, ascii_uppercase

# PART1_FILE = 'demo_part1.txt'
PART1_FILE = 'part1.txt'
# PART2_FILE = 'demo_part2.txt'
PART2_FILE = 'part2.txt'

priorities = {k: v for v, k in enumerate(
    list(ascii_lowercase + ascii_uppercase), 1)}


def get_priority(s, p):
    n2 = len(s) // 2
    left, right = s[:n2], s[n2:]
    common = set(left).intersection(set(right))
    return priorities[common.pop()]

# ---------- Part 1 ----------

tot = 0
with open(PART1_FILE, 'r') as fh:
    for line in fh:
        tot += get_priority(line, priorities)

print('Solution part 1:')
print(tot)

# ---------- Part 2 ----------

tot = 0
sets = [0, 0, 0]
with open(PART2_FILE, 'r') as fh:
    for n, line in enumerate(fh, 1):
        sets[n%3] = set(line.strip())
        if n % 3 == 0:
            common = sets[0].intersection(sets[1]).intersection(sets[2])
            tot += priorities[common.pop()]
            sets = [0, 0, 0]

print('Solution part 2:')
print(tot)

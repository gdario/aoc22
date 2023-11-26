# INPUT_FILE = 'demo_part1.txt'
INPUT_FILE = 'part1.txt'

tot1, tot2 = 0, 0

with open(INPUT_FILE, 'r') as fh:
    for line in fh:
        first, second = line.strip().split(',')
        first, second = first.split('-'), second.split('-')
        a, b = int(first[0]), int(first[1])
        c, d = int(second[0]), int(second[1])
        if (b < c) | (d < a):
            continue
        elif ((c >= a) & (d <= b)) | ((c <= a) & (d >= b)):
            tot1 += 1
            tot2 += 1
        else:
            tot2 += 1


print('Solution part 1:')
print(tot1)
print('Solution part 2:')
print(tot2)
# INPUT_FILE = 'demo_part1.txt'
INPUT_FILE = 'part1.txt'

mapping1 = {
    'A X': 4, # Draw
    'A Y': 8, # Win
    'A Z': 3, # Loss
    'B X': 1, # Loss
    'B Y': 5, # Draw
    'B Z': 9, # Win
    'C X': 7, # Win
    'C Y': 2, # Loss
    'C Z': 6  # Draw
}

tot = 0
with open(INPUT_FILE, 'r') as fh:
    for k in fh:
        tot += int(mapping1[k.strip()])

print("Solution part 1:")
print(tot)

mapping2 = {
    'A X': 'A Z',
    'A Y': 'A X',
    'A Z': 'A Y',
    'B X': 'B X',
    'B Y': 'B Y',
    'B Z': 'B Z',
    'C X': 'C Y',
    'C Y': 'C Z',
    'C Z': 'C X'
}

tot = 0
with open(INPUT_FILE, 'r') as fh:
    for k in fh:
        tot += int(mapping1[mapping2[k.strip()]])

print("Solution part 2:")
print(tot)

from copy import deepcopy
import re

# INPUT_FILE = 'demo_part1.txt'
INPUT_FILE = 'part1.txt'

# original_stacks = {
#     1: list('ZN'),
#     2: list('MCD'),
#     3: list('P')
# }

original_stacks = {
    1: list('BWN'),
    2: list('LZSPTDMB'),
    3: list('QHZWR'),
    4: list('WDVJZR'),
    5: list('SHMB'),
    6: list('LGNJHVPB'),
    7: list('JQZFHDLS'),
    8: list('WSFJGQB'),
    9: list('ZWMSCDJ')
}


def read_moves(infile):
    with open(infile, 'r') as fh:
        moves = fh.readlines()
    return [m.strip() for m in moves if m.startswith('m')]


def get_info(move):
    regex = r'move ([0-9]+) from ([0-9]+) to ([0-9]+)'
    tmp = [int(x) for x in re.sub(regex, r'\1 \2 \3', move).split()]
    return tmp[0], tmp[1], tmp[2]


def get_results(stacks):
    result = ''
    for stack in stacks.values():
        result += stack[-1]
    return result


stacks = deepcopy(original_stacks)
moves = read_moves(INPUT_FILE)

for move in moves:
    num, fro, to = get_info(move)
    for _ in range(num):
        x = stacks[fro].pop()
        stacks[to].append(x)



results1 = get_results(stacks)
print('Result part 1:')
print(results1)

# #---------- Part 2 ----------  
stacks = deepcopy(original_stacks)

for move in moves:
    num, fro, to = get_info(move)
    if num == 1:
        tmp = stacks[fro].pop()
        stacks[to].append(tmp)
    elif num > 1:
        tmp = stacks[fro][-num:]
        stacks[to].extend(tmp)
        del stacks[fro][-num:]
    else:
        print("Illegal number of items")
        break

print('Result part 2:')
results2 = get_results(stacks)
print(results2)
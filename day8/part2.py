from pprint import pprint
# INPUT_FILE = 'demo_part1.txt'
INPUT_FILE = 'part1.txt'


def look_left(x: list, i: int, j: int) -> int:
    height = x[i][j]
    tot = 0
    blocked = False
    if j == 0:
        return 0
    while not blocked:
        tot += 1
        j -= 1
        if x[i][j] >= height or j == 0:
            blocked = True
    return tot


def look_right(x: list, i: int, j: int) -> int:
    border = len(x[0]) - 1 # index of the right border
    height = x[i][j]
    tot = 0
    blocked = False
    if j == border:
        return 0
    while not blocked:
        tot += 1
        j += 1
        if x[i][j] >= height or j == border:
            blocked = True
    return tot


def look_up(x: list, i: int, j: int) -> int:
    height = x[i][j]
    tot = 0
    blocked = False
    if i == 0:
        return 0
    while not blocked:
        tot += 1
        i -= 1
        if x[i][j] >= height or i == 0:
            blocked = True
    return tot


def look_down(x: list, i: int, j: int) -> int:
    border = len(x[0]) - 1 # index of the right border
    height = x[i][j]
    tot = 0
    blocked = False
    if i == border:
        return 0
    while not blocked:
        tot += 1
        i += 1
        if x[i][j] >= height or i == border:
            blocked = True
    return tot


def scenic_score(x: list, i: int, j: int) -> int:
    left = look_left(x, i, j)
    right = look_right(x, i, j)
    up = look_up(x, i, j)
    down = look_down(x, i, j)
    return left * right * up * down


grid = []
with open(INPUT_FILE, 'r') as fh:
    for line in fh:
        tmp = [int(x) for x in list(line.strip())]
        grid.append(tmp)

max_score = 0
for i, row in enumerate(grid):
    for j, val in enumerate(row):
        score = scenic_score(grid, i, j)
        if score > max_score:
            max_score = score

print("Solution part 2")
print(max_score)
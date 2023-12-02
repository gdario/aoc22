from pprint import pprint
INPUT_FILE = 'demo_part1.txt'
# INPUT_FILE = 'part1.txt'

grid = []
with open(INPUT_FILE, 'r') as fh:
    for line in fh:
        tmp = [int(x) for x in list(line.strip())]
        grid.append(tmp)

#------------------------------------------------------------------
#                                part 1
#------------------------------------------------------------------

# Grid of visible trees
nrows, ncols = len(grid), len(grid[0])
assert nrows == ncols, "Different number of rows and columns"

# Initialize the visible grid
visible = [[0 for _ in range(ncols)] for _ in range(nrows)]

max_top = [x for x in grid[0]]
max_bottom = [x for x in grid[-1]]
max_left = [row[0] for row in grid]
max_right = [row[-1] for row in grid]

for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if i == 0 or j == 0 or i == nrows - 1 or j == ncols - 1:
            visible[i][j] = 1
        if grid[i][j] > max_left[i]:
            max_left[i] = grid[i][j]
            visible[i][j] = 1
        if grid[i][j] > max_top[j]:
            max_top[j] = grid[i][j]
            visible[i][j] = 1
        if grid[i][ncols-j-1] > max_right[i]:
            max_right[i] = grid[i][ncols-j-1]
            visible[i][ncols-j-1] = 1
        if grid[nrows-i-1][j] > max_bottom[j]:
            max_bottom[j] = grid[nrows-i-1][j]
            visible[nrows-i-1][j] = 1

tot = 0
for row in visible:
    for tree in row:
        tot += tree

print("Solution to part 1:")
print(tot)

#------------------------------------------------------------------
#                                part 2
#------------------------------------------------------------------


def scenic_score(x: list, i: int, j: int):
    pass

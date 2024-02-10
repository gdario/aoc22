# input_file = "day10_demo.txt"
input_file = 'part2.txt'


def get_value(line):
    if line.startswith('addx'):
        val = int(line.split()[1])
        return [0, val]
    else:
        return [0]


grid = [['.' for _ in range(40)] for _ in range(6)]

cycle = 1
x = 1
tot_signal = 0

with open(input_file, 'r') as fh:
    for line in fh:
        for val in get_value(line):
            row, col = divmod(cycle-1, 40)
            # breakpoint()
            if col in [x-1, x, x+1]:
                grid[row][col] = '#'
            cycle += 1
            x += val


res = '\n'.join([''.join(line) for line in grid])
print(res)

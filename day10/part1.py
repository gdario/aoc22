# input_file = "day10_demo.txt"
input_file = "part1.txt"


def get_value(line):
    if line.startswith('addx'):
        val = int(line.split()[1])
        return [0, val]
    else:
        return [0]


cycle = 1
x = 1
tot_signal = 0

with open(input_file, 'r') as fh:
    for line in fh:
        for val in get_value(line):
            if cycle in [20, 60, 100, 140, 180, 220]:
                tot_signal += cycle * x
            cycle += 1
            x += val

print(tot_signal)

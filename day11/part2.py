from collections import deque
import math

input_file = 'part1_demo.txt'
# input_file = 'part1.txt'
N_ROUNDS = 800


class Monkey:
    def __init__(self, config: str, factor=1):
        self.counter = 0
        self.factor = factor
        self.parse(config)

    def operation(self, old):
        return eval(self.foo)

    def do_round(self, monkeys: list):
        while self.items:
            item = self.operation(self.items.pop())
            self.counter += 1
            idx = self.if_true if item % self.divisor == 0 else self.if_false
            monkeys[idx].items.append(item)

    def parse(self, config):
        for line in config.splitlines():
            if not line.startswith('Monkey'):
                _, rhs = line.split(': ')
                if line.startswith('  Starting items'):
                    vals = rhs.split(',') if ',' in rhs else [rhs]
                    self.items = deque([int(val) for val in vals])
                if line.startswith('  Operation'):
                    self.foo = rhs.split('=')[1]
                if line.startswith('  Test'):
                    self.divisor = int(rhs.split('by ')[1])
                if line.startswith('    If'):
                    to = [int(x) for x in rhs if x.isdigit()][0]
                    if 'If true' in line:
                        self.if_true = to
                    if 'If false: ' in line:
                        self.if_false = to


with open(input_file, 'r') as fh:
    configs = fh.read().split('\n\n')

monkeys = [Monkey(config) for config in configs]
for round in range(N_ROUNDS):
    [m.do_round(monkeys) for m in monkeys]

# monkeys.sort(key=lambda x: x.counter, reverse=True)
# print(monkeys[0].counter * monkeys[1].counter)
for n, m in enumerate(monkeys):
    print(f'Monkey {n}: inspected {m.counter} items')

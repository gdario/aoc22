import math


class Monkey:
    def __init__(self, config: str):
        self.parse(config)

    def operation(self, old):
        new = eval(self.foo)
        return math.floor(new/3)

    def parse(self, config):
        for line in config.splitlines():
            if not line.startswith('Monkey'):
                _, rhs = line.split(': ')
                if line.startswith('  Starting items'):
                    vals = rhs.split(',') if ',' in rhs else [rhs]
                    self.items = [int(val) for val in vals]
                if line.startswith('  Operation'):
                    self.foo = rhs.split('=')[1]
                if line.startswith('Test'):
                    self.divisible_by = int(rhs.split('by ')[1])
                if line.startswith('    If'):
                    to = [int(x) for x in rhs if x.isdigit()][0]
                    if 'If true' in line:
                        self.if_true = to
                    if 'If false: ' in line:
                        self.if_false = to


if __name__ == '__main__':
    config = """Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3
"""
    config2 = """Monkey 2:
  Starting items: 79
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3
"""
    monkey = Monkey(config2)

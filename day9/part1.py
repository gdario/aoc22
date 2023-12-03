import math
# INPUT_FILE = 'demo_part1.txt'
# INPUT_FILE = 'demo_part2.txt'
INPUT_FILE = 'part1.txt'

directions = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}


def parse_input(line: str):
    d, n = line.split()
    n = int(n)
    return [directions[d] for _ in range(n)]


class Point:
    def __init__(self, x: int=0, y: int=0):
        self.x = x
        self.y = y
        self.visited = []

    @staticmethod
    def sign(x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0
    
    def dist(self, other):
        return math.hypot(abs(self.x - other.x), abs(self.y - other.y))
    
    def in_contact(self, other):
        return self.dist(other) <= math.sqrt(2)
    
    def compute_step(self, other):
        deltax = other.x - self.x
        deltay = other.y - self.y
        if self.in_contact(other):
            step = (0, 0)
        else:
            step = (self.sign(deltax), self.sign(deltay))
        return step
    
    def step(self, direction: tuple):
        self.x = self.x + direction[0]
        self.y = self.y + direction[1]
    
    def update_position(self, other):
        direction = self.compute_step(other)
        self.step(direction)
        self.visited.append((self.x, self.y))


if __name__ == '__main__':
    knots = [Point() for _ in range(10)]
    # head, tail = Point(), Point()
    with open(INPUT_FILE, 'r') as fh:
        lines = fh.readlines()
    for line in lines:
        steps = parse_input(line.strip())
        for step in steps:
            # ---------- Part 1 ---------- 
            # head.step(step)
            # tail.update_position(head)
    # print(len(set(tail.visited)))
           knots[0].step(step)
           for k in range(1, 10):
               knots[k].update_position(knots[k-1]) 
    print(len(set(knots[-1].visited)))
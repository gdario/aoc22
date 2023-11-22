def first_marker(string: str, nchar: int = 4):
    for i in range(0, len(string) - nchar):
        window = string[i:(i+nchar)]
        if (len(set(window))) == nchar:
            return i + nchar 


if __name__ == '__main__':
    with open('demo_part1.txt', 'r') as fh:
        for line in fh:
            print(first_marker(line.strip()))
    
    with open('part1.txt', 'r') as fh:
        line = fh.readline().strip()
        print('Solution part 1:')
        print(first_marker(line))
        print('Solution part 2:')
        print(first_marker(line, nchar=14))

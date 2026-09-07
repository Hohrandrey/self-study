with open(input(), encoding='utf-8') as f:
    inf = f.readlines()
    c_lines = len(inf)
    c_l = 0
    c_w = 0
    for line in inf:
        line = line.strip().split()
        c_w += len(line)
        for word in line:
            c_l += len(word.strip('.'))

    print('Input file contains:')
    print(f'{c_l} letters')
    print(f'{c_w} words')
    print(f'{c_lines} lines')
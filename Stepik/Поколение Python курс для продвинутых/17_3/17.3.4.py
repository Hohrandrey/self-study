with open(input(), encoding='utf-8') as f:
    for line in f:
        print(sum(map(int, line.split())))
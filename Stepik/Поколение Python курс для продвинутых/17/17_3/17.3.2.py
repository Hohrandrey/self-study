with open(input(), encoding='utf-8') as f:
    lines = f.readlines()[::-1]
    for line in lines:
        print(line.strip())
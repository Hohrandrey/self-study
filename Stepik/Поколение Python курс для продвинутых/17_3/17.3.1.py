with open(input(), encoding='utf-8') as f:
    string = f.readline().strip()[::-1]
    print(string)
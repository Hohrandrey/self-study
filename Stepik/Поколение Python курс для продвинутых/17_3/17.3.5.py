with open(input(), encoding='utf-8') as f:
    n_str = ''
    for elem in f.read():
        if elem.isdigit():
            n_str += elem
        else:
            n_str += ' '
    print(sum(map(int, n_str.split())))
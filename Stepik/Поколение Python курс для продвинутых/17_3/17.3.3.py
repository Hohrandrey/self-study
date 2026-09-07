with open(input(), encoding='utf-8') as f:
    d = f.readlines()
    m_l = len(max(d, key=len))
    f.seek(0)
    for line in d:
        if len(line) == m_l:
            print(line.strip())
s = 15
l = 0
r = 1000

def tern_search():
    global r, l
    while l <= r:
        m1 = l + (r-l)//3
        m2 = r - (r-l)//3
        if m1 == s:
            return m1
        if m2 == s:
            return m2

        if s < m1:
            r = m1 - 1
        elif s > m2:
            l = m2 + 1
        else:
            l = m1 + 1
            r = m2 - 1
    return None


print(tern_search())
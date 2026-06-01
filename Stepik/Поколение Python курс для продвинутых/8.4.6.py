sstr = input()
str_set = set(sstr)

if len(sstr) != len(str_set):
    print('NO')
else:
    print('YES')
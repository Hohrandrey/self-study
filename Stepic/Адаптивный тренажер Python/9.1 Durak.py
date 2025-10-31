cards_val = {
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'J' : 11,
    'Q' : 12,
    'K' : 13,
    'A' : 14
}

inp = input().split()
koz = input()

c1 = inp[0]
c2 = inp[1]

s1 = inp[0][-1]
s2 = inp[1][-1]

if len(c1) == 3:
    val1 = 10
else:
    val1 = cards_val[c1[0]]

if len(c2) == 3:
    val2 = 10
else:
    val2 = cards_val[c2[0]]

if s1 == s2:
    if val1 > val2:
        print('First')
    elif val1 < val2:
        print('Second')
    else:
        print('Error')
else:
    if (koz not in s1) and (koz not in s2):
        print('Error')
    else:
        if koz in s1:
            print('First')
        else:
            print('Second')
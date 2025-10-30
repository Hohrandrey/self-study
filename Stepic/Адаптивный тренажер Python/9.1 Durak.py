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

if inp[0][-1] == inp[1][-1]:
    if cards_val[inp[0][0]] > cards_val[inp[1][0]]:
        print('First')
    elif cards_val[inp[0][0]] < cards_val[inp[1][0]]:
        print('Second')
    else:
        print('Error')
else:
    if (koz not in inp[0][-1]) and (koz not in inp[1][-1]):
        print('Error')
    else:
        if koz in inp[0][-1]:
            print('First')
        else:
            print('Second')
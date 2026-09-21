def fresco_goats(inp_file):
    list_of_col = []

    with open(inp_file, encoding='utf-8') as inp:
        string = inp.readline()
        while string != 'GOATS\n':
            string = inp.readline()
            list_of_col.append(string.strip())

        list_of_goats = list(map(lambda el: el.strip() , inp.readlines()))

    ans = []
    for color in list_of_col:
        if list_of_goats.count(color) / len(list_of_goats) > 0.07:
            ans.append(color)

    with open('answer.txt', 'w', encoding='utf-8') as out:
        print(*sorted(ans), sep='\n', file=out)


fresco_goats('1.txt')
with open('answer.txt') as f:
   print(f.read())
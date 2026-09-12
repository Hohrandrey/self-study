def add_five(inp_file):
    list_of_strings = []
    with open(inp_file, encoding='utf-8') as inp:
        for line in inp:
            line = line.strip().split()
            new_line = f'{line[0]} {int(line[1]) + 5 if int(line[1]) + 5 <= 100 else 100}\n'
            list_of_strings.append(new_line)

    with open('new_scores.txt', 'w', encoding='utf-8') as out_fire:
        for line in list_of_strings:
            out_fire.write(line)

add_five('1.txt')
with open('new_scores.txt') as f:
    print(f.read())
def numbering_write(inp_file):
    with open(inp_file, encoding='utf-8') as inp_file:
        text = inp_file.readlines()

    with open('output.txt', 'w', encoding='utf-8') as out_file:
        c = 1
        for el in text:
            out_file.write(f'{c}) '+el)
            c += 1


numbering_write('1.txt')
with open('output.txt') as f:
    print(f.read())
def write_line(inp_file):
    with open(inp_file, encoding='utf-8') as f:
        line = f.readline()
    with open('output.txt', 'w', encoding='utf-8') as out_file:
        out_file.write(line)

write_line('1.txt')
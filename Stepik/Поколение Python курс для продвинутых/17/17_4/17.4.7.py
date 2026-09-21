def minutes(x):
    res=[int(i) for i in x.split(':')]
    return res[0]*60+res[1]

def write_long_session_users(inp_file):
    with open(inp_file, encoding='utf-8') as f, open('output.txt', 'w') as out:
        for line in f:
            line = line.strip().split(', ')
            if minutes(line[2]) - minutes(line[1]) >= 60:
                out.write(line[0] + '\n')


write_long_session_users('1.txt')
with open('output.txt') as f:
    print(f.read())
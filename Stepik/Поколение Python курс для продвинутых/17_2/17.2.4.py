file = open(input(), 'r', encoding='utf-8')

print(sum(map(lambda line: int(line.rstrip()),file.readlines())))

file.close()
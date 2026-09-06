file = open(input(), 'r', encoding='utf-8')

for line in file:
    print(line.lstrip())

file.close()
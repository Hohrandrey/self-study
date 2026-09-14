res = []

for i in range(int(input())):
    line = list(input())
    line[0] = line[0].lower()
    line = ''.join(line)
    for el in line:
        if el.isupper():
            line = line.replace(el, '_'+el.lower())
    res.append(line)

print(*res, sep='\n')
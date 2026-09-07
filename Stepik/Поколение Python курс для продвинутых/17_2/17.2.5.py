file = open(input(), 'r', encoding='utf-8')

s = 0
for line in file:
    line = line.rstrip().split('\t')
    s += int(line[1])*int(line[2])
print(s)

file.close()
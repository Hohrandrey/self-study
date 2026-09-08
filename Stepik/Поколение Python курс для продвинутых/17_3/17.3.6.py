with open(input(), encoding='utf-8') as f:
    read = f.readlines()


c_li = len(read)
c_w = 0
c_le = 0
for line in read:
    line = line.strip()
    c_w += len(line.split())
    c_le += len(list(filter(str.isalpha, line)))

print('Input file contains:')
print(f'{c_le} letters')
print(f'{c_w} words')
print(f'{c_li} lines')
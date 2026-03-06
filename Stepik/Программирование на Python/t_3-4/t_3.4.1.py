with open('dataset_3363_2.txt', 'r') as file:
    line = file.readline()

res = ''
i = 0

while i < len(line):
    char = line[i]
    i+=1
    num = ''
    while i < len(line) and line[i].isdigit():
        num += line[i]
        i += 1
    res += char * (int(num) if num else 1)

with open('res_2.txt', 'w') as res_file:
    res_file.write(res)
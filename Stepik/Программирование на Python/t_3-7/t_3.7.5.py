res = {}
with open('dataset_3380_5.txt', 'r') as file:
    for line in file:
        line = line.split()
        if line[0] not in res:
            res[line[0]] = []
            res[line[0]].append(int(line[2]))
        else:
            res[line[0]].append(int(line[2]))

with open('res_5.txt', 'w') as file:
    for i in range(11):
        if str(i+1) in res:
            string = str(i+1) + ' ' + str(sum(res[str(i+1)])/len(res[str(i+1)])) + '\n'
            file.write(string)
        else:
            string = str(i+1) + ' -\n'
            file.write(string)
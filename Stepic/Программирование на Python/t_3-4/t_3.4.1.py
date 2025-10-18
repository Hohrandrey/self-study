with open('dataset_3363_2.txt', 'r') as file:
    line = file.readline().strip()

res = {}
for i in range(len(line)):
    if line[i].type() == str:
        int_len = 1
        int_value = ''
        while line[i + int_len].type() == int:
            int_value.join(line[i + int_len])
        print(int_value)
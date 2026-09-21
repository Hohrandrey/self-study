def read_csv(filr_name):
    with open(filr_name ,encoding='utf8') as f:
        f_line = f.readline().strip().split(',')
        file = f.readlines()

    csv_list = []
    for line in file:
        cur_dict = {}
        line = line.strip().split(',')
        for i_word in range(len(line)):
            cur_dict[f_line[i_word]] = line[i_word]
        csv_list.append(cur_dict)
    return csv_list

print(read_csv('9.csv'))
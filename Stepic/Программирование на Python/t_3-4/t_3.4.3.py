sr_mat = 0
sr_fiz = 0
sr_rus = 0
count = 0

sred_pr = []

with open('dataset_3363_4.txt', 'r') as file:
    for line in file:
        sp = line.split(';')
        count = count + 1
        sr_mat += int(sp[1])
        sr_fiz += int(sp[2])
        sr_rus += int(sp[3])
        sred_pr.append(((int(sp[1]) + int(sp[2]) + int(sp[3])) / 3))


with open('test_res_4.txt', 'w') as res_file:
    for i in sred_pr:
        res_file.write(str(i)+"\n")
    res_file.write(str(sr_mat/count) + " " + str(sr_fiz/count) + " " + str(sr_rus/count))
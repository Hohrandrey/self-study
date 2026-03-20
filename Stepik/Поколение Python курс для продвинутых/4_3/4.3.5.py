string = input().split()

res_sp = []

cur_gr = [string[0]]
for i in range(1, len(string)):
    if string[i] == cur_gr[-1]:
        cur_gr.append(string[i])
    else:
        res_sp.append(cur_gr)
        cur_gr = [string[i]]

res_sp.append(cur_gr)

print(res_sp)
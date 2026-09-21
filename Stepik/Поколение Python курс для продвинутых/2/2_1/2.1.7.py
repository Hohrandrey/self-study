num = input()

if len(num) > 3:
    res_num = num[0 : (len(num)) % 3]
    for i in range((len(num)) % 3, len(num), 3):
        res_num += "," + num[i : i + 3]
    res_num = res_num.lstrip(",")
else:
    res_num = num
print(res_num)

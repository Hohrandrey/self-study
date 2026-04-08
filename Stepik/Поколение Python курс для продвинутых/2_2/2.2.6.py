n = int(input())
kit = [int(input()) for _ in range(n)]
res_num = int(input())


res = "НЕТ"
for i in range(n):
    for j in range(i + 1, n):
        if kit[i] * kit[j] == res_num:
            res = "ДА"
            break
    if res == "ДА":
        break
print(res)

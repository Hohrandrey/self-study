dic = {}

res = []
for word in input().split():
    dic[word] = dic.get(word, 0) + 1
    res.append(dic[word])

print(*res)
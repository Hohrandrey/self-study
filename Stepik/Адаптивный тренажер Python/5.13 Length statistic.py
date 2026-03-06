word_list = input().split()

res = {}

for word in word_list:
    if len(word) not in res.keys():
        res[len(word)] = 1
    else:
        res[len(word)] += 1

for pr in sorted(res):
    print(str(pr) + ':', res[pr])
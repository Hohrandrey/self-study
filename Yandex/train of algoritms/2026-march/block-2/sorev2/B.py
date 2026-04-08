string = input()

max_count = -1
res = ""

for i in range(len(string) // 2):
    c = string.count(string[0 : i + 1])
    if max_count <= c:
        max_count = c
        res = string[0 : i + 1]

print(len(res))

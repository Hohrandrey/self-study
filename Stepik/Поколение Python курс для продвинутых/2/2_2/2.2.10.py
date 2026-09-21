n = int(input())

list_res = []

for i in range(n):
    string = input()

    target = "anton"
    pos = 0

    for char in string:
        if pos < len(target) and char == target[pos]:
            pos += 1

    if pos == len(target):
        list_res.append(i + 1)

print(*list_res)

string = input().split()
rash = 1
res = [[]]

while rash <= len(string):
    for i in range(len(string)):
        if i + rash <= len(string):
            res.append(string[i : i + rash])
    rash += 1
print(res)

n = int(input())

res = {}


def is_parent(parent, child):
    if child not in res:
        return False
    if parent == child:
        return True
    for p in res[child]["parents"]:
        if p == parent or is_parent(parent, p):
            return True
    return False


for _ in range(n):
    inp = input().split()
    class_name = inp[0]
    if class_name not in res:
        res[class_name] = {"parents": []}

    if len(inp) > 1:
        parents = inp[2:]
        res[class_name]["parents"].extend(parents)
        for parent in parents:
            if parent not in res:
                res[parent] = {"parents": []}

q = int(input())
for _ in range(q):
    class1, class2 = input().split()
    if is_parent(class1, class2):
        print("Yes")
    else:
        print("No")
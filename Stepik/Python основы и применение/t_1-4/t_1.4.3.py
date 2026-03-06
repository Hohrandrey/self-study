st = {'global': {"parent": None, "variables": set()}}


def create(namespace, parent):
    if namespace not in st:
        st[namespace] = {"parent": parent, "variables": set()}


def add(namespace, var):
    if namespace in st:
        st[namespace]["variables"].add(var)


def get(namespace, var):
    current = namespace
    while current is not None:
        if var in st[current]["variables"]:
            return current
        current = st[current]["parent"]
    return None


inp = int(input())

for i in range(inp):
    data = input().split()
    command = data[0]
    first = data[1]
    second = data[2]

    if command == "create":
        create(first, second)
    elif command == "add":
        add(first, second)
    elif command == "get":
        print(get(first, second))
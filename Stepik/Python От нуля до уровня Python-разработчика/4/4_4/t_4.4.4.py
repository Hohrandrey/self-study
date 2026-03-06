class CustomList:
    def __init__(self, items):
        self._items = items


    def __getitem__(self, idx):
        return self._items[idx]


    def __setitem__(self, idx, value):
        self._items[idx] = value

cl_sp = []
for _ in range(3):
    i = input()
    cl_sp.append(i)
cl = CustomList(cl_sp)
print(cl[0])

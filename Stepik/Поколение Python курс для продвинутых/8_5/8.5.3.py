li = input().split()
li_set = set()
for el in li:
    li_set.add(el.lower().strip(".,;:-?!"))

print(len(li_set))

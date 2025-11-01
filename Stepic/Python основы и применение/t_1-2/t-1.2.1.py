objects = [1, 2, 1, 2, 3] # при отправки решения надо убрать
unique = []
for obj in objects:
    if obj not in unique:
        unique.append(obj)

print(len(unique))
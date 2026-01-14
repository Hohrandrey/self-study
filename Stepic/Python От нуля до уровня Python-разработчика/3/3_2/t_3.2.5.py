sp = 'aeiouy'
inp = input()
count = 0
for el in sp:
    count += inp.count(el)

print(count)
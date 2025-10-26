d = int(input())
right = set()

for _ in range(d):
    right.add(input().lower())

l = int(input())
wrong = set()
for _ in range(l):
    checked = input().lower().split()
    for word in checked:
        if word not in right:
            wrong.add(word)

for word in wrong:
    print(word)
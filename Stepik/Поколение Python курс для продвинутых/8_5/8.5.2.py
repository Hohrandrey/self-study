n = int(input())
st = ''
for _ in range(n):
    st += input().lower()

print(len(set(st)))
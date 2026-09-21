n = int(input())
k = int(input())

result = 0
for i in range(2, n + 1):
    result = (result + k) % i

print(result + 1)

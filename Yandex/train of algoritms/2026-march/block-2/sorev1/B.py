n = int(input())
words = [input() for _ in range(n)]
length = len(words[0])


# Функция проверки: можно ли разбить на пары при заданном k
def check(k):
    if k == 0:
        return True

    counts = {}
    for w in words:
        prefix = w[:k]
        counts[prefix] = counts.get(prefix, 0) + 1

    for c in counts.values():
        if c % 2 != 0:
            return False
    return True


left, right = 0, length
ans = 0

while left <= right:
    mid = (left + right) // 2
    if check(mid):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)
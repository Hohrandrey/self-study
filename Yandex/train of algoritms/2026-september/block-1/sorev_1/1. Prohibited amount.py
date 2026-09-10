def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    cnt = {}

    for num in nums:
        if num in cnt:
            cnt[num] += 1
        else:
            cnt[num] = 1

    visited = set()
    removed = 0

    for x in cnt:
        if x in visited:
            continue

        y = k - x

        if x == y:
            removed += cnt[x] - 1
        elif y in cnt:
            removed += min(cnt[y], cnt[x])

        visited.add(x)
        visited.add(y)

    print(removed)


if __name__ == '__main__':
    main()

n, m, h, w = map(int, input().split())


def min_folds(size, target):
    if size <= target:
        return 0
    folds = 0
    while size > target:
        size = (size + 1) // 2
        folds += 1
    return folds


ans1 = min_folds(n, h) + min_folds(m, w)

ans2 = min_folds(n, w) + min_folds(m, h)

print(min(ans1, ans2))

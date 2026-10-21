def main():
    n = int(input())
    l = 1
    r = n

    while l <= r:
        m = (l + r) // 2
        if m ** 2 < n:
            l = m + 1
        elif m ** 2 > n:
            r = m - 1
        else:
            return m
    return r


if __name__ == '__main__':
    print(main())
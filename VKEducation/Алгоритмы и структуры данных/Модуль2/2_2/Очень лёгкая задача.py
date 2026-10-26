def main():

    def check():
        n = int(input())
        if n < 1:
            return 0
        x, y = map(int, input().split())
        left = 0
        right = n-1 * max(x, y)

        while left + 1 < right:
            mid = (left + right) // 2
            if mid//x + mid//y < n-1:
                left = mid
            else:
                right = mid
        return right + min(x, y)
    print(check())


if __name__ == "__main__":
    main()

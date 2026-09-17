def main():
    data = list(map(int, input().split()))
    n = data[0]
    row = data[1:n+1]
    stack = []
    min_gist = max(n * min(row), max(row))
    for index, rectangle in enumerate(row):
        if not stack:
            stack.append((index, rectangle))
        else:
            stack.append((index, rectangle))
    print(min_gist)
    print(stack)


if __name__ == '__main__':
    main()

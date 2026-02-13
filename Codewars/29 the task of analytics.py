def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    a, b, c = map(int, input().split())

    deskriminant = (b ** 2) - 4 * a * c

    if deskriminant < 0:
        print(0)
    elif deskriminant == 0:
        print(1)
        print(-b/(2*a))
    else:
        print(2)
        x1 = round((-b + (deskriminant ** 0.5)) / (2 * a), 6)
        x2 = round((-b - (deskriminant ** 0.5)) / (2 * a), 6)
        ls = sorted([x1, x2])
        for elem in ls:
            print(elem, end=' ')




if __name__ == '__main__':
    main()

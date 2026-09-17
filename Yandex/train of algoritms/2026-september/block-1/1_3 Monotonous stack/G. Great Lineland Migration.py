"""
9
7 2 4 5 3 2 5 1 5
"""
def main():
    input()
    string = list(map(int, input().split()))
    stack = []
    ans = []
    for index, el in enumerate(string):
        if not stack:
            stack.append((index, el))
        else:
            while stack and el < stack[-1][1]:
                ans.append((stack.pop()[0], index))
            stack.append((index, el))
    for el in stack:
        ans.append((el[0], -1))
    print(*map(lambda el: el[1], sorted(ans)))

if __name__ == '__main__':
    main()

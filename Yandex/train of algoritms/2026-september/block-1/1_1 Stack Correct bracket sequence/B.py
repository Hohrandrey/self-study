def main():
    dict_of_brackets = {'}':'{', ']':'[', ')':'('}
    n = int(input())
    w = input()
    s = input()

    stack = []

    for el in s:
        if el not in dict_of_brackets:
            stack.append(el)
        else:
            if stack and stack[-1] == dict_of_brackets[el]:
                stack.pop()


    while len(s) < n:
        for br in w:
            if br not in dict_of_brackets and len(stack)+1<=n-len(s):
                stack.append(br)
                s += br
                break
            elif br in dict_of_brackets and stack and stack[-1] == dict_of_brackets[br]:
                stack.pop()
                s += br
                break
    print(s)


if __name__ == '__main__':
    main()

import sys


def main():
    dict_of_brackets = {}

    n = int(input())
    w = input()
    s = input()
    res_string = ''

    for elem in w:
        if elem == '(':
            dict_of_brackets[elem] = ')'
        elif elem == '[':
            dict_of_brackets[elem] = ']'
        elif elem == '{':
            dict_of_brackets[elem] = '}'
        elif elem == ')':
            dict_of_brackets[elem] = '('
        elif elem == ']':
            dict_of_brackets[elem] = '['
        elif elem == '}':
            dict_of_brackets[elem] = '}'

    if len(s) == n:
        return s
    elif len(s) == n//2:
        res_string += s
        for elem in s[::-1]:
            res_string += dict_of_brackets[elem]
        return res_string
    else:
        pass



if __name__ == '__main__':
    print(main())

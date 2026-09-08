import sys

from fontTools.misc.plistlib import end_string


def main():
    dict_of_brackets_front = {'(': ')', '[': ']', '{': '}'}
    dict_of_brackets_backs = {')': '(', ']': '[', '}': '{'}

    n = int(input())
    w = input()
    s = input()

    if len(s) == n:
        return s
    else:
        start_string = s
        end_string = ''

        while len(start_string) != n/2:
            """
            добивать строку основываясь на приоритете до половины длины
            
            if w[0] in dict_of_brackets_backs:
                if start_string[-1] in dict_of_brackets_front:
                    start_string += w[0]
                else:
                    start_string += dict_of_brackets_backs[w[0]]
            else:
                if start_string[-1] in dict_of_brackets_front:
                    start_string += dict_of_brackets_front[w[0]]
                else:
                    start_string += w[0]
            """

        for el in start_string:
            if el in dict_of_brackets_backs:
                end_string += dict_of_brackets_backs[el]
            else:
                end_string += dict_of_brackets_front[el]

        res_string = start_string + end_string[::-1]
        return res_string





if __name__ == '__main__':
    print(main())

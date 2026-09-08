import sys

def main():
    dict_of_brackets = {}
    inp_str = input()
    stack = []  

    if inp_str == '':
        return ''
    else:
        start = 0
        for i in range(len(inp_str)):
            if inp_str[i] == '<':
                start = i
            elif inp_str[i] == '>':
                end = i




if __name__ == '__main__':
    print(main())

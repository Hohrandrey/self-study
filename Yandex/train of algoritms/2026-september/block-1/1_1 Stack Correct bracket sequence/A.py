def main():
    dict_of_brackets = {'}':'{', ']':'[', ')':'('}
    str_to_check = input()

    def check(string, stack = [str]):
        for char in string:
            if char not in dict_of_brackets:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return 'no'
                else:
                    if stack[-1] == dict_of_brackets[char]:
                        stack.pop()
                    else:
                        return 'no'

        if len(stack) != 0:
            return 'no'
        return 'yes'

    print(check(str_to_check))

if __name__ == '__main__':
    main()

def main():
    string = input()
    dict_of_postfix = {'!':3 , '&':2, '|':1, '^':1, '(':-1}
    def create_postfix(string):
        res = []
        stack_of_expressions=[]
        i = 0
        n = len(string)
        while i < n:
            el = string[i]
            if el.isdigit() and el in ('0', '1'):
                j = i
                while j < n and string[j].isdigit() and string[j] in ('0', '1'):
                    j += 1
                res.append(int(string[i:j]))
                i = j
            elif el == ' ':
                i += 1
            elif el in ('!', '&', '|', '^'):
                if not stack_of_expressions:
                    stack_of_expressions.append(el)
                    i += 1
                else:
                    while stack_of_expressions and dict_of_postfix[stack_of_expressions[-1]] >= dict_of_postfix[el]:
                        res.append(stack_of_expressions.pop())
                    stack_of_expressions.append(el)
                    i += 1
            elif el == '(':
                stack_of_expressions.append(el)
                i += 1
            elif el == ')':
                if '(' in stack_of_expressions:
                    while stack_of_expressions and stack_of_expressions[-1] != '(':
                        res.append(stack_of_expressions.pop())
                    stack_of_expressions.pop()
                    i += 1
                else:
                    return 'WRONG'
            else:
                return 'WRONG'

        if '(' in stack_of_expressions:
            return 'WRONG'

        while stack_of_expressions:
            res.append(stack_of_expressions.pop())
        return res

    cr_string = create_postfix(string)
    stack = []
    if cr_string == 'WRONG':
        print('WRONG')
        return

    for el in cr_string:
        if isinstance(el, int):
            stack.append(el)
        elif el == '!':
            if len(stack) < 1:
                print('WRONG')
                return
            op = stack.pop()
            stack.append(1 - op)
        elif el in ('&', '|', '^'):
            if len(stack) < 2:
                print('WRONG')
                return
            op2 = stack.pop()
            op1 = stack.pop()
            if el == '&':
                stack.append(op1 & op2)
            elif el == '|':
                stack.append(op1 | op2)
            elif el == '^':
                stack.append(op1 ^ op2)

    if not stack or len(stack) != 1:
        print('WRONG')
        return
    else:
        print(stack[0])

if __name__ == '__main__':
    main()

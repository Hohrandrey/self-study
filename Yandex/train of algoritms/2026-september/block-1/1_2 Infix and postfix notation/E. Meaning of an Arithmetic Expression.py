def main():
    string = input()
    dict_of_priority = {'+':0, '-':0, '*':1, '/':1, '(':-1}
    def create_postfix(string):
        res = ''
        stack_of_expressions=[]
        for elem in string:
            if elem in '+-*/()':
                if elem in '+-*/':
                    if len(stack_of_expressions) == 0:
                        stack_of_expressions.append(elem)
                    else:
                        while stack_of_expressions and dict_of_priority[stack_of_expressions[-1]] >= dict_of_priority[elem]:
                            res += stack_of_expressions.pop()
                        stack_of_expressions.append(elem)
                elif elem == '(':
                    stack_of_expressions.append(elem)
                elif elem == ')':
                    while stack_of_expressions and stack_of_expressions[-1] != '(':
                        res += stack_of_expressions.pop()
                    stack_of_expressions.pop()
            elif elem.isdigit():
                res+=elem
            elif elem == ' ':
                continue
            else:
                return 'WRONG'
        while stack_of_expressions:
            res += stack_of_expressions.pop()
        return res

    cr_string = create_postfix(string)
    if cr_string == 'WRONG':
        print('WRONG')
        return
    stack = []

    for elem in cr_string:
        if elem.isdigit():
            stack.append(int(elem))
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            match elem:
                case '+':
                    stack.append(op1 + op2)
                case '-':
                    stack.append(op1 - op2)
                case '*':
                    stack.append(op1 * op2)
                case '/':
                    stack.append(op1 / op2)

    if len(stack) == 1:
        print(stack.pop())
        return
    else:
        print('WRONG')
        return

if __name__ == '__main__':
    main()

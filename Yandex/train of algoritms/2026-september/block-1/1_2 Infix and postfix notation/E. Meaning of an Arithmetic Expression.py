def main():
    string = input()
    dict_of_priority = {'+':0, '-':0, '*':1, '/':1, '(':-1}
    def create_postfix(string):
        res = []
        stack_of_expressions=[]
        i = 0
        n = len(string)
        while i < n:
            elem = string[i]
            if elem in '+-*/':
                if not stack_of_expressions:
                    stack_of_expressions.append(elem)
                    i += 1
                else:
                    while stack_of_expressions and dict_of_priority[stack_of_expressions[-1]] >= dict_of_priority[elem]:
                        res.append(stack_of_expressions.pop())
                    stack_of_expressions.append(elem)
                    i += 1
            elif elem == '(':
                stack_of_expressions.append(elem)
                i += 1
            elif elem == ')':
                if '(' in stack_of_expressions:
                    while stack_of_expressions and stack_of_expressions[-1] != '(':
                        res.append(stack_of_expressions.pop())
                    stack_of_expressions.pop()
                    i += 1
                else:
                    return 'WRONG'
            elif elem.isdigit():
                j = i
                while j < n and string[j].isdigit():
                    j += 1
                num_str = string[i:j]
                val = int(num_str)
                res.append(val)
                i = j
            elif elem == ' ':
                i += 1
            else:
                return 'WRONG'

        if '(' in stack_of_expressions:
            return 'WRONG'

        while stack_of_expressions:
            res.append(stack_of_expressions.pop())
        return res

    cr_string = create_postfix(string)
    if cr_string == 'WRONG':
        print('WRONG')
        return

    stack = []

    for elem in cr_string:
        if isinstance(elem, int):
            stack.append(elem)
        else:
            if len(stack) < 2:
                print('WRONG')
                return
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
                    if op2 == 0:
                        print('WRONG')
                        return
                    stack.append(op1 // op2)

    if len(stack) == 1:
        print(stack.pop())
        return
    else:
        print('WRONG')
        return

if __name__ == '__main__':
    main()

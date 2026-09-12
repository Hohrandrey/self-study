def main():
    string = input().split()
    stack = []
    for el in string:
        if el.isdigit():
            stack.append(int(el))
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            match el:
                case '+':
                    stack.append(op1 + op2)
                case '-':
                    stack.append(op1 - op2)
                case '*':
                    stack.append(op1 * op2)
                case '/':
                    stack.append(op1 / op2)
    print(stack.pop())


if __name__ == '__main__':
    main()

class ExtendedStack(list):
    def check_length(self):
        return len(self) >= 2

    def sum(self):
        # операция сложения
        if self.check_length():
            top1 = self.pop()
            top2 = self.pop()
            self.append(top1 + top2)

    def sub(self):
        # операция вычитания
        if self.check_length():
            top1 = self.pop()
            top2 = self.pop()
            self.append(top1 - top2)

    def mul(self):
        # операция умножения
        if self.check_length():
            top1 = self.pop()
            top2 = self.pop()
            self.append(top1 * top2)

    def div(self):
        # операция целочисленного деления
        if self.check_length():
            top1 = self.pop()
            top2 = self.pop()
            self.append(top1 // top2)


stack = ExtendedStack()
sp = [1, 2, 3, 4, 5, 6]
stack.extend(sp)
stack.append(7)
print(stack)
stack.sum()
print(stack)
stack.sub()
print(stack)
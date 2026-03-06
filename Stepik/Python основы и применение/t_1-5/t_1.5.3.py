class Buffer:
    def __init__(self):
        # конструктор без аргументов
        self.sp = []


    def add(self, *a):
        # добавить следующую часть последовательности
        for i in a:
            self.sp.append(i)
            c = len(self.sp) // 5
            while c > 0:
                sum = 0
                for i in range(c*5):
                    sum += self.sp[i]
                self.sp = self.sp[c*5:]
                c -= 1
                if sum != 0:
                    print(sum)


    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
        return self.sp


buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
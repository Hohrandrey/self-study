class Employee:
    def work(self):
        print("Работает...")


class Developer(Employee):
    def work(self):
        super().work()
        print("Пишет код")


Developer().work()

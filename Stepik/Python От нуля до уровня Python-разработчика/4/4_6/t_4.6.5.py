class Employee():
    def __init__(self, name):
        self.name = name


    def get_salary(self):
        return 0


class HourlyEmployee(Employee):
    def __init__(self, name, hours, rate):
        super().__init__(name)
        self.hours = hours
        self.rate = rate


    def get_salary(self):
        return self.hours * self.rate


class SalariedEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary


    def get_salary(self):
        return self.salary


class Manager(SalariedEmployee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus


    def get_salary(self):
        return super().get_salary() + self.bonus


def print_report(employees: list):
    for employee in employees:
        print(f"Сотрудник: {employee.name}, зарплата: {employee.get_salary()}")


h = HourlyEmployee("Иван", hours=160, rate=500)
s = SalariedEmployee("Анна", salary=80000)
m = Manager("Ольга", salary=100000, bonus=20000)

print_report([h, s, m])

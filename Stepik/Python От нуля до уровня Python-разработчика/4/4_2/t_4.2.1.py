class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def introduce(self):
        print(f"Меня зовут {self.name}, мне {self.age} лет.")


name = input()
age = int(input())

me = Person(name, age)
me.introduce()
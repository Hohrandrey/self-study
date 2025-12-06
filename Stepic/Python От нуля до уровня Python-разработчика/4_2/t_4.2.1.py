class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def introduce(self):
        print(f"Меня зовут {self.name}, мне {self.age} лет.")


name = input("Как вас зовут?")
age = int(input("Сколько вам лет?"))

me = Person(name, age)
me.introduce()
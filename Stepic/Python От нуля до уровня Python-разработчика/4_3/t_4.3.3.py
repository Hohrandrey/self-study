class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age


    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if 150 >= age >= 0:
            self._age = age
        else:
            raise ValueError


name = input()
initial_age = int(input())
new_age = int(input())
person = Person(name, initial_age)

person.age = new_age

print(f"Имя: {person.name}, возраст: {person.age}")
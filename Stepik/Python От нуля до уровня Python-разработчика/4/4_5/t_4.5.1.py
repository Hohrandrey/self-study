class Vehicle:
    def move(self):
        print("Транспорт едет")


class Car(Vehicle):
    def move(self):
        print("Автомобиль едет")

car = Car()
car.move()

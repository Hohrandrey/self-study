class Square:
    def area(self):
        print("Площадь квадрата")


class Circle:
    def area(self):
        print("Площадь круга")


class Triangle:
    def area(self):
        print("Площадь треугольника")

objects = [Square(), Circle(), Triangle()]
for obj in objects:
    obj.area()

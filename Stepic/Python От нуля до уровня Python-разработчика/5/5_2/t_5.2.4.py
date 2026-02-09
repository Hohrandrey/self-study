from abc import ABC, abstractmethod


class Drawable(ABC):
    @abstractmethod
    def draw(self) -> None:
        ...


class Square(Drawable):
    def draw(self):
        print("Рисую квадрат")


class Triangle(Drawable):
    def draw(self):
        print("Рисую треугольник")


def draw_all(ls):
    for l in ls:
        l.draw()

ls = [Square(), Triangle()]
draw_all(ls)

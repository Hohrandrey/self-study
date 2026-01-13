class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


    @property
    def S(self):
        return self.width * self.height


    def __eq__(self, other):
        return self.S == other.S


    def __lt__(self, other):
        return self.S < other.S

width = int(input())
height = int(input())
r1 = Rectangle(width, height)
r2 = Rectangle(width=1, height=10)
print(r1 < r2)
print(r1 == r2)

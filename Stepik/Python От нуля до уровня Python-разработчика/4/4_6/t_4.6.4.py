class Bird:
    def fly(self):
        print("Лечу как птица")


class Airplane:
    def fly(self):
        print("Лечу как самолёт")


class Superman:
    def fly(self):
        print("Лечу как Супермен")


def make_fly(obj):
    obj.fly()

b = Bird()
a = Airplane()
superman = Superman()
make_fly(b)
make_fly(a)
make_fly(superman)

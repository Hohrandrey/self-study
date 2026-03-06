class Animal:
    def move(self):
        print("оно двигается")


class Bird(Animal):
    def move(self):
        print("Птица летит")


class Mammal(Animal):
    def move(self):
        print("Млекопитающее бежит")


bird = Bird()
bird.move()
mammal = Mammal()
mammal.move()

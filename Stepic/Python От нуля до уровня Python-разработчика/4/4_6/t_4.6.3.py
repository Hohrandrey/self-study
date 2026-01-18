class Human:
    def walk(self):
        print("Иду как человек")


class Robot:
    def walk(self):
        print("Иду как робот")


def go(obj):
    obj.walk()

human = Human()
robot = Robot()
go(human)
go(robot)

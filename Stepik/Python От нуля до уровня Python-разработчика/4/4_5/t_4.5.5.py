class Singing:
    def sing(self):
        print('Пою')


class Dancing:
    def dance(self):
        print("Танцую")


class Performer(Singing, Dancing):
    def perform(self):
        self.sing()
        self.dance()


performer = Performer()
performer.perform()

class Painter:
    def paint(self):
        print("Рисую картину")


class Writer:
    def write(self):
        print("Пишу текст")


class Artist(Painter, Writer):
    pass

artist = Artist()
artist.paint()
artist.write()

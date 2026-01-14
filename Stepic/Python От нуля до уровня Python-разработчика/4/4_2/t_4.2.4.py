class Library:
    location = "No location"
    def __init__(self):
        self.books = []


    def add_book(self, title):
        self.books.append(title)


    @classmethod
    def set_location(cls, loc):
        cls.location = loc


    @staticmethod
    def info():
        return "Library system v1.0"


obj = Library()
obj.add_book('1984')
obj.add_book('Pride and Prejudice')
Library.set_location('City Center')

print(Library.info())
print(f'Location: {Library.location}')
print(f"Books: {obj.books}")

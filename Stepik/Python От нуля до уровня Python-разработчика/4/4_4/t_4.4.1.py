class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


    def __str__(self):
        return f"Книга: {self.title}"


    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"


title = input()
author = input()
book = Book(title, author)
print(book)
print(repr(book))

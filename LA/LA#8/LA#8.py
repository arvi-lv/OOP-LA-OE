class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("Ang", "Bobong")
book2 = Book("Harry Mother", "Me")

print(book1.title)
print(book1.author)
print(book1.author)
del book1.author
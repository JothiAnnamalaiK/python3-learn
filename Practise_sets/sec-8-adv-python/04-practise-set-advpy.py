"""
4. Magic/Dunder Methods
    1. Create a class Book with attributes title and author .
        Implement __str__() so that printing the object displays "Title by
        Author" .
        Implement __len__() so that len(book) returns the length of the title.
    2. Create two Book objects and test these methods.
"""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return str(f"{self.title} by {self.author}")

    def __len__(self):
        return len(self.title)


b1 = Book("JoJo", "Jothi Annamalai")
b2 = Book("vivi jojo", "vijay")


print("printing magic str for book 1: ", b1)
print("printing magic len for book 1: ", len(b1))


print("printing magic str for book 2: ", b2)
print("printing magic len for book 2: ", len(b2))

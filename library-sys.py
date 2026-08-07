class library:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title} {self.pages} Author: {self.author}"

    def display(self):
        print("Book:", self.title)
        print("Author:", self.author)
        print("Pages:", self.pages)


b1 = library("Python Basics", "Kushal", 450)
b2 = library("DBMS", "Captain", 230)
b3 = library("DAA", "Homnath", 443)

b1.display()
b2.display()
b3.display()

books = [b1, b2, b3]

for book in books:
    book.display()
    print()
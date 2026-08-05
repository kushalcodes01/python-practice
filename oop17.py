class Book:

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title} {self.pages}"


b1 = Book("Python Basics", 250)

print(b1)
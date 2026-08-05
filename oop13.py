class Shape:

    def __init__(self,length):
        self.length = length

class Rectangle(Shape):

    def __init__(self, length, breadth):
        super().__init__(length)
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Square(Shape):

    def __init__(self, length):
        super().__init__(length)

    def area(self):
        return self.length * self.length

r = Rectangle(7,6)
s = Square(5)

print(r.area())
print(s.area())
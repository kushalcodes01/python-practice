class Person:

    def __init__(self,name,Address):
        self.name = name
        self.Address = Address

class Student(Person):
    pass

s1= Student("Kushal", "Nepal")

print(s1.name)
print(s1.Address)
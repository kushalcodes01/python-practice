class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

class student(Person):

    def __init__(self, name, age, semester):
        super().__init__(name, age)
        self.semester = semester


s1 = student("Kushal", 20,5)

print(s1.name)
print(s1.age)
print(s1.semester)
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
            print("Name:", self.name)
            print("Age:", self.age)

class Student(Person):

    def __init__(self, name, age, semester):
        super().__init__(name, age)
        self.semester = semester

    def display(self):
       super().display()
       print("Semester:",self.semester)

class Teacher(Person):

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display(self):
        super().display()
        print("Salary:", self.salary)


s1 = Student("Kushal", 20, 5)
t1 = Teacher("Shadananda", 50, 50000)

print("-----Student------")
s1.display()

print("-----Teacher------")
t1.display()
class Person:

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

class student(Person):

    def __init__(self, name, age, address, semester):
        super().__init__(name, age, address)
        self.semester = semester

    def display_s(self):
        return self.semester

class teacher(Person):

    def __init__(self, name, age, address, salary):
        super().__init__(name, age, address)
        self.salary = salary

    def display_t(self):
        return self.salary

s1 = student("Kushal", 20, "Biratchowk", 5)

t1 = teacher("Shadananda", 25, "Dingla", 50000)

print(s1.name)
print(s1.age)
print(s1.display_s())
print(t1.name)
print(t1.display_t())
class Student:

    def __init__(self,name):
        self.name = name

    def introduce(self):
        print("My name is ", self.name)

s1 = Student("Kushal")

s1.introduce()
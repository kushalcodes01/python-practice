class Student:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

s1 = Student("Kushal")

print(s1.get_name())
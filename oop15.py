class Student():

    def __init__(self, name):
        self.name = name

    def __len__(self):
        return len(self.name)

s1 = Student("Kushal")

print(len(s1))
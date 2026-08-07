class Person:

    def __init__(self, name,age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Employee(Person):

    def __init__(self, name, age, emp_id):
        super().__init__(name,age)
        self.emp_id = emp_id

    def display(self):
        super().display()
        print("Emp_ID:",self.emp_id)

class Manager(Employee):

    def __init__(self, name, age,emp_id,Department):
        super().__init__(name,age,emp_id)
        self.Department = Department

    def display(self):
        super().display()
        print("Department:", self.Department)

E1 = Employee("Aaryan", 26, 101)
M1 = Manager("Kushal", 20, 103,"HR Manager")

E1.display()
print("-----------")
M1.display()

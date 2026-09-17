class Student:


    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            grade="Excellent"

        elif self.marks >= 60:
            grade ="Good"

        elif self.marks >= 40:
            grade="Pass"

        else:
            grade ="Fail"

        return grade

    def show_report(self):
        grade = self.get_grade()
        print(f"Name: {self.name} \n Marks : {self.marks} \n Grade: {grade}")

student1 = Student("Kushal", 87)
student2 = Student("Charlie", 90)

student1.show_report()
student2.show_report()
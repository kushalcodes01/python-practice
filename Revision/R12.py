class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            grade = "Excellent"

        elif self.marks >= 60:
            grade = "Good"

        elif self.marks >= 40:
            grade = "Pass"

        else:
            grade = "Fail"

        return grade

    def show_report(self):
        grade = self.get_grade()

        print(f"Name : {self.name} \n Marks : {self.marks} \n Grade : {grade}\n")


student1= Student("Kushal", 98)
student2 = Student("Harry", 78)
student3 = Student("Kelly", 89)
student4 = Student("Antoni", 34)

students = [student1, student2, student3, student4]


def show_all_students(students):
    for student in students:
        student.show_report()

def find_student(students, name):
    for student in students:
        if name == student.name:
            return student

    return None

show_all_students(students)

result = find_student(students, "Kushal")

if result:
    result.show_report()
else:
    print("Student not found")
students = {
    "Kushal": 85,
    "Rahul": 37,
    "Aman": 72,
    "Priya": 91
}

def student_report(name):

    marks = students.get(name)

    if marks is None:
        return "Invalid Name"

    grade = ""
    if marks >= 90:
        grade = "Excellent"

    elif marks >= 60:
        grade = "Good"

    elif marks >= 40:
        grade = "Pass"

    else:
        grade = "Fail"

    return name, marks, grade
print(student_report("Kushal"))
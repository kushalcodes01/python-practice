students = {
    "Kushal": 85,
    "Rahul": 37,
    "Aman": 72,
    "Priya": 91,
    "Riya": 44
}


def search_std(name):

    marks = students.get(name)

    if marks is None:
        return "Name not found"

    grade = ""

    if marks >= 90:
        grade = "Excellent"

    elif marks >= 60:
        grade = "Good"

    elif marks >= 40:
        grade = "Pass"

    else:
        grade = "Fail"

    return f"Name: {name}\nMarks: {marks}\nGrade: {grade}"


print(search_std("Kushal"))
print(search_std("Priya"))
print(search_std("Alex"))
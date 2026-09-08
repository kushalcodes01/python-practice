students = {
    "Kushal": 85,
    "Rahul": 37,
    "Aman": 72,
    "Priya": 91,
    "Riya": 44
}

def generate_reports():

    for name, marks in students.items():

        grade = ""

        if marks >= 90:
            grade = "Excellent"

        elif marks >= 60:
            grade = "Good"

        elif marks >= 40:
            grade = "Pass"

        else:
            grade = "Fail"

        print( f"Name : {name} - Marks : {marks} - Grade : {grade}")

generate_reports()

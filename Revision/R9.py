students = {
    "Kushal": 85,
    "Rahul": 37,
    "Aman": 72,
    "Priya": 91,
    "Riya": 44
}

def analyze_students():

    Total_Student = len(students)

    total_marks = sum(students.values())
    highest = max(students.values())
    lowest = min(students.values())
    average = total_marks / Total_Student
    print (f"Total: {Total_Student}\n total_marks : {total_marks}\n highest : {highest}\n lowest :{lowest}\n Average : {average} ")

analyze_students()


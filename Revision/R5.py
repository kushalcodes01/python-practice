students = {
    "Kushal": 85,
    "Rahul": 37,
    "Aman": 72,
    "Priya": 91,
    "Riya": 44
}

for name, marks in students.items():

    print(name) 
    print(marks)

    if marks >= 90:
        print("Excellent")

    elif marks >= 60 and marks <= 89:
        print("Good")

    elif marks >= 40 and marks <= 59:
        print("Pass")
    else:
        print("Fail")


print("Total Students:", len(students))
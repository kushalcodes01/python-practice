import json

student = {
    "name" : "Kushal",
    "semester" : 5
}

file = open("student.json", "w")

json.dump(student, file)
file.close()
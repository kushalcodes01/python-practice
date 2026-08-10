import json

student = {
    "name" : "Kushal",
    "Semester" : 6
}

json_data = json.dumps(student)

print(json_data)
print(type(json_data))
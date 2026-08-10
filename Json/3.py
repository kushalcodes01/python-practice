import json

student = {
    "name" : "Kushal",
    "Semester" : 5
}

file = open("student.json", "w")

json_data = json.dumps(student)
json.dump(json_data, file)
python_data = json.loads(json_data)
json.load(python_data, file)

file.close()
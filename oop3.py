class student:

    def __init__(self,student_id,name,semester):
        self.student_id = student_id
        self.name = name
        self.semester = semester

s1 = student("101", "Kushal", 5)
s2 = student("102", "Subrat", 7)

print("ID:", s1.student_id)
print("Name:", s1.name)
print("Semester:", s1.semester)

print("--------------")

print("ID:", s2.student_id)
print("Name:", s2.name)
print("Semseter:", s2.semester)

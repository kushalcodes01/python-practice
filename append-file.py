file = open("students.txt","a")
name = input("Enter Name:")
file.write("\n" + name)
file.close()

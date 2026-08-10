import sqlite3

conn = sqlite3.connect("school.db")

cursor = conn.cursor()

search_id = input("Enter ID:")

cursor.execute(
    "SELECT * FROM student WHERE student_id = ?",
    (search_id,)
)

data = cursor.fetchall()

print(data)

conn.close()

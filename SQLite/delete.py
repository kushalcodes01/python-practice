import sqlite3

conn = sqlite3.connect("school.db")

cursor = conn.cursor()

cursor.execute("""
DELETE FROM student
WHERE student_id = '101'
""")

conn.commit()

print("Deleted successfully")

cursor.execute("SELECT * FROM student")
print(cursor.fetchall())

conn.close()
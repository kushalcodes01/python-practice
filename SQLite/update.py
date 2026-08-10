import sqlite3

conn = sqlite3.connect("school.db")

cursor = conn.cursor()

cursor.execute("""
UPDATE student
SET semester = 6
WHERE student_id = '101'
""")

conn.commit()

print("Updated successfully")

conn.close()
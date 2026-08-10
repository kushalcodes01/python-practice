import sqlite3

conn = sqlite3.connect("school.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS student(
    student_id TEXT PRIMARY KEY,
    name TEXT,
    semester INTEGER
)
""")

cursor.execute("""
INSERT INTO student
VALUES ('101', 'kushal', 5)
""")
cursor.execute("""
INSERT INTO student
VALUES ('102', 'Tara', 5)
""")

cursor.execute("""
INSERT INTO student
VALUES ('103', 'Subrat', 5)
""")

conn.commit()

print("Table Created")

conn.close()
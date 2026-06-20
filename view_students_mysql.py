import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shreya@8902",
    database="student_tracker"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

for student in students:
    print(student)

cursor.close()
conn.close()
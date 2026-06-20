import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shreya@8902",
    database="student_tracker"
)

cursor = conn.cursor()

name = input("Enter student name to update: ")
new_marks = input("Enter new marks: ")

query = "UPDATE students SET marks = %s WHERE name = %s"

cursor.execute(query, (new_marks, name))

conn.commit()

if cursor.rowcount > 0:
    print("Student marks updated successfully!")
else:
    print("Student not found")

cursor.close()
conn.close()
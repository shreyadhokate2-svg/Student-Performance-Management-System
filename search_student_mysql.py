import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shreya@8902",
    database="student_tracker"
)

cursor = conn.cursor()

name = input("Enter student name: ")

query = "SELECT * FROM students WHERE name = %s"
cursor.execute(query, (name,))

results = cursor.fetchall()

if results:
    for row in results:
        print(row)
else:
    print("Student not found")

cursor.close()
conn.close()
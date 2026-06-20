import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shreya@8902",
    database="student_tracker"
)

cursor = conn.cursor()

name = input("Enter Student Name: ")
marks = int(input("Enter Marks: "))

query = "INSERT INTO students (name, marks) VALUES (%s, %s)"
values = (name, marks)

cursor.execute(query, values)

conn.commit()

print("Student Added Successfully!")

cursor.close()
conn.close()
from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shreya@8902",
        database="student_tracker"
    )

@app.route("/")
def home():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()

    return render_template("index.html", students=students)

@app.route("/add", methods=["POST"])
def add_student():

    name = request.form["name"]
    marks = request.form["marks"]

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students(name, marks) VALUES(%s,%s)",
        (name, marks)
    )

    conn.commit()
    conn.close()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
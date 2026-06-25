from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def connect():
    return mysql.connector.connect(
        host="mysql-34277b27-shreyadhokate2-8f8d.h.aivencloud.com",
        port=26664,
        user="avnadmin",
        password="PASTE_THE_ACTUAL_AIVEN_PASSWORD_HERE",
        database="defaultdb"
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
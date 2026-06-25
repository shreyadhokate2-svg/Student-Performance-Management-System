import pymysql

conn = pymysql.connect(
    host="mysql-34277b27-shreyadhokate2-8f8d.h.aivencloud.com",
     port=26660,
    user="avnadmin",
    password="AVNS_ronhaTvwprzl75v_NQq",
    database="defaultdb"
)

print("CONNECTED")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    marks INT
)
""")

conn.commit()

print("TABLE CREATED")

cursor.close()
conn.close()
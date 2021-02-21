import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "afrah",
    password = "12345678",
    database = "3pai"
)

myc = mydb.cursor()
myc.execute("SELECT * FROM OP_People LIMIT 10 ")

res = myc.fetchall()
for x in res:
    print(x)
    
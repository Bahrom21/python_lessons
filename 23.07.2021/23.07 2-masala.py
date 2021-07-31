import mysql.connector

myDb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="17121979",
    database="maktab"
)
mycursor = myDb.cursor()
mycursor.execute("select fio,maoshi,manzili from oqituvchi")
myresult = mycursor.fetchall()
for i in myresult:
    print(i)
    

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="17121979"
)

mycursor = mydb.cursor()
mycursor.execute("show databases")  # fetching data -> bazagi malumot b/n ishlash
bazalar = []

for db in mycursor:
    bazalar.append(db[0])

print(bazalar)

if "test" in bazalar:
    print("bor")
    mycursor.execute("drop database test")
    print("o'chirildi")
else:
    print("yaratildi")
    mycursor.execute("create database test")
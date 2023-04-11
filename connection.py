import mysql.connector

data_base = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='seaflix2'
)

cursor = data_base.cursor()

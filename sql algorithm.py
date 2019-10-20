import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="youusername",
    passwd="yourpassword"
)

print(mydb)

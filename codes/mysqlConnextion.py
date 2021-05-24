import mysql.connector

myDb=mysql.connector.connect(host="localhost",user="root",passwd="Abhilas@2020",database="celebrity")

myCursor=myDb.cursor()

myCursor.execute("select * from user")

result=myCursor.fetchall()

print(type(result))
for i in result:
    print(i)
    #print(type(i))
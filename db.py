import mysql.connector as c
con = c.connect(host = 'localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'x')

cursor = con.cursor()

# if con.is_connected():
#     print("Connected")

name = input("Enter the name")
age = int(input("Enter the age"))
marks = float(input("Enter the marks"))

# query
query = "insert into mukul values ('{}',{},{})".format(name,age,marks)
cursor.execute(query)
con.commit()
print("Data entered successfully!!")



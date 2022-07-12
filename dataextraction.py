import mysql.connector as c
con = c.connect(host = 'localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'x')

cursor = con.cursor()

query = "select * from mukul"

# query
cursor.execute(query)

# fetchone
# fetchall
# fetchmany
data1 = cursor.fetchone()
print(data1)
# data2 = cursor.fetchall()
# print(data2)

# data3 = cursor.fetchmany(2)
# print(data3)



# con.commit()
# print("Data entered successfully!!")



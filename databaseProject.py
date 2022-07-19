import mysql.connector as c
con = c.connect(host = 'localhost',
                user='root',
                passwd = 'Ankit@8285',
                database = 'xbank')

cursor = con.cursor()

print("***************  WELCOME TO XBANK ******************\n")







while True:
    choice = int(input("1.Open Account\n2.Cash Deposit\n3.Cash Withdrawl\n4.Account Details\n5.Exit"))
    # 1 Open account
    if choice == 1:
        name = input("Enter the name")
        age = int(input("Enter the age"))
        address = input("Enter the address")
        account = int(input("Enter the amount"))

        query = "Insert into user values ('{}',{},'{}',{})".format(name,age,address,account)
        cursor.execute(query)
        con.commit()
        print("Account Open Successfully!!")

    # cash deposit
    # name
    # amount
    elif choice == 2:
        name = input("enter the name")
        amt = int(input("Enter the amount"))

        query = "Update user set account = {} where name = '{}'".format(amt,name)

        cursor.execute(query)
        con.commit()
        print("Cash Deposit!!")

    # cash withdrawl
    # name
    # amount

    elif choice == 3:
        name = input("enter the name")
        amt = int(input("Enter the amount"))

        query = "Update user set account = {} where name = '{}'".format(amt,name)

        cursor.execute(query)
        con.commit()
        print("Cash Withdrawl!!")


    #     Account details
    elif choice == 4:
        query = "select * from user"
        cursor.execute(query)

        acc_details = cursor.fetchone()
        print(acc_details)











    # exit
    elif choice == 5:
        print("You are out of the Bank")
        break
        # print("You are out of the Bank")
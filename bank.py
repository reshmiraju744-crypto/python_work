
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
    database="bank"
)
import random
from operator import truediv

account_number = random.randint(1000000000, 9999999999)

cursor = mydb.cursor()

# admin module
def insert_worker():
    sql="insert into worker(name,email,phn,salary,join_date,role,password) values(%s,%s,%s,%s,%s,%s,%s)"
    name=input("Enter the name :")
    email=input("Enter the email ID")
    phn = input("Enter the phn number:")
    salary=input("Enter the salary amount:")
    join_date=input("Enter the join date:")
    role=input("Enter the role:")
    password=input("Enter password:")
    val=(name,email,phn,salary,join_date,role,password)
    cursor.execute(sql,val)
    mydb.commit()
    print(cursor.rowcount,"Record inserted successfully")

def update_worker():
    worker_id = int(input("Enter the election ID to update:"))
    sql="update worker set salary=%s,role=%s where worker_id=%s"
    role = input("Enter the role:")
    salary = input("Enter the salary amount:")
    val=(worker_id,role,salary)
    cursor.execute(sql,val)
    mydb.commit()
    print(cursor.rowcount,"Record updated successfully")


def delete_worker():
    worker_id = int(input("Enter the worker ID to delete:"))
    sql="delete from worker where worker_id=%s"
    cursor.execute(sql,(worker_id,))
    mydb.commit()
    if cursor.rowcount > 0:
        print(f"Record deleted successfully. Rows affected: {cursor.rowcount}")
    else:
        print("No matching record found to delete.")


# customer module
def add_acct():
    sql="insert into account(first_name,last_name,address,email,phn,dob,aadhar,account_no,open_bal,total_bal)values(%s,%s,%s,%s,%s,%s,%s,%s,1000,1000)"
    f_name=input("Enter first name :")
    l_name = input("Enter last name :")
    address=input("Enter the address:")
    email=input("Enter the email ID")
    phn = input("Enter the phn number:")
    dob=input("Enter the dob:")
    aadhar=input("Enter the aadhar:")
    account_no=account_number
    val=(f_name,l_name,address,email,phn,dob,aadhar,account_no)
    cursor.execute(sql,val)
    mydb.commit()
    print(cursor.rowcount,"Record inserted successfully")


def delete_acct():
    acc_no = int(input("Enter the account number to delete :"))
    sql="delete from account where account_no=%s"
    cursor.execute(sql,(acc_no,))
    mydb.commit()
    if cursor.rowcount > 0:
        print(f"Record deleted successfully. Rows affected: {cursor.rowcount}")
    else:
        print("No matching record found to delete.")

def update_acct():
    acc_no = int(input("Enter the account number to update:"))
    sql="update account set first_name=%s,last_name=%s,address=%s,email=%s,phn=%s,dob=%s,aadhar=%s where account_no=%s"
    f_name=input("Enter first name :")
    l_name = input("Enter last name :")
    address=input("Enter the address:")
    email=input("Enter the email ID")
    phn = input("Enter the phn number:")
    dob=input("Enter the dob:")
    aadhar=input("Enter the aadhar:")
    val=(acc_no,f_name,l_name,address,email,phn,dob,aadhar)
    cursor.execute(sql,val)
    mydb.commit()
    print(cursor.rowcount,"Record updated successfully")




def trans():
    print("What do you want!!\n1.Deposit\n2.Withdrawal\n3.Check Balance\n4.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        acc_no = int(input("Enter the account number:"))
        amount = int(input("Enter the amount:"))
        sql="insert into transactions(account_no,transaction_type,amount)values(%s,'Deposit',%s)"
        cursor.execute(sql,(acc_no,amount))
        update_sql = "UPDATE account SET total_bal = total_bal + %s WHERE account_no = %s"
        cursor.execute(update_sql, (amount, acc_no))
        mydb.commit()
    elif ch==2:
        acc_no = int(input("Enter the account number:"))
        amount = int(input("Enter the amount:"))
        sql = "insert into transactions(account_no,transaction_type,amount)values(%s,'Withdrawal',%s)"
        cursor.execute(sql, (acc_no,amount))
        update_sql="update account set total_bal = total_bal - %s where account_no = %s"
        cursor.execute(update_sql, (amount,acc_no))
        mydb.commit()
    elif ch==3:
        acc_no = int(input("Enter the account number:"))
        sql="select total_bal from account where account_no=%s"
        cursor.execute(sql,(acc_no,))
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
    elif ch==4:
        print("Exiting")
    else:
        print("Invalid Choice")

def admin_log():
    email=input("Enter your Email ID:")
    passw=input("Enter your password:")
    cursor.execute("SELECT * FROM admin WHERE email=%s AND password=%s",
                   (email, passw))
    result = cursor.fetchone()
    if cursor.rowcount > 0:
        print("Logged in successfully.")
    else:
        print("No matching record found.")

    while 1:
        print("1.Add worker\n2.Update worker\n3.Delete Worker\n4.View Worker Details\n5.View Holder Details\n6.Exit")
        ch=int(input("Enter your choice:"))
        if ch==1:
            insert_worker()
        elif ch==2:
            update_worker()
        elif ch==3:
            delete_worker()
        elif ch == 4:
            cursor.execute("select * from worker")
            result = cursor.fetchone()
        elif ch==5:
            cursor.execute("select * from account")
            result = cursor.fetchone()
        elif ch==6:
            print("Exiting....")
            break
        else:
            print("Invalid choice!!")

def manager_log():
    email = input("Enter your Email ID:")
    passw = input("Enter your password:")
    sql="SELECT * FROM worker WHERE email=%s AND password=%s"
    val=(email, passw)
    cursor.execute(sql,val)
    result = cursor.fetchone()
    if cursor.rowcount > 0:
        print("Logged in successfully.")
    else:
        print("No matching record found.")
    while 1:
        print("1.Add worker\n2.Update worker\n3.Delete Worker\n4.View Worker Details\n5.View Holder Details\n6.Add account\n7.Update account\n8.Delete Account\n9.Exit")
        ch = int(input("Enter your choice:"))
        if ch == 1:
            insert_worker()
        elif ch == 2:
            update_worker()
        elif ch == 3:
            delete_worker()
        elif ch == 4:
            cursor.execute("select * from worker")
            result = cursor.fetchone()
        elif ch == 5:
            cursor.execute("select * from account")
            result = cursor.fetchone()
        elif ch==6:
            add_acct()
        elif ch==7:
            update_acct()
        elif ch==8:
            delete_acct()
        elif ch == 9:
            print("Exiting....")
            break
        else:
            print("Invalid choice!!")

def worker_log():
    email = input("Enter your Email ID:")
    passw = input("Enter your password:")
    cursor.execute("SELECT * FROM worker WHERE email=%s AND password=%s",
                   (email, passw))
    result = cursor.fetchone()
    if cursor.rowcount > 0:
        print("Logged in successfully.")
    else:
        print("No matching record found.")
    while 1:
        print("1.Update\n2.Delete \n3.View Details\n4.Exit")
        ch=int(input("Enter your choice:"))
        if ch==1:
            update_worker()
        elif ch==2:
            delete_worker()
        elif ch == 3:
            cursor.execute("select * from worker where email=%s and passw=%s")
            result = cursor.fetchone()
        elif ch==4:
            print("Exiting....")
        else:
            print("Invalid choice!!")

def acc_holder():
    acco_num=int(input("Enter your account number:"))
    cursor.execute("select * from account where account_no=%s",(acco_num,))
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)

while 1:
    print("Login portal!!")
    print("Do you want to login as \n1.Admin\n2.Manager\n3.worker\n4.Account Holder\n5.Exit")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        admin_log()
    elif ch == 2:
        manager_log()
    elif ch == 3:
        worker_log()
    elif ch==4:
        acc_holder()
    elif ch == 5:
        print("Exiting....")
    else:
        print("Invalid choice!!")


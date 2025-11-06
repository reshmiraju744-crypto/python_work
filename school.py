import mysql.connector
# from django.contrib.auth import logout

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
    database="demo"
)


cursor = mydb.cursor()


#Inserting student details
def stud_insert():
    sql = "INSERT INTO student (first_name,last_name,gender,dob,class,address,phone_number,email,password) VALUES (%s, %s,%s,%s,'10th std',%s,%s,%s,%s)"
    fname = input("Enter your First Name:")
    lname = input("Enter your Last Name:")
    gender=input("Gender:")
    dob=input("DOB")
    address = input("Enter your address:")
    phone_number=input("Enter your phn number: ")
    email = input("Enter your email:")
    password = input("Enter the password:")

    val= (fname,lname,gender,dob,address,phone_number,email,password)
    cursor.execute(sql,val)

    mydb.commit()
    print(cursor.rowcount, "record inserted")




# updating a student details
def stud_update():
  # asking the id to update
  student_id = int(input("Enter the student ID  to update:"))
  # updating the record
  sql = "UPDATE student SET first_name=%s,last_name=%s,address=%s,phone_number=%s WHERE student_id=%s"

  # asking for new data
  fname = input("Enter  new First Name:")
  lname = input("Enter  new Last name: ")
  address = input("Enter  new  address:")
  phone_number = input("Enter new phn number :")
  val = (fname,lname,address,phone_number,student_id)
  cursor.execute(sql,val)
  mydb.commit()
  print(" Record updated successfully!")



# deleting a student
def stud_delete():
  email=input("Enter  email ID :")
  password=input("Enter  password:")
  sql = "delete from student where email=%s and password=%s"
  val=(email,password)
  cursor.execute(sql,val)
  mydb.commit()
  if cursor.rowcount > 0:
    print(f"Record deleted successfully. Rows affected: {cursor.rowcount}")
  else:
    print("No matching record found to delete.")






def student():
    while 1:
      print("1.Add student\n2.Update student details\n3.Delete a student\n4.Exit")
      choice = int(input("Enter your choice:"))
      if choice==1:
        print("Enter the details of student:")
        stud_insert()
      elif choice==2:
        stud_update()
      elif choice==3:
       stud_delete()
      else:
        print("stop")
        break




# INSERTING A TEACHER
def teach_insert():
    sql = "INSERT INTO teacher(first_name,last_name,subject,phone_number,email,qualification,join_date,password) VALUES (%s, %s,%s,%s,%s,%s,%s,%s)"
    fname = input("Enter  First Name:")
    lname = input("Enter  Last Name:")
    subject = input("Subject:")
    phone_number = input("Enter  phn number: ")
    email = input("Email:")
    quali = input("Qualification:")
    join_date = input("Join date:")
    password = input("Enter the password:")

    val = (fname, lname,subject,  phone_number,email,quali,join_date, password)
    cursor.execute(sql, val)

    mydb.commit()
    print(cursor.rowcount, "record inserted")




#UPDATING A TEACHER
def teach_update():
  # asking the id to update
  teach_id = int(input("Enter the Teacher ID  to update:"))
  # updating the record
  sql = "UPDATE teacher SET first_name=%s,last_name=%s,phone_number=%s WHERE teacher_id=%s"

  # asking for new data
  fname = input("Enter  new First Name:")
  lname = input("Enter  new Last name: ")
  phone_number = input("Enter new phn number :")
  val = (fname,lname,phone_number,teach_id)
  cursor.execute(sql,val)
  mydb.commit()
  print(" Record updated successfully!")



# DELETING A TEACHER
def teach_delete():
  email=input("Enter email ID :")
  password=input("Enter  password:")
  sql = "delete from teacher where email=%s and password=%s"
  val=(email,password)
  cursor.execute(sql,val)
  mydb.commit()
  if cursor.rowcount > 0:
    print(f"Record deleted successfully. Rows affected: {cursor.rowcount}")
  else:
    print("No matching record found to delete.")

def teacher():
    while 1:
      print("1.Add teacher\n2.Update teacher details\n3.Delete a teacher\n4.Exit")
      choice = int(input("Enter your choice:"))
      if choice==1:
        print("Enter the details of teacher:")
        teach_insert()
      elif choice==2:
        teach_update()
      elif choice==3:
       teach_delete()
      else:
        print("stop")
        break



# INSERT STAFF DETAILS
def staff_insert():
    sql = "INSERT INTO staff(first_name,last_name,role,phone_number,email,password) VALUES (%s, %s,%s,%s,%s,%s)"
    fname = input("Enter  First Name:")
    lname = input("Enter  Last Name:")
    role = input("Role:")
    phone_number = input("Enter phn number: ")
    email = input("Email:")
    password = input("Enter the password:")

    val = (fname, lname,role,phone_number,email,password)
    cursor.execute(sql, val)

    mydb.commit()
    print(cursor.rowcount, "record inserted")



# UPDATING  A STAFF
def staff_update():
  # asking the id to update
  staff_id = int(input("Enter the Staff ID  to update:"))
  # updating the record
  sql = "UPDATE staff SET first_name=%s,last_name=%s,phone_number=%s WHERE staff_id=%s"

  # asking for new data
  fname = input("Enter  new First Name:")
  lname = input("Enter  new Last name: ")
  phone_number = input("Enter new phn number :")
  val = (fname,lname,phone_number,staff_id)
  cursor.execute(sql,val)
  mydb.commit()
  print(" Record updated successfully!")



# DELETING A STAFF
def staff_delete():
  email=input("Enter email ID :")
  password=input("Enter  password:")
  sql = "delete from staff where email=%s and password=%s"
  val=(email,password)
  cursor.execute(sql,val)
  mydb.commit()
  if cursor.rowcount > 0:
    print(f"Record deleted successfully. Rows affected: {cursor.rowcount}")
  else:
    print("No matching record found to delete.")


def staff():
    while 1:
      print("1.Add staff\n2.Update staff details\n3.Delete staff\n4.Exit")
      choice = int(input("Enter your choice:"))
      if choice==1:
        print("Enter the details of another customer:")
        staff_insert()
      elif choice==2:
        staff_update()
      elif choice==3:
       staff_delete()
      else:
        print("stop")
        break


# TO VIEW STUDENT DETAILS
def view_stud():
    sql="select * from student"
    cursor.execute(sql)
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)


# TO VIEW TEACHERS DETAILS
def view_teach():
    sql="select * from teacher"
    cursor.execute(sql)
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)



# TO VIEW STAFF DETAILS
def view_staff():
    sql="select * from staff"
    cursor.execute(sql)
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)



# ADMIN LOGIN SYSTEM
def admin_view():
  # print("Your logging in as the admin!!!")
  # email= input("Enter the email:")
  # passw= input("Enter the password:")
  # sql="select * from principal where email=%s and password=%s"
  # val = (email,passw)
  # cursor.execute(sql, val)
  # result = cursor.fetchone()
  # if result:
  #     print("Logged in successfully.")
      while 1:
          print("1.To View Staff Details\n2.To View Teachers Details\n3.To View Students details\n4.Exit ")
          ch=int(input("Enter your choice"))
          if ch==1:
              print("Viewing Staff Details")
              view_staff()
              while True:
                  print("Want to add a new staff or edit the existing one?\n1.Yes 2.No")
                  choice=int(input("Enter your choice"))
                  if choice==1:
                    staff()
                  else:
                    print("Returning to admin menu...")
                    break
          elif ch==2:
              print("Viewing Teachers Details")
              view_teach()
          elif ch==3:
              print("Viewing Students Details")
              view_stud()
          elif ch == 4:
              print("Exiting admin menu...")
              break
          else:
              print("Invalid choice. Please try again.")

  # else:
  #     print(" No matching record found. Invalid email or password.")



# STAFF LOGIN
def manager_log():
    # print("You're logging in as the staff!!!")
    # email = input("Enter the email: ")
    # passw = input("Enter the password: ")
    #
    # sql = "SELECT * FROM staff WHERE email=%s AND password=%s"
    # val = (email, passw)
    # cursor.execute(sql, val)
    # result = cursor.fetchone()  # Fetch one matching record
    #
    # if result:
    #     print("Logged in successfully.")

        while True:
            print("\n1. View Teachers Details\n2. View Students Details\n3. Exit")
            ch = int(input("Enter your choice: "))

            if ch == 1:
                print("Viewing Teachers Details...")
                view_teach()
                while True:
                    print("\nDo you want to add or edit a teacher?\n1. Yes\n2. No")
                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        teacher()
                    else:
                        print("Returning to staff menu...")
                        break

            elif ch == 2:
                print("Viewing Students Details...")
                view_stud()
                while True:
                    print("\nDo you want to add or edit a student?\n1. Yes\n2. No")
                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        student()
                    else:
                        print("Returning to staff menu...")
                        break

            elif ch == 3:
                print("Exiting staff menu...")
                break

            else:
                print("Invalid choice. Please try again.")
    # else:
    #     print(" No matching record found. Invalid email or password.")

def stud_log():
    # print("You're logging in as a student!!!")
    # email = input("Enter your email: ")
    # passw = input("Enter your password: ")
    #
    # sql = "SELECT * FROM student WHERE email=%s AND password=%s"
    # val = (email, passw)
    # cursor.execute(sql, val)
    # result = cursor.fetchone()
    # if result:
    #     print("Logged in successfully.")
        while 1:
            print("Are you want to update your details\n1.Yes\n2.No")
            ch = int(input("Enter your choice:"))
            if ch == 1:
                stud_update()
            elif ch==2:
                print("Existing")
                break
            else:
                 print("Invalid choice. Please try again.")
    # else:
    #     print(" No matching record found. Invalid email or password.")


def teach_log():
        while 1:
            print("Are you want to update your details\n1.Yes\n2.No")
            ch = int(input("Enter your choice:"))
            if ch == 1:
                teach_update()
            elif ch==2:
                print("Existing")
                break
            else:
                print("Invalid choice. Please try again.")


def staff_log():
    while 1:
        print("Are you want to update your details\n1.Yes\n2.No")
        ch = int(input("Enter your choice:"))
        if ch == 1:
            staff_update()
        elif ch == 2:
            print("Existing")
            break
        else:
            print("Invalid choice. Please try again.")


# login
def login():
    print("------ LOGIN PORTAL ------")
    email = input("Enter your email ID: ")
    password = input("Enter your password: ")

    # check if email and password exist in any table
    user_found = False

    # check principal table
    cursor.execute("SELECT * FROM principal WHERE email=%s AND password=%s", (email, password))
    result = cursor.fetchone()
    if result:
        cursor.execute("SELECT * FROM login WHERE email=%s", (email,))
        existing = cursor.fetchone()
        if existing:
            cursor.execute("update login set status=1 where email=%s", (email,))
        else:
            sql = "INSERT INTO login (email, password, role, status) VALUES (%s, %s, %s, %s)"
            val = (email, password, 'principal', '1')
            cursor.execute(sql, val)
        mydb.commit()
        print("✅ Logged in successfully as Principal.")
        admin_view()
        user_found = True

    # check manager table
    if not user_found:
        cursor.execute("SELECT * FROM staff WHERE email=%s AND password=%s", (email, password))
        result=cursor.fetchone()
        if result:
            cursor.execute("SELECT * FROM login WHERE email=%s", (email,))
            existing = cursor.fetchone()
            if existing:
                cursor.execute("update login set status=1 where email=%s", (email,))
            else :
                sql="insert into login(email,password,role,status)values(%s,%s,%s,%s) "
                val=(email,password,'Staff','1')
                cursor.execute(sql,val)
            mydb.commit()
            print("✅ Logged in successfully as Staff.")
            staff_log()
            user_found = True


        # check staff table
        if not user_found:
            cursor.execute("SELECT * FROM staff WHERE email='staff@school.com' AND password='staff123'",
                           (email, password))
            result = cursor.fetchone()
            if result:
                cursor.execute("SELECT * FROM login WHERE email=%s", (email,))
                existing = cursor.fetchone()
                if existing:
                    cursor.execute("update login set status=1 where email=%s", (email,))
                else:
                    sql = "insert into login(email,password,role,status)values(%s,%s,%s,%s) "
                    val = (email, password, 'Staff', '1')
                    cursor.execute(sql, val)
                mydb.commit()
                print("✅ Logged in successfully as Staff.")
                manager_log()
                user_found = True

        # check staff table
        if not user_found:
            cursor.execute("SELECT * FROM staff WHERE email='staff@school.com' AND password='staff123'",
                           (email, password))
            result = cursor.fetchone()
            if result:
                cursor.execute("SELECT * FROM login WHERE email=%s", (email,))
                existing = cursor.fetchone()
                if existing:
                    cursor.execute("update login set status=1 where email=%s", (email,))
                else:
                    sql = "insert into login(email,password,role,status)values(%s,%s,%s,%s) "
                    val = (email, password, 'Staff', '1')
                    cursor.execute(sql, val)
                mydb.commit()
                print("✅ Logged in successfully as Staff.")
                staff_log()
                user_found = True


    # check teacher table
    if not user_found:
        cursor.execute("SELECT * FROM teacher WHERE email=%s AND password=%s", (email, password))
        result = cursor.fetchone()
        if result:
            cursor.execute("SELECT * FROM login WHERE email=%s", (email,))
            existing = cursor.fetchone()

            if existing:
                cursor.execute("UPDATE login SET status='1' WHERE email=%s", (email,))
            else:
                sql = "INSERT INTO login(email,password,role,status) VALUES(%s,%s,%s,%s)"
                val = (email, password, 'teacher', '1')
                cursor.execute(sql, val)
            mydb.commit()

            print("✅ Logged in successfully as Teacher.")
            teach_log()
            user_found = True


    # check student table
    if not user_found:
        cursor.execute("SELECT * FROM student WHERE email=%s AND password=%s", (email, password))
        result=cursor.fetchone()
        if result:
            cursor.execute("update login set status=1 where email=%s", (email,))
        else:
            sql = "INSERT INTO login (email, password, role, status) VALUES (%s, %s, %s, %s)"
            val = (email, password, 'Student', '1')
            cursor.execute(sql, val)
        mydb.commit()
        print("✅ Logged in successfully as Student.")
        stud_log()
        user_found = True
    else:
        print("❌ Invalid email or password. Please try again.")



def logged_out():
    sq = "update login set status='0' where status='1'"
    cursor.execute(sq)
    mydb.commit()
    print("Logged out successfully ")

while 1:
    print("School Management System!!")
    print("1.Login\n2.Logout\n3.Exit")
    cho=int(input("Enter your choice:"))
    if cho==1:
        login()
    elif cho==2:
        logged_out()
        break
    else:
        print("Exiting....")
        break
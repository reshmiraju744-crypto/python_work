import re
import os
def add_employee():
    while True:
        name = input("Enter employee name:")
        if re.match(r'^[a-zA-Z\s\']{2,20}$', name):
            break
        print("invalid .Please enter a valid name")
    while True:
        emp_id=input("enter the employee id:")
        if re.match(r'^\d{4,6}$',emp_id):
            break
        print("invalid ID.Please enter a numeric ID with 4-6digits.")
    while True:
        position=input("Enter the position")
        if re.match(r'^[a-zA-Z\s\-]{2,20}$',position):
            break
        print("invalid.Please enter a valid position")
    while True:
        try:
            salary=int(input("enter the salary:"))
            if salary>0:
             break
            print("enter a positive number")
        except ValueError:
             print("Invalid salary ,please enter a valid number")
    details=f"Name:{name}\nEmployee ID:{emp_id}\nPosition:{position}\nSalary:{salary}\n{'-'*30}\n"
    with open(name,"w")as file :
        if file.tell()==0:
         file.write("=== Bank Employee details ===\n")
        file.write(details)
    print("saved successfully")


def show_employee():
    name=input("enter name to see all the details about the employee:")
    try:
        with open(name,"r")as file:
            print("\n-- Employee Records --\n")
            print(file.read())
    except FileNotFoundError:
        print("No records found. Please add employees first.")

def delete_employee():
    name=input("enter name to see all the details about the employee:")
    if os.path.exists(name):
        os.remove(name)
        print("Deleted  Successfully")
    else:
        print("file does not exist")



while 1:
    print("Bank Employee Management System")
    print("1.Add Employee\n 2.Show Employee Records\n 3.Delete Employee")
    choice=int(input("Enter your choice: "))
    if choice==1:
        add_employee()
    elif choice==2:
        show_employee()
    elif choice==3:
        delete_employee()
    else:
        print("Invalid choice")
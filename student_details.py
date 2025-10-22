import re
import os
# adding student
def add_student():
    stud_name=input("Enter your name:")
    stud_id=input("Enter your student ID:")
    sub1 = int(input("Enter your marks in English:"))
    sub2 = int(input("Enter your marks in Malayalam:"))
    sub3 = int(input("Enter your marks in Maths:"))
    sub4 = int(input("Enter your marks in EVS:"))
    total_marks = (sub1 + sub2 + sub3 + sub4)
    print("Total Marks:", total_marks, "/400")
    avg_marks = total_marks / 4
    print("Average Marks:", avg_marks, "/100.0")
    details=f"Student Name:{stud_name}\nStudent ID:{stud_id}\nEnglish:{sub1}\nMalayalam:{sub2}\nMaths:{sub3}\nEVS:{sub4}\nTotal Marks:{total_marks}\nAverage Marks:{avg_marks}"
    with open(stud_name,"w") as file:
        if file.tell()==0:
            file.write("Student's mark details\n")
            file.write(details)
    if avg_marks >= 90:
        print("Excellent")
    elif avg_marks >= 75:
        print("Very Good")
    elif avg_marks >= 50:
        print("Good")
    elif avg_marks >= 35:
        print("Good")
    elif avg_marks >= 20:
        print("Just Pass")
    else:
        print("Failed")
    print("successfully added")


# view a student
def view_student():
    stud_name=input("Enter the student name to see all the details:")
    try:
        with open(stud_name,"r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Doesn't exist first add your name!1")

# deleting a student details
def delete_student():
    name = input("enter name delete the student:")
    if os.path.exists(name):
        os.remove(name)
        print("Deleted  Successfully")
    else:
        print("file does not exist")

while 1:
    print("Student details")
    print("1.Add Student\n 2.Show student record\n 3.Delete Student\n 4.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        add_student()
    elif choice==2:
        view_student()
    elif choice==3:
        delete_student()
    elif choice==4:
        exit()
    else:
        print("Invalid choice")
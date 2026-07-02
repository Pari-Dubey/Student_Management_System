from student import *

while True:

    print("\n====== Student Management System ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        marks = int(input("Enter Marks: "))

        print(add_student(roll, name, marks))

    elif choice == "2":

        students = view_students()

        if len(students) == 0:
            print("No Student Found")

        else:
            for student in students:
                print(student)

    elif choice == "3":

        roll = int(input("Enter Roll Number: "))

        student = search_student(roll)

        if student:
            print(student)
        else:
            print("Student Not Found")

    elif choice == "4":

        roll = int(input("Enter Roll Number: "))
        name = input("Enter New Name: ")
        marks = int(input("Enter New Marks: "))

        print(update_student(roll, name, marks))

    elif choice == "5":

        roll = int(input("Enter Roll Number: "))

        print(delete_student(roll))

    elif choice == "6":

        print("Thank You")
        break

    else:
        print("Invalid Choice")
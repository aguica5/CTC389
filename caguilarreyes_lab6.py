#Carmen Aguilar
#Lab6 

students = ["Felipe", "Mateo", "Cristian", "Yolanda", "Cesar"]

print ("Student List: ")
print(students)

print ("\nMenu")
print ("1. Add a student")
print ("2. Modify a student's name")
print ("3. Remove a student")

choice = int (input("\nEnter your choice between 1-3: "))

if choice == 1: 
    newstu = input("Enter the student's name: ")
    students.append(newstu)

    print (students)

elif choice ==2: 
    print (0, students[0])
    print (1, students[1])
    print (2, students[2])
    print (3, students[3])
    print (4, students[4])

    x = int(input("Enter the number before the student's name that you want to change: "))
    newname = input("enter the new student name")

    students[x] = newname

    print (students)

elif choice ==3: 
    print (0, students[0])
    print (1, students[1])
    print (2, students[2])
    print (3, students[3])
    print (4, students[4])

    y = int(input("Enter the number before the student's name that you want to remove: "))

    students.pop(y)

    print (students)



# In[ ]:
print("Welcome to Python Programming for Data Analytics!")

name = input("Shubham pandey: ")
college = input("Nims unversity: ")
branch = input("Management: ")

print("\n--- Student Information ---")
print("Shubham pandey  :", name)
print("Nims unversity:", college)
print("Management :", branch)


# In[ ]:
age = 22
percentage = 85.5
name = "Shubham kumar pandey"
is_student = True

print("Age:", age, "| Data Type:", type(age))
print("Percentage:", percentage, "| Data Type:", type(percentage))
print("Name:", name, "| Data Type:", type(name))
print("Is Student:", is_student, "| Data Type:", type(is_student))


# In[ ]:
num1 = 5555
num2 = 4444
print("\n--- Calculator Result ---")

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
    print("Modulus:", num1 % num2)
else:
    print("Division: Cannot divide by zero")
    print("Modulus: Cannot divide by zero")


# In[ ]:
marks = 85

if marks >= 85:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Fail"

print("Your Grade is:", grade)


# In[ ]:
for number in range(1, 21):
    print(number)


# In[ ]:
number = 88

print("Multiplication Table of", number)

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# In[ ]:
number = 2

while number <= 50:
    print(number)
    number += 2


# In[ ]:
def square(number):
    return number * number


def average(num1, num2, num3):
    return (num1 + num2 + num3) / 3


number = 555
print("Square:", square(number))

num1 = 10
num2 = 40
num3 = 30

print("Average:", average(num1, num2, num3))


# In[ ]:
text = "Python Programming"

print("Original String:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Replace:", text.replace("Python", "Data"))
print("Position of Programming:", text.find("Programming"))


# In[ ]:
numbers = [50, 20, 40, 10, 30]

print("Original List:", numbers)

numbers.append(60)
print("After append:", numbers)

numbers.remove(20)
print("After remove:", numbers)

numbers.sort()
print("After sort:", numbers)


# In[ ]:
student = ("Shubham", 22, "BBA Finance", 85)

print("Tuple:", student)
print("First Element:", student[0])
print("Second Element:", student[1])
print("Third Element:", student[2])
print("Fourth Element:", student[3])


# In[ ]:
student = {
    "Name": "Shubham",
    "Age": 22,
    "Branch": "BBA Finance",
    "Marks": 85
}


# In[ ]:
print("Student Information:")
print("Name:", student["Name"])
print("Age:", student["Age"])
print("Branch:", student["Branch"])
print("Marks:", student["Marks"])


# In[ ]:
numbers = {10, 20, 30, 40}

print("Original Set:", numbers)

numbers.add(50)
print("After add:", numbers)

numbers.remove(20)
print("After remove:", numbers)


# In[ ]:
introduction = """
My name is Shubham.
I am pursuing BBA Finance.
I am interested in Finance and Data Analytics.
I am learning Python, Excel, SQL and Power BI.
"""

file = open("introduction.txt", "w")
file.write(introduction)
file.close()

file = open("introduction.txt", "r")
content = file.read()
file.close()

print("File Contents:")
print(content)


# In[ ]:
students = []


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    branch = input("Enter Branch: ")
    marks = input("Enter Marks: ")

    student = {
        "ID": student_id,
        "Name": name,
        "Age": age,
        "Branch": branch,
        "Marks": marks
    }

    students.append(student)
    print("Student added successfully!\n")


def display_students():
    if len(students) == 0:
        print("No student records found.\n")
        return

    print("\n--- All Student Records ---")

    for student in students:
        print("ID:", student["ID"])
        print("Name:", student["Name"])
        print("Age:", student["Age"])
        print("Branch:", student["Branch"])
        print("Marks:", student["Marks"])
        print("------------------------")


def search_student():
    name = input("Enter student name to search: ")

    found = False

    for student in students:
        if student["Name"].lower() == name.lower():
            print("\nStudent Found!")
            print("ID:", student["ID"])
            print("Name:", student["Name"])
            print("Age:", student["Age"])
            print("Branch:", student["Branch"])
            print("Marks:", student["Marks"])
            found = True

    if not found:
        print("Student not found.\n")


def delete_student():
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["ID"] == student_id:
            students.remove(student)
            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")


while True:
    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you for using Student Record Management System!")
        break

    else:
        print("Invalid choice. Please try again.")

# exercises 1 List 

# Lists
#A list in Python is a collection of items that are ordered and mutable,
# which means you can change, add, and remove items from it.
#Lists are defined using square brackets [], with elements separated by commas.

fruits = ['apple', "banana","cherry"]

print("Origin list", fruits)

## how to access elements of the list
fruits.append('orange')
print("After appending orange", fruits)

# remove elements
fruits.remove('banana')
print("After remove banana",fruits)

# Reversing the list
fruits.reverse()
print("After reverse the list",fruits)

## example use of list

# Creating a list of students as a directory
students = [
    ['Alice', 20, 'A'],
    ['Bob', 22, 'B'],
    ['Charlie', 21, 'A'],
]

# Adding a new student
students.append(['David', 23, 'B'])
print("Students after adding David:", students)

# Updating a student's information
for student in students:
    if student[0] == 'Alice':
        student[1] = 21
        student[2] = 'A+'
print("Students after updating Alice's information:", students)

# Deleting a student
for student in students:
    if student[0] == 'Bob':
        students.remove(student)
        break
print("Students after deleting Bob:", students)

# Finding a student
for student in students:
    if student[0] == 'Charlie':
        print("Found student:", student)
        break
else:
    print("Student Charlie not found.")

# Printing all student details
for student in students:
    print(f"Student: {student[0]}, Age: {student[1]}, Grade: {student[2]}")


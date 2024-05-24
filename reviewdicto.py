# review A dictionary in Python is a collection of key-value pairs.
# Each key is unique within a dictionary, and keys are used to access their corresponding values.
#Dictionaries are defined using curly braces {}, with key-value pairs separated by colons :.


thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

for key, value in thisdict.items():
    print(f"Key: {key}, Value: {value}")



# Using curly braces
student = {
    'Alice': {'grade': 85, 'age': 20},
    'Bob': {'grade': 78, 'age': 22},
    'Charlie': {'grade': 92, 'age': 21},
}


# Adding a new key-value pair
student['major'] = 'Computer Science'
print(student)  # Output: {'name': 'Alice', 'age': 20, 'grade': 'A', 'major': 'Computer Science'}

# Updating an existing value
student['grade'] = 'A+'
print(student) 

# Using pop()
major = student.pop('major')
print(student)  # Output: {'name': 'Alice', 'grade': 'A+'}
print(major)    #


# Iterating through keys
for key in student:
    print(key)

# Iterating through values
for value in student.values():
    print(value)

# Iterating through key-value pairs
for key, value in student.items():
    print(key, value)
    
    
# Example of common methods to get the students 
student = {'name': 'Alice', 'age': 20, 'grade': 'A'}
print(student.get('name'))  # Output: Alice
print(student.get('major', 'N/A'))  # Output: N/A

# Updating with another dictionary
student.update({'major': 'Computer Science', 'age': 21})
print(student)  




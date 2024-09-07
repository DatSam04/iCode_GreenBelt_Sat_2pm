## example tuple
#Tuples

#A tuple is similar to a list but is immutable, meaning you cannot change its elements once it's created.
#Tuples are defined using parentheses (), with elements separated by commas.

thistuple = ("apple", "banana", "cherry", "orange")

# Iterating over the tuple
for item in thistuple:
    print(item)

num_tuple = (1, 2, 3, 4, 5)

# Iterating over the tuple
for num in num_tuple:
    print(num)



mixed_tuple = ("apple", 123, True, 3.14)

# Iterating over the tuple
for item in mixed_tuple:
    print(item)


nested_tuple = ((1, 2), (3, 4), (5, 6))

# Iterating over the tuple
for pair in nested_tuple:
    for num in pair:
        print(num)
        
        
data_tuple = ("Alice", 25, "Bob", 30, "Charlie", 35)

# Iterating over the tuple
for i in range(0, len(data_tuple), 2):
    print(f"Name: {data_tuple[i]}, Age: {data_tuple[i + 1]}")
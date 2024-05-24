#Uniqueness: Sets in Python are collections of unique elements. 
# This property makes them particularly useful when 
# you need to work with a collection of items without any duplicates A set is an unordered collection of unique elements. Sets do not allow duplicate items.
#Sets are defined using curly braces {}, with elements separated by commas.



# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)

# Adding elements to a set
my_set.add(6)
print("Set after adding 6:", my_set)

# Removing elements from a set
my_set.remove(3)
print("Set after removing 3:", my_set)

# Set operations: Union, Intersection, Difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1.union(set2)
print("Union:", union_set)

intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

difference_set = set1.difference(set2)
print("Difference (set1 - set2):", difference_set)

# Set comprehensions
numbers = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
unique_numbers = {x for x in numbers}
print("Unique numbers using set comprehension:", unique_numbers)

#####################################################################################################
# Sample data: Hashtags from posts on different platforms
twitter_hashtags = {'#python', '#coding', '#dataanalytics', '#socialmedia'}
instagram_hashtags = {'#python', '#machinelearning', '#datascience', '#coding'}

# Combine hashtags from different platforms using union
all_hashtags = twitter_hashtags.union(instagram_hashtags)
print("All Hashtags:", all_hashtags)

# Find common hashtags using intersection
common_hashtags = twitter_hashtags.intersection(instagram_hashtags)
print("Common Hashtags:", common_hashtags)

# Count occurrences of hashtags using a dictionary
hashtags_counts = {}
posts = [{'hashtags': ['#python', '#coding']}, {'hashtags': ['#python', '#machinelearning']}]

for post in posts:
    for hashtag in post['hashtags']:
        if hashtag in hashtags_counts:
            hashtags_counts[hashtag] += 1
        else:
            hashtags_counts[hashtag] = 1

print("Hashtag Occurrences:", hashtags_counts)
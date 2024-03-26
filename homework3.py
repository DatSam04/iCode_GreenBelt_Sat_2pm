# Example 2
# initialize the stepper variable favorite_food to 5 
# This variable will be out put times that favorite food has to be print example : 
# favorite food : pizza, out put : pizza,pizza,pizza
favorite_food = 3
# ask the user what is your favorite food:
food = input("Favorite Food: ")
# using while loop, create a condition that will execute 3 times
# favorite food has to be greather than 0
while favorite_food > 0:
    print(food)
    # decrement the step variable favorite_food
    favorite_food = favorite_food- 1
# Example 1
# using whileloop, print even number from 10 - 1 
# What value can we initialize stepp variable to?
number = 10
while number > 0:
    print(number)
    number = number - 1
    
# Exercise 1 
#Using a while loop, ask the user for a number 3 times.   
# Where in the program should we ask the user for the number?  
# make a variable ask_number and int(input("Number:"))
# Inside the loop, or outside the loop?
#Create a temporary variable named squared that squares the number.  
# Create another temporary variable named cubed that cubes the number.
#Print the values of squared and cubed.

number = 3
while number > 0:
    ask_num = int(input("Number: "))
    squared = ask_num * ask_num
    print("Squared:",squared)
    cubed = ask_num ** 3
    print("Cubed:",cubed)
    number = number - 1



# Exercise 3
# print the print("Mins\tCalories") this is the divition for mins = 10 and the calories = 400
#  comment more about the code
print("Mins\tCalories")
# variable calories and lost calories
calories = 400
lost_calories = 10
# get the while loop has to be greather than > 0
while lost_calories >= 0:
    # print lost calories using the print(lost_calories,"\t",calories)
    print(lost_calories,"\t",calories)
    # calories has to be - 11 
    calories = calories - 11
    # lost calories has to declare - 1
    lost_calories = lost_calories - 1
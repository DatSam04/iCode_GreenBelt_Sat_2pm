# python list lesson 2
# write a if statement.
thing_1 = 5
thing_2 = 1
thing_3 =10

if thing_1 == thing_2 and thing_1 >= thing_3:
    print("thing1_rocks!")
elif thing_1 >= thing_2 and thing_1 < thing_3:
    print("Thing_1 is okay")
else :
    print("thing_1 is meh.....")


# get the NOT,AND OR
# Explanation of tables:
# add the not to the if statement

if thing_1 == thing_2 and thing_1 >= thing_3:
    print("thing1_rocks!")
elif thing_1 >= thing_2 and thing_1 < thing_3:
    print("Thing_1 is okay")
elif not(thing_1 >= thing_2) and thing_1 > thing_3:
    print("All the number are the same !!!")
elif thing_1 == thing_2 and thing_2 == thing_3:
    print("All numbers are the same!!")
else :
    print("thing_1 is meh.....")




# print list variable
list_1 = []
# you can create a list with values too
list_1 = ["a","b","c","d"]
print(list_1[3])

# you can get the size of a list (n) with the len() method
list_size = len(list_1)

# here is more a formatted output
print("The list size is: {}".format(list_size))

# to ad an item in a list use the .append() method
list_1.append("e")
print(list_1)

# swap out position 3 (c) with the number 3
list_1[2] = 3
print(list_1)

# remove the item from the list
del list_1[2]
print(list_1)


# exercises for the list will be sortres data in this order
# first name:
# last name:
# age :
# location:
# hobby:
personal_list = ["Javier","Carreno",30, "Bellevue", "Programmer"]

print(personal_list[0])

# friend list create a python program of list
# create 4 list each with 5 items
# list1 = friend first names
# list 2 = friend 2 first name and last name, city location
# list 3 = friend 3 first name and lasta name, city location
# list 4 = friend 4 first name and last name,citylocation

#output the corresponding information together for each friend
# make the list and print
list_1 = ["firstName: javier","lastName: Carreno","City_location:Bellevue"]

print((list_1[0], list_1[1],list_1[2]))

# while loops
# loopy for loops
# while loop
# needs a counter
counter = 0
while counter < 10:
    print("Counter is {}an dless than 10".format(counter))
    counter += 1
# forloops
for i in range(10):
    print("i = {}".format(i))


print("we will count to 100!")
for i in range(100):
    print(i+1)
    #add an if statement to check the cases
    if i > 0:
        for k in range(i):
            if k> 0:
                number =  number * k



# print the days of the of week
print ("Days of the weeks:")
for i in range(7):
    if i == 0:
        print("Monday")
    elif i == 1:
        print("Tuesday")
    elif i == 2:
        print("Wednesday")
    elif i == 3:
        print("Thursday")
    elif i == 4:
        print("Friday ")
    elif i == 5:
        print("Satuday")
    else :
        print ("Sunday")
# forever loops



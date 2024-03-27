Directory_1 = {
    "Name":"Javier",
    "Age": 33,
    "Hobbies": ["What Tv", "Code","Sleep", "Work"]
}

print(Directory_1["Name"])
print(Directory_1["Age"])


## make a foorloop of the directory
for keys in Directory_1:
    print(keys)


SD = {
    "Name":"Javier",
    "LastName":"Carreno",
    "Age": 33,
    "Hobbies": ["What Tv", "Code","Sleep", "Work"]
}
# create a Directory with security Files
Directory_1["Friends"] = ["Luke", "Marco", "Cathrine"]
#Show dictionary
print(Directory_1)

# Removing data
del Directory_1["Name"]
# Show dictionary
print(Directory_1)

# looping throug just the key
print("\n\nPrinting just key")

# forloop to each val and key
for keys in Directory_1.keys():
    print(keys)
# print the values
print("\n\n printing just the Values:")
# looping the Values
for val in Directory_1.values():
    print(val)
# looping through both key and Value
print("\n\nPrinting both Keys and Values:")
for key,val in Directory_1.items():
    print("Key: {}\nValue:{}\n\n".format(key,val))


# make some question and ask the user to answer that questions
# how it will be adding 1 to counter and if the counter is cero leave the problem

# Challegue will be create a secury checkPoint program
# todo create a dictory filled with secury fields
SD ={
    "Name":"carter",
    "What was your first planet": "Mars",
    "When does the fox catch its tail?": "22:33",
    "Password": "123_456_789"
}

# set up program variables
user_guess : "_"
wrong_count: 0
# foorloop throught each key val pair
for key, val in SD.items():
    q_string = key
# ask user to answer the question of the (key,val)
user_guess = input(q_string)
# 5 if user input does not match value add 1 to counter
if user_guess != val:
    wrong_count += 1
# 6 if counter is not zero. leave program
if wrong_count > 0:
    print("Access denied...self destructure in.... 3...2..1")
else :
    print("Acess granted : Welcome Back")


# scopes and global scopes
varl = 5
# function number
def Global():
    global varl
    print("val is inside func:{}!!".format(varl))
print("Var1 is outside func:{}!!".format(varl))
Global()


# local scope using a function
def func2():
    vars = 10
print("var is inside function 2!! {}".format(vars))
func2()
print("var is outside func2 !! {}".format(vars))





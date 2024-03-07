def grade():
    grade = int(input('Enter your grade: '))
    if grade > 80:
        print("greate work")
    elif grade == 75:
        print("you got a B")
    else: 
        print("you can do it better")
print(grade())

def number():
    number = int(input('Enter number is positive: '))
    if number > 0: 
        print("The number is positive") 
    elif number < 0: 
        print("The number is negative") 
    else: 
        print("The number is zero") 

print(number())


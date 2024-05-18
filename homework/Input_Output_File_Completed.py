import os
import random
from datetime import datetime

def read_file(file_name):
    if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:
        print("No entries found.")
    else:
        file = open(file_name, "r")
        file_data = file.read().strip().split("\n\n")
        for i in range(len(file_data)):
            data = file_data[i].split('\n')
            date_created = data[0]
            username = data[1]
            password = data[2]
            question = data[3]
            answer = data[4]
            code = data[5]
            print("{}. \n {} \n {} \n {} \n {} \n {} \n {} \n".format(i+1, date_created, username, password, question, answer, code))

def write_file(file_name):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    question = input("Enter a special question: ")
    answer = input("Enter the answer for the question: ")
    code = ""
    for i in range(4):
        code += str(random.randrange(1,10))
    print("Account created successfully!")
    print(f"Your confirmation code: {code}")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file = open(file_name, 'a')
    file.write(f"\n\nDate Created: {timestamp}\nUsername: {username}\nPassword: {password}\nQuestion: {question}\nAnswer: {answer}\nConfirmation Code: {code}")

def Sign_up():
    user_input = input("Do you want to sign up? (y/n)")
    while user_input == 'y':
        write_file("accounts.txt")
        print("Account text file: ")
        read_file("accounts.txt")
        user_input = input("Do you want to sign up again? (y/n)")
        while user_input != 'y' and user_input != 'n':
            print("Invalid input")
            user_input = input("Do you want to sign up again? (Enter y or n)")

Sign_up()
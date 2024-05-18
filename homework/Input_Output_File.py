import os
import random
from datetime import datetime

# Create a read_file function to read the text from a file
def read_file(file_name):
    # use os.path.exists and os.path.getsize functions to check whether the file exist
    # Hint: 1. Use not infront of path.exists and compare the path.getsize with 0
    #       2. Both functions take 1 argument, which is the name of the file
    if                                     or                                    :
        print("No entries found.")
    else:
        # create a variable named file and link it to a file using open(file, mode) function

        # create a variable named file_data and store each account as an element in a list
        # Hint: Use .read().strip().split("\n\n") function

        # Use for loops to store each data to a different variable and print them out
        # Hint: Use the length of the file_data for the range of the loop
        for i in
            # Create a variable named data and store the data of an account as a list
            # Hint: use file_name[index] to access element inside file_name
            #       use split('\n') to turn data into a list

            # Create 6 variables, date_created, username, password, question, answer, and code
            # Assign 6 different values stored in data to these 6 variables






            print("{}. \n {} \n {} \n {} \n {} \n {} \n {} \n".format(i+1, date_created, username, password, question, answer, code))

# Create a write_file function to write to or modify a file
def write_file(file_name):
    # Creates 4 variables, username, password, question, and answer, that takes user input




    # Create a variable named code and assigned an empty string to it
    # Use a for loops that run 4 times and store a random number to code in each loop
    # Hint: use str(number) function to convert the number to string
    #       use random.randrange(1, 10) to get a random number from 1-9



    print("Account created successfully!")
    print(f"Your confirmation code: {code}")
    # Create a variable name timestamp and store the time created to it
    # Hint: Use datetime.now().strftime("%Y-%m-%d %H:%M:%S") function

    # Create a variable name file and link it the file using open(file, mode)
    # Hint: for the mode, use 'a', stand for appending, which is modify the file

    # Use file.write(text) function to write to the file and use f"" to write the text
    # Hint: inside f"", you can put variable inside {} to include it in the text

def Sign_up():
    # Create a variable called user_input and ask user whether they want to sign up
                =       ("Do you want to sign up? (y/n)")
    # Use a while to run other function if user enter y

        # Called write_file function to add an account to accounts.txt file

        print("Account text file: ")
        # Called read_file function to print the information in the file

        # Ask user if they want to sign up again and store it in user_input

        # Use a while loop to ensure that user have to enter y or n
        # Hint: use 'and' keyword to check if user_input is different than y and n

            print("Invalid input")
            # Ask user to input their choice again and store it in user_input


# Called sign_up function to execute the code in our program

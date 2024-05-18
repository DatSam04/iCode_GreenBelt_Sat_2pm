import re

text = """
store's number was 888-000-8080
Sam's number is 123-223-1128
Dad's number is 999-234-1899
Gandma-Geen's is 777-727-0001
Keith's might be 876-543-2111
Cathrine's is 222-444-6666
manager's number 555-345-6881
PIGSFEET's number 214-843-7650
"""

# Define a regex pattern to capture names and numbers
# Hint: 1. (name)'s, they takes both lower and upper case
#       2. text between name and number, included all of them
#       3. what letter represent number and how many numbers, letter{amount}
pattern = r"\_([__-__-_-]+)'s (?:           |           |           |       |    )(\_{_}-\_{_}-\_{_})"

# Create a variable called matches and store all the contact in it
# Use re.findall(pattern, text) to find all matches in the text


# Create a dictionary named contacts to store the contacts
# Hint: use a for loops to split the contact into different object
#       Format: {var_1: var_2 for var_1, var_2 in matches}


# Print the contacts
for name, number in contacts.items():
    print(f"{name}: {number}")

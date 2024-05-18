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
pattern = r"\b([A-Za-z-]+)'s (?:number was |number is |might be |number |is )(\d{3}-\d{3}-\d{4})"

# Use re.findall to find all matches in the text
matches = re.findall(pattern, text)

# Create a dictionary to store the contacts
contacts = {name: number for name, number in matches}

# Print the contacts
for name, number in contacts.items():
    print(f"{name}: {number}")

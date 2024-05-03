##Todo-list

#Import modules
# Make a list of the alphabet list 
# Make a count down 
# Get a random letter 
# Ask the user for input 
# Keep track of the time  
# Check if the user typed in the correct letter
#Challenges:
#C1. Have the game repeat without having to restart the game
#C2. Keep track of how many you get correct and the total time
#C3. Make them type more than one letter
#C4. Make it more challenging

# Speed Test Project

import time
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("This is a test to see how fast you can type a random letter")

for i in range(5):
    print(5- i)
    time.sleep(1)
    
answer = random.choice(letters)
print("Type: " + answer)
start = time.time()

choice = input("")

finish = time.time()

if (choice == answer):
    print("You took: " + str(finish - start) + " seconds")
else:
    print("Wrong letter")
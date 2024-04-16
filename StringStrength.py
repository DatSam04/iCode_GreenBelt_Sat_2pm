# todo
## 1. create a forever loop
while True:
    words_strength = [[],[]] ## 2. set up program variable
    leave = '' # empaty string create a variable name leave
    strongest = 0 # create a variable and equal to 0
    list_size = 0 # create a variable name it list_size has to be equal to 0
    leave = input("Please enter a list size (Enter to Exit)") ## 3. get user input (min 3 words) and add strength
    if not leave.isdigit(): # if statement with the isdigit method to check if all the characters are digits
        print("Good Bye") # print good bye if is not a digit
        break # break it
    else: # make an else statement and 
        list_size = int(leave) # create a new variable = to int (empaty string variable)
    for i in range(list_size): #4 get user input (min 3 words) && add strength value
        word = input("Enter a word:") # create a new variable name it word and it will be input("enter a word")
        words_strength[0].append(word) # create use the variable words_strength position [0] to append the variable word
        strength = 0 # create a new variable make it equal to 0
        for letter in word:# forloop letter and the variable word
            strength += ord(letter) # the variable create it strength has to be += ord(letter)
        words_strength[1].append(strength) # the variable words_strength has to have the positon 1 and append the strength
        
    for i in range(list_size - 1): # for loop the index of list_size - 1 
        if words_strength[1][i] >  strongest: # if the words_strength with the position and the index on the forloop[i] it greather than strongest 
            strongest = i # has to be strongest = to the index
    print("the strongest word is {}".format(words_strength[0][strongest])) # print the "the strongest word is {}".format(words_strength[0][strongest])
    print("Strength: {}".format(words_strength[1][strongest])) # print "Strength: {}".format(words_strength[1][strongest])
    
    # 7 pause the game # extra step
    #input(" press enter to un-pause")
    for index in range(10):
        print(index)
    
       
    

# Hangman (game)
import random

word_list = ["cat", "dog", "mouse", "zebra", "chicken", "lion", "dolphin", "chipmunk",
            "snake", "elephant", "horse", "wolf", "hippo", "crocodile", "lizard",
            "fish", "tiger", "butterfly", "rhino", "giraffe"]
hidden_word = ""
current_word = ""

# Initialize for new game
def initialization():
    global hidden_word
    global current_word
    current_word = ""
    number = random.randrange(0, 20)
    hidden_word = word_list[number]
    for i in hidden_word:
        current_word += '_'

# Reveal character that match with the input
# Convert to list to reveal character and convert it back to string
def reveal_character(input):
    global current_word
    tmp = list(current_word)
    index = 0
    for i in hidden_word:
        if(i == input):
            tmp[index] = i
        index += 1
    current_word = ''.join(tmp)

# Compare input and hidden word
def check_input(input):
    if(input == hidden_word):
        print("Congratulation, you got the hidden word")
        return True
    else:
        # if input match with character in the hidden word, reveal them
        print(hidden_word.find(input))
        if(hidden_word.find(input) != -1):
            reveal_character(input)
        # check if user reveal all characters
        if(current_word == hidden_word):
            print("Congratulation, you got the hidden word")
            return True
    return False

# Guess the word
def guessing():
    user_input = input("Enter a character or word: ")
    while(not check_input(user_input)):
        print(current_word)
        user_input = input("Enter a character or word: ")

# Maintain game status
def play():
    game_status = True
    user_choice = ""
    while(game_status):
        initialization()
        guessing()
        user_choice = input("Do you want to play again? (yes/no)")
        while(user_choice != "yes" and user_choice != "no"):
            user_choice = input("Invalid input, please enter yes or no: ")
        if(user_choice == "no"):
            game_status = False

play()
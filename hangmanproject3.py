import random
# global variables
words_list = ["apple", "robot", "happy", "baseball", "computer", "mouse", "horse"]
remaining_letters = list("abcdefghijklmnopqrstuvwxyz")# list of the variable use for it
hidden_word = random.choice(words_list).lower()
word_guessed = "_" * len(hidden_word)
guess_limit = len(hidden_word) + 5
num_guesses = 0
remaining = "".join(remaining_letters)
print("Letters remaining:", remaining)
   
# declaration of the function hangman_game()
def hangman_game():
    global hidden_word,remaining, word_guessed, guess_limit, num_guesses, remaining_letters # declaration of the global variables.
    while num_guesses <= guess_limit:
        guess = input("Please enter a letter: ").lower()
        if guess not in remaining_letters:
            print("You already guessed that letter or it's not a valid letter.")
            continue

        remaining_letters.remove(guess)
        num_guesses += 1

        for index in range(len(hidden_word)):
            if hidden_word[index] == guess:
                word_guessed = word_guessed[:index] + guess + word_guessed[index + 1:]

        print(word_guessed)
        print("Letters remaining:", remaining)

        if hidden_word == word_guessed:
            print("You Won")
            return

    if num_guesses > guess_limit:
        print("You ran out of guesses. You Lose")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    
    if play_again == "yes":
        hangman_game(hidden_word, word_guessed, guess_limit, num_guesses, remaining_letters)
    else:
        print("Thanks for playing!")


hangman_game()
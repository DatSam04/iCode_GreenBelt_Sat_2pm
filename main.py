import random
def guess():
    ## make the random guess
 random_number = random.randint(1, x)
 guess = 0
 while guess != random_number:
    guess = int(input(f"Guess a number between 1 and {x}:"))
    if guess < random_number:
       print('sorry guess again. too low')
    elif guess > random_number:
       print("Sorry guess again to high.")
       print (f'yay congrats you have guessed the number {random_number} congratulation')
#print(guess())
# function computer guess
def computer_guess(feed_Back):
 low = 1
 high = x
 feed_Back = ''
 while feed_Back != 'c':
   if low != high:
     guess = random.radint(low,high)
   else:
      guess = feed_back = input(f'Is{guess} to high(h),too low (l)or corect(c)')
   if feed_back == 'h':
         high = guess  - 1
   elif feed_back == 'l':
      low = guess +1

print(f'Yay the computer guessed your number, {guess},correctly')

# Guess a Number AI edition!
# Derek D
# September 27, 2017

import random

# config
low = 1
high = 100


# helper functions
def show_start_screen():
    print("*************************")
    print("*  Guess a Number A.I!  *")
    print("*************************")

def show_credits():
    if input() == 'n':
        show_credits()
    
def get_guess(current_low, current_high):
    current_low + current_high // 2
"""
Return a truncated average of current low and high.
"""

def pick_number():
    print("Pick a number between" + "" + str(low) + "" + "and" + str(high) + "" + "and keep it in your head! Press enter when you are ready.")
    input()

"""
Ask the player to think of a number between low and high.
Then wait until the player presses enter.
"""
    
def check_guess(guess):
    pass
print("Was my guess too low, too high, or did I get it right?")

"""
Computer will ask if guess was too high, low, or correct.

Returns -1 if the guess was too low
         0 if the guess was correct
         1 if the guess was too high
"""
    
def show_result():
     pass

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    current_low = low
    current_high = high
    check = -1
    
    pick_number()
    
    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess)

        if check == -1:
           current_low = +1
            
        elif check == 1:
            current_high = -1
        

    show_result(guess, rand)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()




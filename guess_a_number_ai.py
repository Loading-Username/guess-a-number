# Guess a Number AI edition!
# Derek D
# September 27, 2017

import random

# config


# helper functions
def show_start_screen():
    print("*************************")
    print("*  Guess a Number A.I!  *")
    print("*************************")

def show_credits():
    print("***************************************************************")
    print("* This game was created by Derek and was completed on 10-6-17 *")
    print("***************************************************************")

def get_guess(current_low, current_high):
    """
    Return a truncated average of current low and high.
    """
    return (current_low + current_high) // 2

def ask_name():
    """
    Asks the player what his/her name is, then refers to them by name in all output.
    """
    print("What is your name?")
    name = input()
    return name

def set_values(name):
    print("Hello" + " " + str(name) + "," + " " + "what do you want the starting low number to be?")
    low = input()
    
    print("What do you want the starting high number to be" + " " + str(name) + "?")
    high = input()

    return int(low), int(high)
    
def pick_number(name,low,high):
    """
    Ask the player to think of a number between low and high.
    Then wait until the player presses enter.
     """    
    print("Hello" + " " + name + "!" + " " + "Pick a number between" + " " + str(low) + " " + "and" + " " + str(high) + " " + "and keep it in your head! Press enter when you are ready!")
    input()    
    
def check_guess(guess):
    """
    Computer will ask if guess was too high, low, or correct.

    Returns -1 if the guess was too low
             0 if the guess was correct
             1 if the guess was too high
    """
    print("Is the number" + " " + str(guess) + "?" + " " + "If not, higher or lower?")
    answer = input()
    
    if answer == ("higher") or answer == ("h") or answer == ("Higher"):
        return +1
    if answer == ("lower") or answer == ("l") or answer == ("Lower"):
        return -1
    if answer == ("yes") or answer == ("y") or answer == ("Yes"):
        return 0 
    else:
        print("What? I don't understand.  Higher, Lower, or Yes?")

def show_result():
    """
    Says the result of the game. (The computer might always win.)
    """
    print("Yay, I won! You suck" + " " + name + "!")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play(name):
    current_low, current_high = set_values(name)
    check = -1

    
    pick_number(name,current_low,current_high)
    
    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess)

        if check == -1:
           current_high = guess +1
            
        elif check == 1:
           current_low = guess -1
        

    show_result()


# Game starts running here
show_start_screen()
name = ask_name()

playing = True

while playing:
    play(name)
    playing = play_again()

show_credits()




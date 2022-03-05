import random, gtn_art
import os # for clear()
clear = lambda: os.system('cls')
play = True
user_Dif = ""
EASY_NUM_TURNS = 10
HARD_NUM_TURNS = 5

def set_dif(): # Return attempts according to difficulty level
    user_C = ""
    while user_C != "easy" and user_C != "hard": # loop will end when there is a valid input
        user_C = input("Choose a difficulty level - Type 'easy' or 'hard': ").lower()
        if user_C == "easy":
            return EASY_NUM_TURNS
        elif user_C == "hard":
            return HARD_NUM_TURNS
        else:
            print("Invalid input")

def end_game(bool): # Return boolean answer if to end/ not end the game
    user_C = ""
    while user_C != "yes" and user_C != "no": # loop will end when there is a valid input
        user_C = input("\nDo you want to continue playing? Type 'yes' or 'no': ").lower()
        if user_C == "no":
            return False
        elif user_C == "yes":
            return True
        else:
            print("Invalid input")

def check_equal(num, in_guess, turns):
    if num > in_guess: # if smaller than
        print("Too low! Try again!")
        return (turns - 1)
    elif num < in_guess: # if bigger than
        print("Too High! Try again!")
        return (turns - 1)
    else:
        print (f"You guessed right! The number is {rand_Num} You Won!\n")
        return

# Main:
while play is True: # play as long as play is True
    print(gtn_art.logo)
    print("Welcom to the Number Guessing Game!\n")
    print("I'm thinking of a number between 1 and 100.\n")
    guess_Attempts = set_dif() # Player will chose difficulty

    rand_Num = random.randint(1, 100) # PC will chose a random number

    # while loop will end when player guess the rand_Num:
    guess = ""
    while rand_Num != guess:
        print(f"You have {guess_Attempts} attempts remaining to guess the number.\n") # print attempts remaining
        guess = int(input("Make a guess: ")) # user guess (input)
        guess_Attempts = check_equal(rand_Num, guess, guess_Attempts)
        if guess_Attempts == 0: # if last attempt
            print("You Lose :(")
            guess = rand_Num

    play = end_game(play) # end the game?
    clear() # clear console

import random, game_data, art
import os # for clear()
clear = lambda: os.system('cls')

def rand_vs():
    """ Func to randomly choice 2 list items and return as val """
    i = 0
    val = random.choices( list(game_data.data) , k = 2) # choose 2 items (k = 2)
    return val

def format_data(data_list):
    """ This function will return formated results: name, description and country from a given dictionary. """
    name = data_list["name"] # set name from dictionary with key "name" from paramater data_list
    desc = data_list["description"]
    country = data_list["country"]
    return f"{name}, a {desc}, from {country}"

def full_format_data(data_list):
    """ This function will return formated results: name, follower count and vs name, vs follower count from a given dictionary. """
    name = data_list[0]["name"] # set name from dictionary with key "name" from paramater data_list
    foll_count = data_list[0]["follower_count"]
    vs_name = data_list[1]["name"]
    vs_foll_count = data_list[1]["follower_count"]
    return f"{name} has {foll_count} followers and {vs_name} has {vs_foll_count} followers"


def comp_vs(choice, a, b):
    """ func to return if palyer gussed right - in which case return 1, else return 0 """
    if choice == 'a':
        if a > b:
            return 1
        else:
            return 0
    if choice == 'b':
        if b > a:
            return 1
        else:
            return 0

def player_input():
    """ Check player valid input """
    valid = ""
    while valid != "a" or valid != "b":
        valid = (input("Who has more followers? Type 'A' or 'B': ")).lower() # player guess
        if valid == "a" or valid == "b":
            return valid
        else:
            print("Invalid input")


########## main:

play = True # boolean state of playing the game
score = 0 # player score counter

print(art.logo)

while play == True: # Game will run until worng guess
    cmplist = rand_vs() # take random items from game_data


    # print the guessing options to player:
    print(f"Compare A: {format_data(cmplist[0])}.")
    print(art.vs)
    print(f"\nCompare B: {format_data(cmplist[1])}. \n")

    guess = player_input() # player guess

    res = comp_vs(guess, cmplist[0]["follower_count"], cmplist[1]["follower_count"]) # compare the results with player guess - return 1 - guess is corrent, return 0 guess is wrong
    clear()
    print(art.logo)
    if res == 0:
        print(f"Wrong, Too bad. {full_format_data(cmplist)} \nYour score is {score}")
        play = False
    else:
        score += 1
        print(f"You're right! {full_format_data(cmplist)} \n")
        print(f"Your score is {score}\n")

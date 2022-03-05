import math
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



logo = """
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
            88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
              88
              88
"""



def caesar_cipher(cip_direction, in_text ,shift_num):
    out_text = "" # initilizing string output (encoded/decoded text)
    if cip_direction != "encode" and cip_direction != "decode": # if user request id not decode or encode - print and exit
        print(f"Unrecognized request, you might wanted to type 'encode' or 'decode' instad of '{direction}'")
    else: # if request is encode or decode
        for letter in in_text: # loop the input text (to be de/en-code)
            # Check if letter is list alphabet - if letter is in list - decode/encode, else skip and writh as is in out-text:
            if letter in alphabet:
                position = alphabet.index(letter) # index - returns the index of the specified element in the list
                # if decode - sub shift from position and chchek if number of shift is not out of range:
                if cip_direction == "decode":
                    new_position = position - shift_num
                else:
                    new_position = position + shift_num
                new_position = new_position % 26 # To avoid shift that is out of range (ex: if shift is -3 - (-3) mod 26 = 23)
                out_text += alphabet[new_position]
            else:
                out_text += letter
        print(f"The {cip_direction}d text is: {out_text}")
            # return out_text

# Main:
program_switch = True

print(logo)

while program_switch == True:
    option_user = ""
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar_cipher(direction, text ,shift)
    while option_user != "n" and option_user != "y":
        option_user = input("Do you want to keep using Caesar Cipher? type Y for yes or N for No ").lower()
        if option_user == "n":
            program_switch = False
            print("Goodbye!")
        elif option_user == "y":
            program_switch = True
        else:
            print("Invalid input!")

import random
import os
import string
import sys
import time

#constants
password = ""

generatePass = False
goBack = False

letters = "abcdefghijklmnopqrstuvwxyz"
capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+"

class COLORS:
    BLUE = "\033[94m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    ORANGE = "\033[33m"
    RESET = "\033[0m"

def colored_input(message):
    user_input = input(message.lower())
    if user_input == 'y':
        print(f"{COLORS.GREEN}{user_input}{COLORS.RESET} - Yes")
        return True
    elif user_input == 'n':
        print(f"{COLORS.RED}{user_input}{COLORS.RESET} - No")
        return False
    else:
        print(f"Invalid input: {user_input}")
        return colored_input(message)
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_logo():
    print("       .---.")
    print("      /     \\")
    print("      \\.@-@./")
    print("      /`\\_/`\\")
    print("     //  _  \\")
    print("    | \\     )|_")
    print("   /`\\_`>  <_/ \\")
    print("den\\__/'---'\\__/" + COLORS.BLUE + " P" + COLORS.RESET + COLORS.RED + "A" + COLORS.RESET +  COLORS.YELLOW + "S" + COLORS.RESET +  COLORS.GREEN + "S" + COLORS.RESET +  COLORS.ORANGE + "W" + COLORS.RESET +  COLORS.BLUE + "O" + COLORS.RESET +  COLORS.RED + "R" + COLORS.RESET +  COLORS.YELLOW + "D" + COLORS.RESET +  COLORS.GREEN + " " + COLORS.RESET +  COLORS.ORANGE + "G" + COLORS.RESET +  COLORS.BLUE + "E" + COLORS.RESET +  COLORS.RED + "N" + COLORS.RESET +  COLORS.YELLOW + "E" + COLORS.RESET +  COLORS.GREEN + "R" + COLORS.RESET +  COLORS.ORANGE + "A" + COLORS.RESET +  COLORS.BLUE + "T" + COLORS.RESET +  COLORS.RED + "O" + COLORS.RESET +  COLORS.YELLOW + "R" + COLORS.RESET +  COLORS.GREEN + " " + COLORS.RESET +  COLORS.ORANGE + "V" + COLORS.RESET +  COLORS.BLUE + "1.0" + COLORS.RESET) 
    print(" ")

def print_menu():
    print(COLORS.GREEN + "1." + COLORS.RESET + " Generate Password")
    print(COLORS.GREEN + "2." + COLORS.RESET + " See saved Passwords")
    print(COLORS.GREEN + "3." + COLORS.RESET + " Exit")

def check_strength(length, want_capital, want_numbers, want_symbols):
    strength_score = 0
    if length > 8:
        strength_score += 1
    if want_capital:
        strength_score += 1
    if want_numbers:
        strength_score += 1
    if want_symbols:
        strength_score += 1

    if strength_score == 4:
        print("Your password is", COLORS.GREEN + "very strong" + COLORS.RESET)
    elif strength_score == 3:
        print("Your password is", COLORS.GREEN + "moderate" + COLORS.RESET)
    elif strength_score == 2:
        print("Your password is", COLORS.YELLOW + "weak" + COLORS.RESET)
    else:
        print("Your password is", COLORS.RED + "very weak" + COLORS.RESET)


def get_pass_length():
    try:
        length = int(input("How long do you want your password to be? "))
        return length
    except ValueError:
        print("Please enter a valid number")
        return get_pass_length()

def generate_password(length, want_capital, want_numbers, want_symbols, letters, capital_letters, numbers, symbols):
    choices = letters
    if want_capital:
        choices += capital_letters
    if want_numbers:
        choices += numbers
    if want_symbols:
        choices += symbols

    if not choices:
        print("Error: No characters selected for password generation.")
        return ""

    password = random.choices(choices, k=int(length))
    final_password = "".join(password)
    return final_password

def loader():
    bar_length = 20
    print("Generating password: [", end='', flush=True)
    
    for i in range(bar_length):
        time.sleep(0.1) 
        print(COLORS.GREEN + "=" + COLORS.RESET, end='', flush=True)
    
    print("]", end='', flush=True) 

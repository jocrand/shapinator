# functions to run the user menu and get the user's choice
import time   # for time.sleep() to control timing of display

def display_menu():
    time.sleep(1)
    print("\n*** SHAPINATOR MENU ***")
    print("1. Add a circle\n\
2. Add a rectangle\n\
3. See my collection\n\
4. End\n")

def get_user_choice():
    choice = input("Please choose 1, 2, 3, or 4\n")
    return choice

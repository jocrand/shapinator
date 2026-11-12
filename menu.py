# code to run the user menu and get the user's choice

def display_options():
    print("SHAPINATOR MENU")
    print("1. Add a circle\n\
2. Add a rectangle\n\
3. See my collection\n\
4. End")

def get_user_choice():
    choice = input("Please choose 1, 2, 3, or 4\n")
    return choice
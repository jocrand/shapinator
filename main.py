"""
SHAPINATOR
Simple menu-driven application with modules and classes.

Author: Jo Crandall (last update November 15, 2026)
    **Include your name and student ID in your project files!

(This is the main file that the user will run.
It imports the modules with necessary functions and classes module.)
"""

import time   # for time.sleep() to control timing of display
import shapinator_utils as su
import shapinator_classes as sc

def main():
    
    print("\n\nWelcome to Shapinator!\n")
    c = sc.Collection()
    
    play = True
    while play:
        su.display_menu()
        choice = int(su.get_user_choice())

        match choice:                     # match-case is similar to switch statements in c++ and java, but no fall-through
            case 1: # add a circle
                rad = float(input("OK, choose a radius: "))
                new_circ = sc.Circle(rad)
                c.add_shape(new_circ)
            case 2: # add a rectangle
                w = float(input("OK, choose a width: "))
                h = float(input("Choose a height: "))
                new_rec = sc.Rectangle(w, h)
                c.add_shape(new_rec)
            case 3: # see collection
                c.display_collection()
            case 4: # end
                play = False
                time.sleep(0.2)
                print("\n\nThanks for playing!\n\n")
                time.sleep(0.2)

if __name__ == '__main__':        #if the name of this file is main, then execute
    main()
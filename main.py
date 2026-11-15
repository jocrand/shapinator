"""This is the main file that the user will run.
It imports the square module and the circle module."""

import time   # for time.sleep() to control timing of display
import shapinator_utils as su

def main():

    print("\n\nWelcome to Shapinator!\n")
    c = su.Collection()
    
    play = True
    while play:
        su.display_menu()
        choice = int(su.get_user_choice())

        match choice:                     # match-case is similar to switch statements in c++ and java, but no fall-through
            case 1: # add a circle
                rad = float(input("OK, choose a radius: "))
                new_circ = su.Circle(rad)
                c.add_shape(new_circ)
            case 2: # add a rectangle
                w = float(input("OK, choose a width: "))
                h = float(input("Choose a height: "))
                new_rec = su.Rectangle(w, h)
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
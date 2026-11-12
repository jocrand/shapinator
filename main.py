"""This is the main file that the user will run.
It imports the square module and the circle module."""

import rectangle as rec
import circle as cir
import collection as col
import menu
import time   # for time.sleep() to control timing of display

def main():

    print("\n\nWelcome to Shapinator!\n")
    c = col.Collection()
    
    play = True
    while play:
        menu.display_options()
        choice = int(menu.get_user_choice())

        match choice:
            case 1: # add a circle
                rad = float(input("OK, choose a radius: "))
                new_circ = cir.Circle(rad)
                c.add_shape(new_circ)
            case 2: # add a rectangle
                w = float(input("OK, choose a width: "))
                h = float(input("Choose a height: "))
                new_rec = rec.Rectangle(w, h)
                c.add_shape(new_rec)
            case 3: # see collection
                print('hi')
            case 4: # end
                play = False
                time.sleep(0.5)
                print("\n\nThanks for playing!\n\n")
                time.sleep(0.5)
                
        
            

    


if __name__ == '__main__':        #if the name of this file is main, then execute
    main()
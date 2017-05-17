"""This program is the implementation of the game Superbrain in Python. 

"""

import random
import sys
import itertools
 
__author__ = "5731507: Eike Henrich, 5967009: Paul Daechert"
__copyright__ = "Copyright 2015/2016 – EPR-Goethe-Uni" 
__credits__ = "" 
__email__ = "uni@family-henrich.de, paul.daechert@hotmail.com" 
  
gShapes = ["square","triangle","pentagon","circle"]
gColours = ["red","blue","yellow","green"]
gInstructions = "Input stones by typing their colour and shape like this:\
 colour,shape (case sensitive!)"
gPossible_stones = list(itertools.product(gColours, gShapes))

def check_stone(stone, available_colours, available_shapes):
    """check_stone examines, if the given stone is valid.

    The funtion also prints out additional information about errors

    """
    if '!' in stone:                            #command input
        print("\n" * 500)
        return False
        
    if not ',' in stone:                        #wrong input seperation
        print("\n" * 500)
        print("No divider ',' detected, please read the instructions!")
        return False
    else:                                       #input syntax is right
        stone_colour = stone.split(',')[0]
        stone_shape = stone.split(',')[1]   
    if not stone_colour in available_colours:   #colour is already taken
        print("\n" * 500)                       #or input is not a colour
        print("Colour is not available!")
        return False
    elif not stone_shape in available_shapes:
        print("\n" * 500)                       #same as colour with shape
        print("Shape is not available!")
        return False
    else:
        return True                             #input is valid
        
def create_new_code(possible_stones):
    """This function creates a random code.
    
    """
    code = [0, 0, 0, 0]
    y = 0
    available_stones = possible_stones[:]
    
    for x in range(4):
        random_selection = random.choice(available_stones)  #choose random
        selected_colour = random_selection[0]               #stones
        selected_shape = random_selection[1]
        code[x] = random_selection
        for stone in available_stones[:]:           #delete chosen stones
            if (stone[0] == selected_colour) or\
            (stone[1] == selected_shape):           #from available stones
                available_stones.remove(stone)
    return(code)
    
def guess_turn(player_code, cheater, current_code, available_colours,\
available_shapes, attempts, previous_selections, previous_hints):
    """guess_turn controls the main actions of this program.
    
    The Program handles the instructions and UI, as well as user input,
    input processing and output. It is recursive."""
    stone_number = 0
    while stone_number < 4:
        print("This is your", attempts, ". attempt")
        if cheater == True:                         #show the right code,
            print("Current Code:\n", current_code)  #this is for testing
        legal_input = True
        if attempts > 1:                            #show the hints,
            print("\nHints:")                       #no hints available
            print(previous_hints[0])                #in round 1
            print(previous_hints[1])
            print(previous_hints[2])
            print()
        if attempts > 1:                            #same for the previous
            print("\nPrevious Selection:")          #selected code
            for k in range(0,attempts-1):
                print (previous_selections[k])
        print("\nAvailable Colours: ", available_colours,
              "\nAvailable Shapes:  ", available_shapes)
        print("\nCurrent Selection:",player_code)
        print(gInstructions)
        chosen_stone = input("Please input the stone.") #user stone input
        legal_input = check_stone(chosen_stone, available_colours,
        available_shapes)
        if (legal_input):                           #checking user input
            stone_colour = chosen_stone.split(',')[0]
            stone_shape = chosen_stone.split(',')[1]
            stone_combine = (stone_colour, stone_shape)
            player_code[stone_number] = stone_combine
            stone_number += 1
            available_colours = [colour for colour in available_colours \
            if not colour == stone_colour]          #delete chosen shapes
            available_shapes = [shape for shape in\
            available_shapes if not shape == stone_shape]#and colours
            print("\n" * 500)
        elif chosen_stone == '!cancel':             #cancle current selection
            guess_turn([0, 0, 0, 0], cheater, current_code, gColours, 
            gShapes, attempts, previous_selections, previous_hints)
        elif chosen_stone == '!code':               #cheat code
            cheater = True
    previous_selections.append(player_code)         #save current input
    
    if validate(player_code, current_code):         #check if the code is
        print("\n" * 500)                           #correct
        print("You won in %d attempts!\n" % (attempts))
        print("Code:", player_code)
        return()
    else:
        print("\n" * 500)                           #incorrect
        print("Wrong guess.")
        if attempts < 8:
            hints = create_hint(player_code, current_code)
            guess_turn([0, 0, 0, 0], cheater, current_code, gColours, gShapes\
            , attempts + 1, previous_selections, hints) #next attempt
        else:
            print("\nYou are out of attempts!\nThe correct code was:",\
            current_code)
        
def create_hint(player_code, current_code):
    """create_hint is the function to create hints of the player code.
    
    The function returns three strings in a list, one for each hint"""
    hint_colour = 0
    hint_shape = 0
    hint_both = 0 
    for y in range(4):
        code_piece = current_code[y]    #check every stone of the playercode
        check_piece = player_code[y] 
        code_colour = code_piece[0]
        code_shape = code_piece[1]
        check_colour = check_piece[0]
        check_shape = check_piece[1]
        if code_colour == check_colour: 
            if code_shape == check_shape:
                hint_both += 1
            else:                
                hint_colour += 1
        elif code_shape == check_shape:
            hint_shape += 1
    return ["Number of correct colours:            %d" % (hint_colour),
            "Number of correct shapes:             %d" % (hint_shape),
            "Number of correct colours AND shapes: %d" % (hint_both)]
          
def validate(player_code, current_code):
    """validate validates the user code.
    
    """
    if (player_code == current_code):
        return(True)
    else:
        return(False)

def start():
    """start starts the program and calls the guess_turn function.
    
    """
    print("""        ***Welcome to Superbrain!***\n\n
        Press Return to start.""")
    press_return = input()
    print("\n" * 500)
    guess_turn([0, 0, 0, 0], False, create_new_code(gPossible_stones), \
    gColours, gShapes, 1, [], [])
    x = True
    while (x == True):                      #replay mechanic
        print("Do you want to play again?")
        play_again_input = input("y/n")
        if play_again_input == 'y':
            print("\n" * 500)
            guess_turn([0, 0, 0, 0], False, create_new_code(gPossible_stones)\
            , gColours, gShapes, 1, [], [])
        elif play_again_input == 'n':
            x = False
        else: 
            print("Please enter y for yes or n for no.")

start()

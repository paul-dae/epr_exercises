"""Docstring: A very short sentence explaining the function. < 79 characters.

This is a implementation of the game skyline for EPR15/16 Aufgabe_04.

"""
import tkinter
import tkinter.messagebox
import random


__author__ = "5967009: Paul Daechert, 5731507: Eike Henrich"
__copyright__ = "Copyright 2015/2016 – EPR-Goethe-Uni"
__credits__ = ""
__email__ = "paul.daechert@hotmail.com, uni@family-henrich.de"


class SkylineField:
    def __init__(self, master):
        """

        Creates the game board.

        """
        field = tkinter.Frame(master)   #Initialize Frame
        field.pack()

        #Creates the fieldbuttons and assigns the increase_cell_value function
        self.field00 = tkinter.Button(field,
                                      command = lambda:
                                      self.increase_cell_value(self.field00),
                                      width = 10, height = 5, bg = "white")
        self.field01 = tkinter.Button(field,
                                      command = lambda:
                                      self.increase_cell_value(self.field01),
                                      width = 10, height = 5, bg = "white")
        self.field02 = tkinter.Button(field,
                                      command = lambda:
                                      self.increase_cell_value(self.field02),
                                      width = 10, height = 5, bg = "white")
        self.field03 = tkinter.Button(field,
                                      command = lambda:
                                      self.increase_cell_value(self.field03),
                                      width = 10, height = 5, bg = "white")
        self.field10 = tkinter.Button(field,
                                      command = lambda:
                                      self.increase_cell_value(self.field10),
                                      width = 10, height = 5, bg = "white")
        self.field11 = tkinter.Button(field,
                                      command = lambda:
                                      self.increase_cell_value(self.field11),
                                      width = 10, height = 5, bg = "white")
        self.field12 = tkinter.Button(field,
                                      command = lambda:
                                      self.increase_cell_value(self.field12),
                                      width = 10, height = 5, bg = "white")
        self.field13 = tkinter.Button(field,
                                      command = lambda:
                                      self.increase_cell_value(self.field13),
                                      width = 10, height = 5, bg = "white")
        self.field20 = tkinter.Button(field,
                                      command = lambda:
                                      self.increase_cell_value(self.field20),
                                      width = 10, height = 5, bg = "white")
        self.field21 = tkinter.Button(field,
                                      command = lambda:
                                      self.increase_cell_value(self.field21),
                                      width = 10, height = 5, bg = "white")
        self.field22 = tkinter.Button(field,
                                      command = lambda:
                                      self.increase_cell_value(self.field22),
                                      width = 10, height = 5, bg = "white")
        self.field23 = tkinter.Button(field,
                                      command = lambda:
                                      self.increase_cell_value(self.field23),
                                      width = 10, height = 5, bg = "white")
        self.field30 = tkinter.Button(field,
                                      command = lambda:
                                      self.increase_cell_value(self.field30),
                                      width = 10, height = 5, bg = "white")
        self.field31 = tkinter.Button(field,
                                      command = lambda:
                                      self.increase_cell_value(self.field31),
                                      width = 10, height = 5, bg = "white")
        self.field32 = tkinter.Button(field,
                                      command = lambda:
                                      self.increase_cell_value(self.field32),
                                      width = 10, height = 5, bg = "white")
        self.field33 = tkinter.Button(field,
                                      command = lambda:
                                      self.increase_cell_value(self.field33),
                                      width = 10, height = 5, bg = "white")

        #Creates the hintfields as buttons without command.
        self.hintfield00 = tkinter.Button(field, width = 11, height = 6)
        self.hintfield01 = tkinter.Button(field, width = 10, height = 6)
        self.hintfield02 = tkinter.Button(field, width = 10, height = 6)
        self.hintfield03 = tkinter.Button(field, width = 10, height = 6)
        self.hintfield04 = tkinter.Button(field, width = 10, height = 6)
        self.hintfield05 = tkinter.Button(field, width = 11, height = 6)
        self.hintfield06 = tkinter.Button(field, width = 11, height = 5)
        self.hintfield07 = tkinter.Button(field, width = 11, height = 5)
        self.hintfield08 = tkinter.Button(field, width = 11, height = 5)
        self.hintfield09 = tkinter.Button(field, width = 11, height = 5)
        self.hintfield10 = tkinter.Button(field, width = 11, height = 6)
        self.hintfield11 = tkinter.Button(field, width = 10, height = 6)
        self.hintfield12 = tkinter.Button(field, width = 10, height = 6)
        self.hintfield13 = tkinter.Button(field, width = 10, height = 6)
        self.hintfield14 = tkinter.Button(field, width = 10, height = 6)
        self.hintfield15 = tkinter.Button(field, width = 11, height = 6)
        self.hintfield16 = tkinter.Button(field, width = 11, height = 5)
        self.hintfield17 = tkinter.Button(field, width = 11, height = 5)
        self.hintfield18 = tkinter.Button(field, width = 11, height = 5)
        self.hintfield19 = tkinter.Button(field, width = 11, height = 5)

        #Alignes the hintfields to surround the board.
        self.hintfield00.grid(row = 0, column = 0)
        self.hintfield01.grid(row = 0, column = 1)
        self.hintfield02.grid(row = 0, column = 2)
        self.hintfield03.grid(row = 0, column = 3)
        self.hintfield04.grid(row = 0, column = 4)
        self.hintfield05.grid(row = 0, column = 5)
        self.hintfield06.grid(row = 1, column = 5)
        self.hintfield07.grid(row = 2, column = 5)
        self.hintfield08.grid(row = 3, column = 5)
        self.hintfield09.grid(row = 4, column = 5)
        self.hintfield10.grid(row = 5, column = 5)
        self.hintfield11.grid(row = 5, column = 4)
        self.hintfield12.grid(row = 5, column = 3)
        self.hintfield13.grid(row = 5, column = 2)
        self.hintfield14.grid(row = 5, column = 1)
        self.hintfield15.grid(row = 5, column = 0)
        self.hintfield16.grid(row = 4, column = 0)
        self.hintfield17.grid(row = 3, column = 0)
        self.hintfield18.grid(row = 2, column = 0)
        self.hintfield19.grid(row = 1, column = 0)

        #Alignes the inputfields to form a 4x4 square.
        self.field00.grid(row = 1, column = 1)
        self.field01.grid(row = 1, column = 2)
        self.field02.grid(row = 1, column = 3)
        self.field03.grid(row = 1, column = 4)
        self.field10.grid(row = 2, column = 1)
        self.field11.grid(row = 2, column = 2)
        self.field12.grid(row = 2, column = 3)
        self.field13.grid(row = 2, column = 4)
        self.field20.grid(row = 3, column = 1)
        self.field21.grid(row = 3, column = 2)
        self.field22.grid(row = 3, column = 3)
        self.field23.grid(row = 3, column = 4)
        self.field30.grid(row = 4, column = 1)
        self.field31.grid(row = 4, column = 2)
        self.field32.grid(row = 4, column = 3)
        self.field33.grid(row = 4, column = 4)

        self.make_new_game()

    def make_new_game(self):
        """

        Starts a new game.

        """
        self.skyline_code = self.create_new_field() #Creates new code
        self.create_hints(self.skyline_code)        #Creates new hints

        self.field00["text"] = "?"        #Resets all buttons to "?"
        self.field01["text"] = "?"
        self.field02["text"] = "?"
        self.field03["text"] = "?"
        self.field10["text"] = "?"
        self.field11["text"] = "?"
        self.field12["text"] = "?"
        self.field13["text"] = "?"
        self.field20["text"] = "?"
        self.field21["text"] = "?"
        self.field22["text"] = "?"
        self.field23["text"] = "?"
        self.field30["text"] = "?"
        self.field31["text"] = "?"
        self.field32["text"] = "?"
        self.field33["text"] = "?"

    def create_new_field(self):
        """

        Creates a new random code.

        """
        fieldcode = [[0 for x in range(4)] for x in range(4)]
        for rows in range(4):
            for columns in range(4):
                possible_numbers = list(range(1, 5))
                #Creates list of possible numbers from 1 to 4 for every field
                for a in range(4):
                    #Removes existing numbers from colums.
                    if fieldcode[a][columns] in possible_numbers:
                        possible_numbers.remove(fieldcode[a][columns])
                for b in range(4):
                    #Removes existing numbers from rows.
                     if fieldcode[rows][b] in possible_numbers:
                        possible_numbers.remove(fieldcode[rows][b])
                if possible_numbers != []:
                    #If possible numbers are left.
                    #choses a random possible number.
                    fieldcode[rows][columns] = random.choice(possible_numbers)
                else:
                    #If there are no possible numbers start new generation.
                    fieldcode = self.create_new_field()
                    break
        return fieldcode

    def check_field(self):
        """

        Checks if the code on the field is the right one.

        """
        #Compares every field to it's corresponding code segment.
        #Breaks if one field doesn't accord and returns False.
        #Otherwise returns True.
        if self.field00["text"] != self.skyline_code[0][0]:
            return False
        elif self.field01["text"] != self.skyline_code[0][1]:
            return False
        elif self.field02["text"] != self.skyline_code[0][2]:
            return False
        elif self.field03["text"] != self.skyline_code[0][3]:
            return False
        elif self.field10["text"] != self.skyline_code[1][0]:
            return False
        elif self.field11["text"] != self.skyline_code[1][1]:
            return False
        elif self.field12["text"] != self.skyline_code[1][2]:
            return False
        elif self.field13["text"] != self.skyline_code[1][3]:
            return False
        elif self.field20["text"] != self.skyline_code[2][0]:
            return False
        elif self.field21["text"] != self.skyline_code[2][1]:
            return False
        elif self.field22["text"] != self.skyline_code[2][2]:
            return False
        elif self.field23["text"] != self.skyline_code[2][3]:
            return False
        elif self.field30["text"] != self.skyline_code[3][0]:
            return False
        elif self.field31["text"] != self.skyline_code[3][1]:
            return False
        elif self.field32["text"] != self.skyline_code[3][2]:
            return False
        elif self.field33["text"] != self.skyline_code[3][3]:
            return False
        else:
            return True

    def height_check(self, row_value, column_value, index, fieldcode):
        """

        Checks what number should be displayed as hint.

        """
        if fieldcode[row_value][column_value] == 4:
            hint_value = 1
            #If the first height is 4 the adjacent hint is 1.
        elif index == "row":
            #If it is a row.
            if column_value == 0:
                #checks from the left.
                if fieldcode[row_value][1] == 4:
                    hint_value = 2
                elif fieldcode[row_value][0] == 3:
                    hint_value = 2
                elif fieldcode[row_value][1] == 3:
                    hint_value = 3
                elif fieldcode[row_value][0] == 2:
                    if fieldcode[row_value][2] == 3:
                        hint_value = 3
                    else:
                        hint_value = 2
                elif fieldcode[row_value][2] == 4:
                    hint_value = 3
                else:
                    hint_value = 4
            else:
                #checks from the right.
                if fieldcode[row_value][2] == 4:
                    hint_value = 2
                elif fieldcode[row_value][3] == 3:
                    hint_value = 2
                elif fieldcode[row_value][2] == 3:
                    hint_value = 3
                elif fieldcode[row_value][3] == 2:
                    if fieldcode[row_value][1] == 3:
                        hint_value = 3
                    else:
                        hint_value = 2
                elif fieldcode[row_value][1] == 4:
                    hint_value = 3
                else:
                    hint_value = 4
        else:
            #If it is a collum.
            if row_value == 0:
                #checks from the top.
                if fieldcode[1][column_value] == 4:
                    hint_value = 2
                elif fieldcode[0][column_value] == 3:
                    hint_value = 2
                elif fieldcode[1][column_value] == 3:
                    hint_value = 3
                elif fieldcode[0][column_value] == 2:
                    if fieldcode[2][column_value] == 3:
                        hint_value = 3
                    else:
                        hint_value = 2
                elif fieldcode[2][column_value] == 4:
                    hint_value = 3
                else:
                     hint_value = 4
            else:
                #checks from the bottom.
                if fieldcode[2][column_value] == 4:
                    hint_value = 2
                elif fieldcode[3][column_value] == 3:
                    hint_value = 2
                elif fieldcode[2][column_value] == 3:
                    hint_value = 3
                elif fieldcode[3][column_value] == 2:
                    if fieldcode[1][column_value] == 3:
                        hint_value = 3
                    else:
                        hint_value = 2
                elif fieldcode[1][column_value] == 4:
                    hint_value = 3
                else:
                    hint_value = 4
        return hint_value

    def create_hints(self, fieldcode):
        """

        Creates hints for the fields as shown in the example.
        For the hint it useses height_check.

        """
        self.hintfield01["text"] = self.height_check(0, 0, "column",
                                                     fieldcode)
        self.hintfield03["text"] = self.height_check(0, 2, "column",
                                                     fieldcode)
        self.hintfield08["text"] = self.height_check(2, 3, "row", fieldcode)
        self.hintfield09["text"] = self.height_check(3, 3, "row", fieldcode)
        self.hintfield11["text"] = self.height_check(3, 3, "column",
                                                     fieldcode)
        self.hintfield12["text"] = self.height_check(3, 2, "column",
                                                     fieldcode)
        self.hintfield13["text"] = self.height_check(3, 1, "column",
                                                     fieldcode)
        self.hintfield14["text"] = self.height_check(3, 0, "column",
                                                     fieldcode)
        self.hintfield16["text"] = self.height_check(3, 0, "row", fieldcode)
        self.hintfield18["text"] = self.height_check(1, 0, "row", fieldcode)
        self.hintfield19["text"] = self.height_check(0, 0, "row", fieldcode)

    def increase_cell_value(self, field_cell):
        """

        Increment cell value or resets to "?"

        """
        if field_cell["text"] != "?":
            #If "?" set to 1.
            if field_cell["text"] == 4:
                #If 4 set to "?".
                field_cell["text"] = "?"
            else:
                field_cell["text"] = int(field_cell["text"]) + 1
                #Increment value.
        else:
            field_cell["text"] = 1


def fieldcheck(skyline_game):
    """

    The button to validate the field.

    """
    if skyline_game.check_field():
        #If the players guess is right.
        answer = tkinter.messagebox.askquestion("You Won!", "Congratulations!"
                                                            "Do you want to "
                                                            "play again?")
        if answer == "yes":
            skyline_game.make_new_game()
            #If wished creates new game.
    else:
        #If the players guess is wrong.
        tkinter.messagebox.showinfo("Try Again", "Sorry this is not the right"
                                                 "Code :/ .")


def show_instructions():
    """

    Shows the instructions of the game.

    """
    tkinter.messagebox.showinfo("Instructions", instructions)
    #prints instructions in a messagebox

instructions = "The game Skyline works as following: \n" \
               "The game generates a random code that illustrates houses.\n" \
               "Houses can have the heights 1 to 4 and there are 16 houses\n"\
               "arranged in a 4x4 field (White background).\n" \
               "There is always 1 set of houses in each column and " \
               "row (houses from 1-4).\n" \
               "When standing on the outside positions of the field,\n" \
               "you can't see all houses, since higher ones cover smaller " \
               "ones.\n\nOn the outside (grey background) you can see " \
               " some numbers,\nthese show the number of houses you can see."\
               "This means, if the number on the grey area is 1 for example,"\
               " the first house in that column or row has the height 4.\n\n"\
               "How to play:\n" \
               "You can change the numbers in the white field by simply " \
               "clicking on them.\nOnce you think you are done, click 'File'"\
               "in the top menu\nand then 'Check Field'.\nIf you want to" \
               "start a new game, hit 'New Game'."

root = tkinter.Tk()         #creates root window
root.title("Skyline")       #name of the game window
skyline_game = SkylineField(root)  #creates object

toolbar = tkinter.Menu(root)    #creates the toolbar
root.config(menu = toolbar)     #assignes the toolbar
sub_toolbar1 = tkinter.Menu(toolbar)    #creates toolbar 'File'
sub_toolbar2 = tkinter.Menu(toolbar)    #creates toolbar '?'

toolbar.add_cascade(label = "File", menu = sub_toolbar1)
                    #set name of first to "File".
sub_toolbar1.add_command(label = "New game",
                         command = skyline_game.make_new_game)
                        #command to make new game.
sub_toolbar1.add_command(label = "Check Field",
                         command = lambda: fieldcheck(skyline_game))
                        #command to check the field.
sub_toolbar1.add_command(label = "Exit", command = root.quit)
                        #command to shut down the game.

toolbar.add_cascade(label = "?", menu = sub_toolbar2)
                        #set name of second to"?"
sub_toolbar2.add_command(label = "Instructions", command = show_instructions)
#command to display the instructions.


root.mainloop()  #keeps the window open
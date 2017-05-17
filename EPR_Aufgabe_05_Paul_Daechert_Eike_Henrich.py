"""

This is an implementation of the game PyCreatures for EPR.
For a full set of rules you need a HRZ-Account and visit
http://moodle.studiumdigitale.uni-frankfurt.de/moodle2/pluginfile.php/27613
/mod_resource/content/1/PRG1-WS-2015-2016-EPR5.pdf

"""


import random


__author__ = "5731507: Eike Henrich, 5967009: Paul Daechert"
__copyright__ = "Copyright 2015/2016 – EPR-Goethe-Uni"
__credits__ = ""
__email__ = "uni@family-henrich.de, paul.daechert@hotmail.com"

gInstructions = "Press 'h' to access these Instructions. \n"\
                "Press 'q' to quit the game. \n"\
                "Spawn <number> <type> creates x of selected type."\
                "Spawn 3 Mouse results in spawning 3 Mice at random locations"\
                "\n Press Return once to Compute one Cycle and enter any "\
                "number to compute as many cycles."

#To access the Instructions from different functions
#we defined them in the start.

class World:

    def __init__(self, width, height):
        self.age = 0
        if type(width) == int and 1 <= width <= 79:
            self._width = width
        else:
            raise TypeError("The width has to be between 1 and 79!")
        if type(height) == int and height >= 1:
            self._height = height
        else:
            raise TypeError("The height has to be greater than 1!")
        self.worldMap = [['.' for i in range(self._width)]for j in
                         range(self._height)]
        self.Dictionary = {}
        for width in range(self._width):
            for height in range(self._height):
                self.Dictionary[width, height] = None

    def printMap(self):
        """

    Iterates through the map from top left to bottom rigth and prints it.

    """
        for height in range(self._height):
            for width in range(self._width):
                print(self.worldMap[height][width], end="")
            print()

    def getObj(self, x, y):
        """

    Prints the symbol of an object at Position(x,y). If no object '.'.
    Just used in the test for Milestone1.

    """
        if self.Dictionary[x, y] is not None:
            print(self.Dictionary[x, y].symbol)
        else:
            print('.')

    def getNeighbour(self, x, y, direction):

        """

    Requires the position of an object and the direction of desired Neighbour.
    0 for North (or up)
    1 for East (or rigth)
    2 for South (or down)
    3 for West (or left)
    Returns the Neighbours entry in the Dictionary.

    The map is connected on the edges. So if a Neighbours position exceedes
    the range of the map it starts again on the opposing side.
    """

        if direction == 0:
            if y != 0:
                return self.Dictionary[x, (y - 1)]
            else:
                return self.Dictionary[x, (self._height - 1)]

        elif direction == 1:
            if x != (self._width - 1):
                return self.Dictionary[(x + 1), y]
            else:
                return self.Dictionary[0, y]

        elif direction == 2:
            if y != (self._height - 1):
                return self.Dictionary[x, (y + 1)]
            else:
                return self.Dictionary[x, 0]

        elif direction == 3:
            if x != 0:
                return self.Dictionary[(x - 1), y]
            else:
                return self.Dictionary[(self._width - 1), y]

    def computeLifeCycle(self):

        """

    Iterates the age of the world.
    Creates a list of Things in the World and shuffeles the list to ensure
    performed actions are in random order.
    Performes actions for every object on the created list.

    """

        self.age += 1
        things = []
        for width in range(self._width):
            for height in range(self._height):
                if self.Dictionary[width, height] is not None:
                    things.append(self.Dictionary[width, height])
        random.shuffle(things)
        for x in range(len(things)):
            things[x].performAction()

    def delPos(self, x, y):

        """

    Requires the position of the Object that should be deleted.
    Sets the Dictionaryentry to None and resets the Map on given location.

    """

        self.Dictionary[x, y] = None
        self.worldMap[y][x] = '.'

    def move(self, this, posx, posy):
        """

    Requires the object to move and its target location.
    Delets the current entrys for selected object.
    Then replaces the entrys on the destination with its own values.

    """

        this.world.delPos(this.posx, this.posy)
        this.posx = posx
        this.posy = posy
        this.world.Dictionary[posx, posy] = this
        this.world.worldMap[posy][posx] = this.symbol


class Thing:

    def __init__(self, symbol, posx, posy, world):
        self.age = 0
        self.posx = posx
        self.posy = posy
        self.symbol = symbol
        self.world = world
        self.world.Dictionary[posx, posy] = self
        self.world.worldMap[posy][posx] = symbol

    def performAction(self):
    
        """
    
        Includes all the actions that can occour.
    
        """
 
        self.age += 1 #increments the age
        if isinstance(self, Plant): #actions for plants
            if self.age % self.seedCycle == 0: #checks if the time to
                                               #offspring is reached 
                directions = [0, 1, 2, 3]
                random.shuffle(directions) #ensures direction is random
                for x in range(4): #checks for empty direction
                    if self.world.getNeighbour(self.posx, self.posy,
                                               directions[x]) is None:
                        seedposx = 0
                        seedposy = 0
                        if directions[x] == 0: #adjusts seeds pos according
                            seedposy = -1      #to selected direction
                        elif directions[x] == 1:
                            seedposx = 1
                        elif directions[x] == 2:
                            seedposy = 1
                        elif directions[x] == 3:
                            seedposx = -1
                        seed = Plant(self.symbol, ((self.posx + seedposx) %
                                                   self.world._width),
                                     ((self.posy - seedposy) %
                                      self.world._height), self.world,
                                     self.seedCycle)#actually creates new Plant
                        break
                    
        if isinstance(self, Creature):#actions for creatures
            if self.age >= self.maxAge or self.starving >= self.maxStarving:
                self.world.delPos(self.posx, self.posy) #del if maxAge or
                                                        #maxStarve is exceeded
            else:
                directions = [0, 1, 2, 3]
                random.shuffle(directions) #ensures direction is random
                for x in range(4):#checks for empty direction 
                                  #or plant-neighbour
                    if isinstance(self.world.getNeighbour(self.posx, self.posy,
                                                          directions[x]),
                                  Plant):
                        newposx = 0
                        newposy = 0
                        if directions[x] == 0:
                            newposy = -1
                        elif directions[x] == 1:
                            newposx = 1
                        elif directions[x] == 2:
                            newposy = 1
                        elif directions[x] == 3:
                            newposx = -1
                        self.world.move(self, (self.posx + newposx) %
                                        self.world._width,
                                        (self.posy + newposy) %
                                        self.world._height)
                        self.starving = -1 #resets hunger 
                        break
                if self.starving != -1:#checks if Creature has allready 
                                       #moved through eating
                    random.shuffle(directions)#Random move if otherwise
                    for x in range(4):
                        if not isinstance(self.world.getNeighbour(self.posx,
                                                                  self.posy,
                                                                  directions[x]
                                                                  ),
                                          Thing):
                            newposx = 0
                            newposy = 0
                            if directions[x] == 0:
                                newposy = -1
                            elif directions[x] == 1:
                                newposx = 1
                            elif directions[x] == 2:
                                newposy = 1
                            elif directions[x] == 3:
                                newposx = -1
                            self.world.move(self, (self.posx + newposx) %
                                            self.world._width,
                                            (self.posy + newposy) %
                                            self.world._height)
                            break
                self.starving += 1 #increment hunger
                if self.age % self.offspringCycle == 0:#checks if the time to
                                                       #offspring is reached
                                                       #process as for plant
                    random.shuffle(directions)
                    for x in range(4):
                        if not isinstance(self.world.getNeighbour(self.posx,
                                                                  self.posy,
                                                                  directions[x]
                                                                  ),
                                          Creature):
                            babyposx = 0
                            babyposy = 0
                            if directions[x] == 0:
                                babyposy = -1
                            elif directions[x] == 1:
                                babyposx = 1
                            elif directions[x] == 2:
                                babyposy = 1
                            elif directions[x] == 3:
                                babyposx = -1
                            baby_creature = Creature(self.symbol,
                                                     ((self.posx + babyposx) %
                                                      self.world._width),
                                                     ((self.posy - babyposy) %
                                                      self.world._height),
                                                     self.world,
                                                     self.offspringCycle, 0,
                                                     self.maxStarving,
                                                     self.maxAge)
                            baby_creature.world.move(baby_creature,
                                                     baby_creature.posx,
                                                     baby_creature.posy)
                            #move to update worldmap symbols
                            break
                    

class Plant(Thing):
    def __init__(self, symbol, posx, posy, world, seedCycle):
        """
        This class is the Plant version of the Thing class.
        """
        super().__init__(symbol, posx, posy, world)
        #The Plant is a Thing that has a seedCycle and therefor only has
        #this as an extra variable, the rest will be passed through
        #to the Thing class
        self.seedCycle = seedCycle


class Creature(Thing):
    def __init__(self, symbol, posx, posy, world, offspringCycle, starving,
                 maxStarving, maxAge):
        """
        This class is the Creature version of the Thing class.
        """
        super().__init__(symbol, posx, posy, world)
        #The Creature classes passes the same attributes to the Thing class
        #as the Plant class, but has some more own variables
        self.offspringCycle = offspringCycle
        self.starving = starving
        self.maxStarving = maxStarving
        self.maxAge = maxAge


class Mouse(Creature):
    def __init__(self, posx, posy, world, offspringCycle, maxStarving, maxAge):
        """
        This class is a version of the Creature class.
        """
        #Mouses passes all variables to the Creature class, but has a constant
        #symbol and starting starving rate
        super().__init__('M', posx, posy, world, offspringCycle, 0,
                         maxStarving, maxAge)


class Corn(Plant):
    def __init__(self, posx, posy, world, seedCycle):
        """
        This class is a version of the Plant class.
        """
        #The Corn passes all variables and its symbol "§" to the Plant class
        super().__init__('§', posx, posy, world, seedCycle)


def create_corn(pos, world, seedCycle):
    """
    This function is used for spawning corn.
    """
    (posx, posy) = pos
    #Coordinates were packed to shuffle the list easier, so need to be unpacked
    corn = Corn(posx, posy, world, seedCycle)


def create_mouse(pos, world, offspringCycle, maxStarving, maxAge):
    """
    This function is used for spawning mice.
    """
    #Same as create corn, coordinates need to be unpacked
    (posx, posy) = pos
    mouse = Mouse(posx, posy, world, offspringCycle, maxStarving, maxAge)
    
    
def playGame():
    """
    This function controls the game itself.
    """
    playing = True
    height = 0
    width = 0
    while height < 1 or width < 1 or width > 79:
        #loop to ensure a valid input
        width = input("Please input the width of your world. It shouldn't "
                      "exceed 79 to display your world properly. ")
        height = input("Please input the height of your world.")
        if height.isdigit():
            height = int(height)
            if width.isdigit():
                width = int(width)
                if height < 1:
                    if width < 1 or width > 79:
                        print("\nInvalid width and height")
                    else:
                        print("\nInvalid height")
                elif width < 1 or width > 79:
                    print("\nInvalid width")
            else:
                print("\nInvalid width")
                width = 0
        elif width.isdigit():
            print("\nInvalid height")
            height = 0
        else:
            print("\nInvalid width and height")
            width = 0
            height = 0
            
    game_world = World(int(width), int(height))  #create World from user input
    game_world.printMap()               #print world
    things = ['corn', 'mouse']          #all possible Things
    while playing:                      #game loop
        errormessage = []               #errormessages cleared
        valInt = False                  #Valid spawn input
        valType = False                 #
        user_input = input("Input command, 'h' for help. ")
        if user_input.lower() == 'h':   #input h for help
            print(gInstructions)
        elif user_input.lower() == 'q': #input q for quit
            playing = False
        elif user_input.isdigit():      #check computeLifeCycle turns
            if int(user_input) > 0:
                for k in range(int(user_input)):
                    game_world.computeLifeCycle()   #compute k Cycles
                game_world.printMap()
        elif user_input == "":          #only 1 Cycle
            game_world.computeLifeCycle()
            game_world.printMap()
        elif user_input.split(' ')[0].lower() == "spawn":   #spawn command
            if (user_input.split(' ')[1]).isdigit:  #check valid input
                if int(user_input.split(' ')[1]) > 0:
                    valInt = True
                else:
                    errormessage.append('The second argument has to be a '
                                        'positive Integer. ')
            else:
                errormessage.append('The second argument has to be a '
                                    'positive Integer. ')
            if user_input.split(' ')[2].lower() in things:
                valType = True
            else:
                errormessage.append('The third argument needs to be an '
                                    'implemented Creature or Plant.')
            if valType and valInt:
                if user_input.split(' ')[2].lower() == "corn":
                    available_spaces = []           #clear valid spaces
                    for width in range(game_world._width):
                        for height in range(game_world._height):
                            if game_world.Dictionary[width, height] is None:
                                available_spaces.append((width, height))
                                #append all coords of not taken fields
                                #from dictionary
                    random.shuffle(available_spaces)    #shuffle spaces
                    if len(available_spaces) < int(user_input.split(' ')[1]):
                        for width in range(game_world._width):
                            for height in range(game_world._height):
                                if isinstance(game_world.Dictionary[width,
                                                                    height],
                                              Plant):
                                    available_spaces.append((width, height))
                    #if available spaces are not enough, plant spots will
                    #be added to available spaces
                    for x in range(int(user_input.split(' ')[1]) if
                                   (int(user_input.split(' ')[1]) <
                                    len(available_spaces)) else
                                   len(available_spaces)):
                        create_corn(available_spaces[x], game_world, 6)
                        #corn gets spawned
                    game_world.printMap()   #show map
                if user_input.split(' ')[2].lower() == "mouse":
                    available_spaces = []           #clear valid spaces
                    for width in range(game_world._width):
                        for height in range(game_world._height):
                            if game_world.Dictionary[width, height] is None:
                                available_spaces.append((width, height))
                                #append all coords of not taken fields
                                #from dictionary
                    random.shuffle(available_spaces)    #shuffle spaces
                    if len(available_spaces) < int(user_input.split(' ')[1]):
                        for width in range(game_world._width):
                            for height in range(game_world._height):
                                if isinstance(game_world.Dictionary[width,
                                                                    height],
                                              Plant):
                                    available_spaces.append((width, height))
                    #if available spaces are not enough, plant spots will
                    #be added to available spaces
                    for x in range(int(user_input.split(' ')[1]) if
                                   (int(user_input.split(' ')[1]) <
                                    len(available_spaces)) else
                                   len(available_spaces)):
                        create_mouse(available_spaces[x], game_world, 12, 7,
                                     25)
                    game_world.printMap()
            else:
                print('\n'.join(errormessage))   #put errormessages together
        else:
            print("Input h to access the instructions.")

playGame() #starts game

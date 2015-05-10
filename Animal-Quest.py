# SWE100 - Intro to Python
# L G
# Final Assignment: Pygame "ANIMAL QUEST"

# NOTES:

# !!! Code in animal abilities and functionalities
# !! Add proper comments in code to explain what blocks of code do
# DONE !! Replace "index <=" essence value with an array for dynamic aquiring.
# DONE !! How to spawn food item on demand?  Also would work with how to spawn any object??  Hook into "Pawn" function if possible...
# DONE OrderedUpdates() > DefaultLayer allows for sprite layers within a group.

# Ideally, Item/Player/Animal and any other board object can stem from a common "Pawn" base class...
# I tried to do this but it caused a lot of problems.  Something to look into for future refinement.

# Map design and coding.  How to organize 'level designs'?
# Finish making sprites so I can import and start testing functionality.
  # Ability graphics and objects/terrain.
# Is there a way to call the object that the cursor is colliding with?  I can call objects instead of having to hard code in collisions.
  # Used with for loop to call pawn in pawn_group.  Could be expanded to detect objects from different groups...?

import pygame

pygame.init()

title_font = pygame.font.SysFont("Lucida Console", 17, False, False)
console_font = pygame.font.SysFont("Lucida Console", 13, False, False)

version = 0.5
# Statistics for window dimensions and tile definitions.
pygame.display.set_caption('Animal Quest v %s' % version)
window_width = 800
window_height = 600
tile_size = 32
tile_rows = 25
tile_columns = 18
ui_height = 200

screen = pygame.display.set_mode([window_width, window_height + ui_height])
board_width = tile_size * tile_rows
board_height = tile_size * tile_columns
background = pygame.Surface(screen.get_size())
background = background.convert()

background.fill([0, 0, 0])
screen.blit(background, (0, 0))

# board = Board (TILESIZE, TILESWIDTH, TILESHEIGHT)

def load_image(filename):
    image = pygame.image.load(filename)
    return image


def make_sprite(filename):
    sprite = pygame.sprite.Sprite()
    image = pygame.image.load(filename)
    sprite.image = image.convert_alpha()
    sprite.rect = sprite.image.get_rect()
    sprite.mask = pygame.mask.from_surface(sprite.image)
    return sprite


def draw_sprite(sprite):
    background.blit(sprite.image, sprite.rect)

#Defines dimentions of board.  Used to determine where sprites can move or be placed. (Borders)
def board_space(self):
    if 0 <= self.coords[0] <= 24 and 0 <= self.coords[1] <= 18:
        return True
    else:
        return False


# Used to detect if two objects are adjacent to eachother or not.
def is_adjacent(self, other):
    x = (self.coords[0] - other.coords[0])
    y = (self.coords[1] - other.coords[1])
    if -1 <= x <= 1 and -1 <= y <= 1:
        return True
    else:
        return False


class Player(pygame.sprite.Sprite):
    default_layer = 5
    inventory = []
    essence = ['spirit']
    coords = (0, 0)
    base_id = ('spirit')
    ability1 = ('Illuminate')
    trait = ('Hover')

    def __init__(self, x, y):
        super(Player, self).__init__()
        self.images = []
        self.images.append(load_image('spirit.png'))
        self.images.append(load_image('spiritstag.png'))
        self.images.append(load_image('spiritwolf.png'))
        self.images.append(load_image('spiritrat.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(0, 0, 32, 32)
        self.mask = pygame.mask.from_surface(self.image)
        self.coords = (x, y)

        self.isactive = True
        self.call_form()

    # Update function that redraws sprite on movement, and refreshes sprite on form change.
    def update(self):
        self.image = self.images[self.index]
        self.rect.centerx = self.coords[0] * tile_size + self.rect.width / 2
        self.rect.centery = self.coords[1] * tile_size + self.rect.height / 2

    def call_form(self):
        #Calls base_id and set appropriate sprite and base_id value for other functions to use.
        if self.base_id == ('spirit'):
            self.index = 0
        elif self.base_id == ('stag'):
            self.index = 1
        elif self.base_id == ('wolf'):
            self.index = 2
        elif self.base_id == ('rat'):
            self.index = 3

        if self.base_id == ('spirit'):
            self.ability1 = ('Illuminate')
            self.trait = ('Hover')
        if self.base_id == ('stag'):
            self.ability1 = ('Carry')
            self.trait = ('Strength')
        if self.base_id == ('wolf'):
            self.ability1 = ('Dig')
            self.trait = ('Track & Smell')
        if self.base_id == ('rat'):
            self.ability1 = ('Sneak')
            self.trait = ('Small')

    #def ability(self):
        #if self.ability1 == ('Illuminate')


    #Form changing code here!  Draws forms from array list, and sorts them in the order you have acquired them in.
    def invoke(self):
        if len(player.essence) == 1:
            console_scroll('You have no Aspects to invoke at this time.')
            player.isactive = True
        elif len(player.essence) == 2:
            console_scroll('Invoke which Aspect?')
            console_scroll('1: {0} 2: {1}'.format(player.essence[0], player.essence[1]))
        elif len(player.essence) == 3:
            console_scroll('Invoke which Aspect?')
            console_scroll('1: {0} 2: {1} 3: {2}'.format(player.essence[0], player.essence[1], player.essence[2]))
        elif len(player.essence) == 4:
            console_scroll('Invoke which Aspect?')
            console_scroll('1: {0} 2: {1} 3: {2} 4: {3}'.format(player.essence[0], player.essence[1], player.essence[2],
                                                                player.essence[3]))

        print ('FormID:', player.base_id)

    #Look interactions to call on when player is targeted with "look"
    def look(self):
        if self.base_id == ('spirit'):
            console_scroll('You are an Aspect of Nature. You glow with a brilliant radiance.')
            console_scroll(
                'As a {0}, you can {1} your surroundings and reveal hidden objects or creatures.'.format(self.base_id,
                                                                                                         self.ability1))
            console_scroll('You can also {0} over most terrain.'.format(self.trait))

        else:
            console_scroll('You have invoked the blessing of the {0}.'.format(self.base_id))

        if self.base_id == ('stag'):
            console_scroll(
                'The {0} can use its {1} to push objects, and can also {2} other animals.'.format(self.base_id,
                                                                                                  self.trait,
                                                                                                  self.ability1))

        if self.base_id == ('wolf'):
            console_scroll('The {0} can {1} up objects with its paws.'.format(self.base_id, self.ability1))
            console_scroll('It can also {0} other creatures and hidden treasure.'.format(self.trait))

        if self.base_id == ('rat'):
            console_scroll(
                'The {0} can use its {1} size to squeeze into tight spaces.  It can also {2} by other animals.'.format(
                    self.base_id, self.trait, self.ability1))

#Spawns instance of player on board.  Must come before Cursor since Cursor uses player.coords to find location to spawn at.
player = Player(12, 11)

#Item Base class that all items will derive from.
class Item(pygame.sprite.Sprite):
    default_layer = 2
    base_id = ('item')
    coords = (0, 0)

    def __init__(self, x, y):
        super(Item, self).__init__()
        self.images = []
        self.index = 0
        self.rect = pygame.Rect(0, 0, 32, 32)
        self.coords = (x, y)
        print ('Base class method was called: Item')

    def look(self):
        console_scroll('There is an {} here'.format(self.base_id))


    def interact(self):

        is_adjacent(self, player)

        if is_adjacent(self, player):
            console_scroll('You pick up the {}.'.format(self.base_id))
            player.inventory.append('ITEM_BASECLASS')
            self.kill()

        elif not is_adjacent(self, player):
            console_scroll('You are not close enough to pick up the {}.'.format(self.base_id))


class Food(Item):
    base_id = ('Food')

    def __init__(self, x, y):
        Item.__init__(self, x, y)
        self.images = []
        self.images.append(load_image('item_food.png'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(0, 0, 32, 32)
        self.coords = (x, y)
        print ('Derived class method called: Food')

    def update(self):
        self.rect.centerx = self.coords[0] * tile_size + self.rect.width / 2
        self.rect.centery = self.coords[1] * tile_size + self.rect.height / 2

    def look(self):
        console_scroll('There is {0} here.  It looks delicious.'.format(self.base_id))


    def interact(self):

        is_adjacent(self, player)

        if is_adjacent(self, player):
            console_scroll('You pick up the {}.'.format(self.base_id))
            player.inventory.append('food')
            self.kill()


        elif not is_adjacent(self, player):
            console_scroll('You are not close enough to pick up the {}.'.format(self.base_id))

    def place(self, x, y):
        self.add(pawn_group)
        self.coords = (x, y)
        self.add(game_sprites_group)
        self.update()

        print ('Food has been placed on the grid.')


class Cursor(pygame.sprite.Sprite):
    coords = (player.coords[0], player.coords[1])
    default_layer = 5
    def __init__(self, x, y):
        super(Cursor, self).__init__()
        self.images = []
        self.images.append(load_image('cursor1.png'))
        self.images.append(load_image('cursor2.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(0, 0, 32, 32)

        self.counter = 0
        self.maxcount = 12

    #Cursor animation cycle
    def blink(self):
        self.counter += 1
        if self.counter == 12:
            self.index += 1
            self.counter = 0
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def update(self):
        self.rect.centerx = self.coords[0] * tile_size + self.rect.width / 2
        self.rect.centery = self.coords[1] * tile_size + self.rect.height / 2

    def on(self):
        cursor.coords = player.coords
        cursor.add(game_sprites_group)
        player.isactive = False
        print ('Active:', player.isactive)
        print ('Cursor spawn at:', cursor.coords)
        print ('Cursor Toggle:', cursor.alive())

    def off(self):
        cursor.kill()
        cursor.counter = 0
        cursor.index = 0
        player.isactive = True
        print ('Active:', player.isactive)
        print ('Cursor Mode:', cursor.alive())


#--- Ability Classes Here ---

class player_ability(pygame.sprite.Sprite):
    base_id = ('player_ability')
    default_layer = 4
    coords = (0, 0)

    def __init__(self, x, y):
        super(player_ability, self).__init__()
        self.coords = (x, y)
        self.rect = pygame.Rect(0, 0, 32, 32)
        print ('Base class method was called: Ability')

    def update(self):
        self.rect.centerx = player.coords[0] * tile_size + self.rect.width / 2
        self.rect.centery = player.coords[1] * tile_size + self.rect.height / 2

    def on(self, x, y):
        self.add(game_sprites_group)
        self.add(ability_group)
        self.update()
        print ('ability.on called')

    def off(self):
        player_ability.kill()

class Illuminate(player_ability):
    base_id = ('illuminate')
    coords = (player.coords[0], player.coords[1])
    ability_range = 3

    def __init__(self, x, y):
        player_ability.__init__(self, x, y)
        self.image = load_image('ability_illuminate.png')
        self.rect = self.image.get_rect()
        self.coords = (player.coords[0], player.coords[1])
        print self.rect.width, self.rect.height

    def in_range(self, other):
        if (abs(self.coords[0] - other.coords[0]) + abs(self.coords[1] - other.coords[1]) <= self.ability_range):
            return True

    def trigger(self, other):
        if illuminate.alive():
            if self.in_range(self, other):
                try:
                    other.flag_illuminate = True
                    print ('[0].illuminate: [1]'.format(other, other.flag_illuminate))
                except:
                    return


class Animal(pygame.sprite.Sprite):
    flag_illuminate = False
    default_layer = 4
    base_id = ('animal')
    greeting = 0
    coords = (0, 0)

    def __init__(self, x, y):
        super(Animal, self).__init__()
        self.images = []
        self.index = 0
        self.rect = pygame.Rect(0, 0, 32, 32)
        self.coords = (x, y)
        print ('Base class method was called: Animal')

    def update(self):
        self.rect.centerx = self.coords[0] * tile_size + self.rect.width / 2
        self.rect.centery = self.coords[1] * tile_size + self.rect.height / 2

    def look(self):
        console_scroll('There is an {} here'.format(self.base_id))


    def interact(self):

        is_adjacent(self, player)

        if is_adjacent(self, player):
            console_scroll('The {} regards you with a benign curiosity.'.format(self.base_id))


        elif not is_adjacent(self, player):
            console_scroll('You are not close enough to interact with the {}.'.format(self.base_id))


class Stag(Animal):
    base_id = ('stag')

    def __init__(self, x, y):
        Animal.__init__(self, x, y)
        self.images = []
        self.images.append(load_image('npcstagsick.png'))
        self.images.append(load_image('npcstag.png'))
        self.index = 0

        self.image = self.images[self.index]
        self.rect = pygame.Rect(0, 0, 32, 32)
        self.coords = (x, y)
        print ('Derived class method was called: Stag.')

    def look(self):
        console_scroll('You look at {0}.'.format(self.base_id))
        if self.greeting == 0:
            console_scroll(
                'The {0} trembles in fear of the darkness around it.  Perhaps you can aid the poor {0}?'.format(
                    self.base_id))
        if self.greeting == 1:
            console_scroll(
                'The {0} seems to be at ease now.  You have helped cure the {0} of its worry!'.format(self.base_id))


    def interact(self):
        is_adjacent(self, player)

        if is_adjacent(self, player):

            if self.greeting == 0:
                console_scroll('The {0} seems to be at ease now, comforted by the light of your [Illuminate].'.format(
                    self.base_id))
                self.greeting = 1
                self.index = 1
                self.image = self.images[self.index]
                player.essence.append('stag')
                console_scroll(
                    'In response to your aid, the {0} has entreated its blessing to you.'.format(self.base_id))
                console_scroll('You can now invoke the aspect of the [stag]!'.format(self.base_id))

            elif self.greeting == 1:
                console_scroll(
                    'You have already helped the {0}.  The {0} gently bows its head in gratitude.'.format(self.base_id))

        elif not is_adjacent(self, player):
            console_scroll('You are not close enough to interact with the {}.'.format(self.base_id))


class Wolf(Animal):
    base_id = ('wolf')

    def __init__(self, x, y):
        Animal.__init__(self, x, y)
        self.images = []
        self.images.append(load_image('npcwolfsick.png'))
        self.images.append(load_image('npcwolf.png'))
        self.image = self.images[self.index]

        print ('Derived class method was called: Wolf.')

    def look(self):
        if self.index == 0:
            console_scroll(
                'You look at the {0}. The {0} appears to have wounded its paw and cannot easily move.'.format(
                    self.base_id))
            console_scroll(
                'The {0} looks longingly at the rising moon.  If only it could get a better view.'.format(self.base_id))

        if self.index == 1:
            console_scroll('The {0} seems to be much happier now that it can watch the moon rise!'.format(self.base_id))

    def interact(self):
        is_adjacent(self, player)

        #Needs puzzle implemented and wolf interaction pre/post puzzle solve
        if is_adjacent(self, player):

            if self.greeting == 0:
                console_scroll(
                    'The {0} bows its head in thanks to you, now the {0} can enjoy the view'.format(self.base_id))
                self.greeting = 1
                self.index = 1
                self.image = self.images[self.index]
                player.essence.append('wolf')

                console_scroll('As a token of gratitude, the {0} has entreated its blessing to you.'.format(self.base_id))
                console_scroll('You can now invoke the aspect of the {0}!'.format(self.base_id))

            elif self.greeting == 1:
                console_scroll(
                    'In thanks for your help, the {0} also informs you of some food it has buried nearby.'.format(
                        self.base_id))
                food.place(4, 4)
                self.greeting = 2

            elif self.greeting == 2:
                console_scroll('You have already helped the {0}.  The {0} bows its head in gratitude.'.format(self.base_id))

        elif not is_adjacent(self, player):
            console_scroll('You are not close enough to interact with the {0}.'.format(self.base_id))



class Rat(Animal):
    base_id = ('rat')

    def __init__(self, x, y):
        Animal.__init__(self, x, y)
        self.images = []
        self.images.append(load_image('npcratsick.png'))
        self.images.append(load_image('npcrat.png'))
        self.image = self.images[self.index]

        print ('Derived class method was called: {0}.'.format(self.base_id))

    def look(self):
        if self.index == 0:
            console_scroll(
                'You look at the {0}. The {0} looks very hungry, but cannot find any food.'.format(self.base_id))
        elif self.index == 1:
            console_scroll('The {0} seems satisfied by its meal and is healthy again!'.format(self.base_id))

    def interact(self):
        is_adjacent(self, player)

        if is_adjacent(self, player):

            if self.greeting == 0:
                if 'food' in player.inventory:
                        console_scroll(
                            'The {0} eagerly accepts the offering of food and scarfs it down hungrily'.format(
                                self.base_id))
                        self.index = 1
                        self.image = self.images[self.index]
                        player.essence.append('rat')
                        player.inventory.remove('food')
                        self.greeting = 1
                        console_scroll(
                            'As a token of gratitude, the {0} has entreated its blessing to you.'.format(self.base_id))
                        console_scroll('You can now invoke the aspect of the {0}!'.format(self.base_id))

                elif 'food' not in player.inventory:
                    console_scroll(
                        'The {0} looks at you weakly.  Food could help this poor {0} regain its strength.'.format(
                            self.base_id))

            elif self.greeting == 1:
                console_scroll('You have already helped the {0}.  The {0} bows its head in gratitude.'.format(
                    self.base_id))

        elif not is_adjacent(self, player):
                console_scroll('You are not close enough to interact with the {0}.'.format(self.base_id))

#Instances of non-player objects

illuminate = Illuminate(player.coords[0], player.coords[1])

cursor = Cursor(player.coords[0], player.coords[1])

food = Food(Food.coords[0], Food.coords[1])

pawn = [Wolf(8, 12), Stag(12, 8), Rat(16, 12)]

pawn_group = pygame.sprite.Group(pawn)

#Array to funnel and kill all ability functions
ability_group = []


#Movement library
arrow_keys = {pygame.K_LEFT: (-1, 0),
              pygame.K_RIGHT: (+1, 0),
              pygame.K_UP: ( 0, -1),
              pygame.K_DOWN: ( 0, +1)
              }

cursor_keys = [pygame.K_a, pygame.K_s]


#Blank grid & UI Sprites/sorting.
testboard = make_sprite('grid.png')

UI_sprites = Cursor(player.coords[0], player.coords[1])
UI_group = pygame.sprite.Group(UI_sprites)

game_sprites = [player, pawn]
game_sprites_group = pygame.sprite.LayeredUpdates(game_sprites)

#Defines dimensions of the UI!  Use this for placing text within the surface area.
ui_surface = pygame.Surface((800, 200))
ui_surface_pos = ui_surface.get_rect()
ui_surface_pos.x = 0
ui_surface_pos.y = background.get_rect().bottom - 192

#array for console line buffer
console_lines = []

#This is what prints messages to the on screen "console" space.
def console_scroll(string):
    max_lines = 5
    console_lines.append(string)

    while len(console_lines) > max_lines:
        console_lines.pop(0)


#This space is for printing UI text!
def update_UI():
    ui_surface.fill((0, 0, 0,))

    y_offset = 0

    for line in console_lines:
        console_text = console_font.render(line, 0, (255, 255, 255))
        console_pos = console_text.get_rect()
        console_pos.x = ui_surface.get_rect().left + 25
        console_pos.y = ui_surface.get_rect().top + 85 + y_offset

        ui_surface.blit(console_text, console_pos)

        y_offset += 16

    #Positioning and data for the UI header
    title_text = title_font.render(
        '''- - - - - - - - - - - - - - - Animal Quest v %s - - - - - - - - - - - - - - -''' % version, 0,
        (255, 255, 255))
    title_pos = title_text.get_rect()
    title_pos.centerx = ui_surface.get_rect().centerx
    title_pos.centery = ui_surface.get_rect().bottom - 178

    #Prints UI text to UI space.
    ui_actions01 = console_font.render(
        '''[a] Look  [s] Interact [d] Item  [f] Invoke   |         ''' + '[g] {0}   [Trait] {1}'.format(
            player.ability1, player.trait), 0, (255, 255, 255))
    ui_actions01_pos = ui_actions01.get_rect()
    ui_actions01_pos.x = +30
    ui_actions01_pos.centery = ui_surface.get_rect().top + 50

    #Draws text on screen
    ui_surface.blit(title_text, title_pos)
    ui_surface.blit(ui_actions01, ui_actions01_pos)
    background.blit(ui_surface, ui_surface_pos)
    screen.blit(background, (0, 0))


#Runtime loop.
runtime = True
while runtime:

    for ev in pygame.event.get():
        #Quits on window close or Esc keypress.
        if (ev.type == pygame.QUIT or ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE):
            runtime = False

        #When when player is not in control of character...
        if player.isactive == False:
            #When cursor is present
            if cursor.alive():
                if ev.type == pygame.KEYDOWN and ev.key in arrow_keys:
                    board_space(cursor)
                    (column, row) = cursor.coords
                    (dx, dy) = arrow_keys[ev.key]
                    cursor_newCoords = (column + dx, row + dy)
                    #Moves player to new Coordinates
                    cursor.coords = cursor_newCoords
                    if board_space(cursor) == False:
                        cursor.coords = (column, row)
                        cursor.update()
                    #Debug Coordinates Printed to Console
                    print ('Cursor moved to: {0}'.format(cursor.coords))
                if ev.type == pygame.KEYDOWN and ev.key == pygame.K_a:
                    #Collision detection for cursor to detect interactions
                    if pygame.sprite.collide_rect(cursor, player):
                        player.look()
                    else:
                        pawncollision = []
                        pawnfetch = []
                        for pawn in pawn_group:
                            if pygame.sprite.collide_rect(cursor, pawn):
                                pawncollision = True
                                pawnfetch = pawn
                        if pawncollision:
                            pawnfetch.look()
                        else:
                            console_scroll('There is nothing to look at here.')
                    cursor.off()

                if ev.type == pygame.KEYDOWN and ev.key == pygame.K_s:
                    pawncollision = []
                    pawnfetch = []
                    for pawn in pawn_group:
                        if pygame.sprite.collide_rect(cursor, pawn):
                            pawncollision = True
                            pawnfetch = pawn
                    if pawncollision:
                        pawnfetch.interact()

                    else:
                        console_scroll('There is nothing to interact with here.')

                    cursor.off()


            #Invoke action form changes here
            #When cursor is inactive and player does not have control (used to check for non selection prompts)
            if not cursor.alive():

                #Conditionals for form changing.  Checks number of blessings in list and then adjusts accordingly.
                if ev.type == pygame.KEYDOWN and ev.key == pygame.K_1 and len(player.essence) >= 1:
                    player.base_id = ('{0}'.format(player.essence[0]))
                    player.call_form()
                    console_scroll('You invoke the aspect of the {0}.'.format(player.base_id))
                    player.isactive = True

                elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_2 and len(player.essence) >= 2:
                    player.base_id = ('{0}'.format(player.essence[1]))
                    player.call_form()
                    console_scroll('You invoke the aspect of the {0}.'.format(player.base_id))
                    player.isactive = True

                elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_3 and len(player.essence) >= 3:
                    player.base_id = ('{0}'.format(player.essence[2]))
                    player.call_form()
                    console_scroll('You invoke the aspect of the {0}.'.format(player.base_id))
                    player.isactive = True

                elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_4 and len(player.essence) >= 4:
                    player.base_id = ('{0}'.format(player.essence[3]))
                    player.call_form()
                    console_scroll('You invoke the aspect of the {0}.'.format(player.base_id))
                    player.isactive = True


        #If player is active use following inputs
        elif player.isactive:

            if ev.type == pygame.KEYDOWN:
                if ev.key in arrow_keys:
                    board_space(player)
                    (column, row) = player.coords
                    (dx, dy) = arrow_keys[ev.key]
                    player_newCoords = (column + dx, row + dy)
                    #Moves player to new Coordinates
                    player.coords = player_newCoords
                    player.update()

                    for pawn in pawn_group:
                        if pygame.sprite.collide_rect(player, pawn):
                            player.coords = (column, row)
                            player.update()

                    if board_space(player) == False:
                        player.coords = (column, row)
                        player.update()

                    #Debug Coordinates Printed to Console              
                    print('Player moved to: {0}'.format(player_newCoords))
                    print('Player is on board: {0}'.format(board_space(player)))

                    #Spawns and sets "Cursor Mode"
                if ev.type == pygame.KEYDOWN and ev.key in cursor_keys:
                    if ev.key == pygame.K_a:
                        console_scroll('Look at what?')
                    if ev.key == pygame.K_s:
                        console_scroll('Interact with what?')
                    cursor.on()

                if ev.type == pygame.KEYDOWN and ev.key == pygame.K_d:
                    if len(player.inventory) == 0:
                        console_scroll('You currently have no items in your inventory.')
                    else:
                        console_scroll('You currently have the following items:')
                        console_scroll('{0}'.format(' '.join(player.inventory)))

                if ev.type == pygame.KEYDOWN and ev.key == pygame.K_f:
                    #Triggers invoke prompt
                    player.isactive = False
                    player.invoke()

                if ev.type == pygame.KEYDOWN and ev. key == pygame.K_g:
                    if player.base_id == ('spirit'):
                        illuminate.on(player.coords[0], player.coords[1])



        #Updates sprite positions on grid.  Main loop, otherwise sprites spawn at (0, 0) and snap later.
        player.update()
        illuminate.update()
        print illuminate.update()

        try:
            if illuminate in ability_group:
                illuminate.update()

        except:
            pass

        if cursor in game_sprites_group:
            cursor.update()

        for pawn in pawn_group:
            pawn.update()


    #Graphics

    screen.blit(background, (0, 0))
    draw_sprite(testboard)
    background.blit(ui_surface, ui_surface_pos)
    game_sprites_group.draw(background)

    update_UI()

    if cursor in game_sprites_group:
        cursor.blink()

    pygame.display.flip()
    pygame.time.wait(30)

pygame.quit()

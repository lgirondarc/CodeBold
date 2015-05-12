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
import random

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

def random_coords(other):
    x = random.randint(0, tile_rows)
    y = random.randint(0, tile_columns)
    other.coords = (x, y)

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

def is_beside(self, other):
    x = (self.coords[0] - other.coords[0])
    y = (self.coords[1] - other.coords[1])
    if -1 <= x <= 1 and -1 <= y <= 1 and (x != 0 or y != 0):
        return True
    else:
        return False

class Player(pygame.sprite.Sprite):
    layer = 5
    inventory = []
    essence = ['spirit']
    coords = (0, 0)
    base_id = ('spirit')
    ability1 = ('Illuminate')
    trait = ('Hover')
    carry_id = []
    is_carrying = []

    def __init__(self, x, y):
        super(Player, self).__init__()
        self.images = []
        self.images.append(load_image('spirit.png'))
        self.images.append(load_image('spiritstag.png'))
        self.images.append(load_image('spiritwolf.png'))
        self.images.append(load_image('spiritrat.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(0, 0, 31, 31)
        self.mask = pygame.mask.from_surface(self.image)
        self.coords = (x, y)

        self.isactive = True

    # Update function that redraws sprite on movement, and refreshes sprite on form change.
    def update(self):
        self.image = self.images[self.index]
        self.rect.centerx = self.coords[0] * tile_size + self.rect.width / 2
        self.rect.centery = self.coords[1] * tile_size + self.rect.height / 2

    def call_form(self):
        console_scroll('You invoke the aspect of the {0}.'.format(player.base_id))

        #Calls base_id and set appropriate sprite and base_id value for other functions to use.
        if self.base_id == ('spirit'):
            self.index = 0
        elif self.base_id == ('stag'):
            self.index = 1
        elif self.base_id == ('wolf'):
            self.index = 2
            console_scroll ('You begin tracking with your acute senses.')
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

    def ability_check(self):
        if not self.base_id == ('spirit'):
            if illuminate.alive():
                illuminate.kill()
                for pawn in pawn_group:
                    illuminate.trigger(pawn)

        if not self.base_id == ('wolf'):
            if tracking.active:
                tracking.active = False
                console_scroll ('You stop tracking.')

        elif self.base_id == ('wolf'):
            tracking.active = True


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
player = Player(12, 9)

#Item Base class that all items will derive from.
class Item(pygame.sprite.Sprite):
    flag_tracked = False
    hidden = False
    layer = 2
    base_id = ('item')
    coords = (0, 0)

    def __init__(self, x, y):
        super(Item, self).__init__()
        self.images = []
        self.index = 0
        self.rect = pygame.Rect(0, 0, 31, 31)
        self.coords = (x, y)
        print ('Base class method was called: Item')

    def look(self):
        console_scroll('There is an {0} here'.format(self.base_id))

    def update(self):
        self.rect.centerx = self.coords[0] * tile_size + self.rect.width / 2
        self.rect.centery = self.coords[1] * tile_size + self.rect.height / 2

    def interact(self):

        is_adjacent(self, player)

        if is_adjacent(self, player):
            console_scroll('You pick up the {}.'.format(self.base_id))
            player.inventory.append('ITEM_BASECLASS')
            self.kill()

        elif not is_adjacent(self, player):
            console_scroll('You are not close enough to pick up the {}.'.format(self.base_id))

    def place(self, x, y):
        #self.add(item)
        self.add(item_group)
        self.coords = (x, y)
        self.update()

        print ('{} has been placed on the grid.'.format(self.base_id))


class Food(Item):
    base_id = ('Food')

    def __init__(self, x, y):
        Item.__init__(self, x, y)
        self.images = []
        self.images.append(load_image('item_food.png'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(0, 0, 31, 31)
        self.coords = (x, y)
        print ('Derived class method called: Food')

    def look(self):
        if not self.hidden:
            console_scroll('There is {0} here.  It looks delicious.'.format(self.base_id))

        elif self.hidden:
            if not player.base_id == ('wolf'):
                console_scroll('There is nothing to look at here.')
            else:
                console_scroll('Your acute tracking senses tell you something is buried here.')


    def interact(self):
        if not self.hidden:

            if is_adjacent(self, player):
                console_scroll('You pick up the {}.'.format(self.base_id))
                player.inventory.append('food')
                self.kill()

            elif not is_adjacent(self, player):
                console_scroll('You are not close enough to pick up the {}.'.format(self.base_id))

        elif self.hidden:
            if not player.base_id == ('wolf'):
                console_scroll('There is nothing to interact with here.')
            else:
                console_scroll('Your acute tracking senses tell you something is buried here.')


class Cursor(pygame.sprite.Sprite):
    base_id = ('normal')
    coords = (player.coords[0], player.coords[1])
    layer = 6
    def __init__(self, x, y):
        super(Cursor, self).__init__()
        self.images = []
        self.images.append(load_image('cursor1.png'))
        self.images.append(load_image('cursor2.png'))
        self.images.append(load_image('ability_cursor.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(0, 0, 32, 32)

        self.counter = 0
        self.maxcount = 12

    def check_id(self):
        if self.base_id == ('normal'):
            self.index = 0
        if self.base_id == ('ability'):
            self.index = 2
        self.image = self.images[self.index]

    #Cursor animation cycle
    def blink(self):
        self.counter += 1
        if self.counter == 12:
            if self.index == 0:
                self.index += 1
                self.counter = 0
            elif self.index == 1:
                if self.base_id == ('normal'):
                    self.index -= 1
                    self.counter = 0
                if self.base_id == ('ability'):
                    self.index += 1
                    self.counter = 0
            elif self.index == 2:
                self.index -= 1
                self.counter = 0

        self.image = self.images[self.index]

    def update(self):
        self.rect.centerx = self.coords[0] * tile_size + (self.rect.width / 2) - 1
        self.rect.centery = self.coords[1] * tile_size + (self.rect.height / 2) - 1

    def on(self):
        cursor.check_id()
        cursor.coords = player.coords
        cursor.add(game_sprites_group)
        player.isactive = False
        print ('Active:', player.isactive)
        print ('Cursor spawn at:', cursor.coords)
        print ('Cursor Toggle:', cursor.alive())

    def off(self):
        cursor.kill()
        cursor.counter = 0
        player.isactive = True
        print ('Active:', player.isactive)
        print ('Cursor Mode:', cursor.alive())

    def ability_action(self):
        if player.base_id == ('stag'):
            ability_carry(pawn)
        if player.base_id == ('wolf'):
            ability_dig(object)


#--- Ability Classes Here ---

class player_ability(pygame.sprite.Sprite):
    base_id = ('player_ability')
    layer = 5
    coords = (0, 0)

    def __init__(self, x, y):
        super(player_ability, self).__init__()
        self.coords = (x, y)
        self.rect = pygame.Rect(0, 0, 32, 32)
        print ('Base class method was called: Ability')

    def update(self):
        self.coords = player.coords
        self.rect.centerx = player.coords[0] * tile_size + (tile_size / 2) - 1
        self.rect.centery = player.coords[1] * tile_size + (tile_size / 2) - 1

    def in_range(self, other):
        if (abs(self.coords[0] - other.coords[0]) + abs(self.coords[1] - other.coords[1]) <= self.ability_range):
            return True


class Illuminate(player_ability):
    base_id = ('illuminate')
    coords = (player.coords[0], player.coords[1])
    ability_range = 3

    def __init__(self, x, y):
        player_ability.__init__(self, x, y)
        self.image = load_image('ability_illuminate.png')
        self.rect = self.image.get_rect()
        self.coords = (player.coords[0], player.coords[1])

    def trigger(self, other):
        if illuminate.alive():
            if self.in_range(other):
                try:
                    other.flag_illuminate = True
                except:
                    pass
            else:
                try:
                    other.flag_illuminate = False
                except:
                    pass
        elif not illuminate.alive():
            try:
                other.flag_illuminate = False
            except:
                pass

    def toggle(self):
        if not illuminate.alive():
            self.add(effect_sprites_group)
        else:
            self.kill()

def ability_carry(pawn):
    if not player.is_carrying:
        pawncollision = []
        pawnfetch = []
        for pawn in pawn_group:
            if pygame.sprite.collide_rect(cursor, pawn):
                pawncollision = True
                pawnfetch = pawn
        if pawncollision:
            console_scroll ('You pick up and {0} the {1} upon your back.'.format(player.ability1, pawnfetch.base_id))
            player.is_carrying = (pawnfetch.base_id)
            player.carry_id = pawnfetch
            print ('Carrying:', player.is_carrying)

            for pawn in pawn_group:
                game_sprites_group.remove(pawnfetch)
                pawn_group.remove(pawnfetch)
                cursor.off()

        elif not pawncollision:
            console_scroll('There is nothing to carry here.')
            cursor.off()

    elif player.is_carrying:
        pawncollision = []
        for pawn in pawn_group:
            if pygame.sprite.collide_rect(cursor, pawn):
                pawncollision = True
            if pygame.sprite.collide_rect(cursor, player):
                pawncollision = True
        if pawncollision:
            console_scroll('You cannot place the {0} here!'.format(player.is_carrying))

        else:
            console_scroll ('You place the {0} down beside you.'.format(player.is_carrying))
            player.carry_id.coords = (cursor.coords[0], cursor.coords[1])
            game_sprites_group.add(player.carry_id)
            pawn_group.add(player.carry_id)
            player.is_carrying = []
            player.carry_id = []

        cursor.off()

def ability_dig(item):
    objectcollision = []
    object = []
    object_id = []
    for item in item_group:
        if pygame.sprite.collide_rect(cursor, item):
            objectcollision = True
            object = item.base_id
            object_id = item
    if objectcollision:
        if object_id.hidden:
            console_scroll ('You dug something up: {0}!'.format(item.base_id))
            item_group.add(object_id)
            effect_sprites_group.add(object_id)
            object_id.hidden = False
        elif not object_id.hidden:
            console_scroll ('The {0} is not buried.'.format(item.base_id))

        cursor.off()
    elif not objectcollision:
        console_scroll ('You dig, but find nothing.')
        cursor.off()

class Ability_Track(player_ability):
    active = False
    ability_range = 3
    coords = (player.coords[0], player.coords[1])

    def __init__(self, x, y):
        player_ability.__init__(self, x, y)
        self.coords = (player.coords[0], player.coords[1])

    def detect(self, other):
        if tracking.active:
            if self.in_range(other):
                if not other.flag_tracked:
                    try:
                        other.flag_tracked = True
                        print ('Tracking: {}'.format(other.base_id))
                        console_scroll('Your acute senses detect the {0} nearby.'.format(other.base_id))
                        if other.coords[0] > self.coords[0]:
                            console_scroll ('The {0} is east of here.'.format(other.base_id))
                        if other.coords[0] < self.coords[0]:
                            console_scroll ('The {0} is west of here.'.format(other.base_id))
                        if other.coords[1] > self.coords[1]:
                            console_scroll ('The {0} is south of here.'.format(other.base_id))
                        if other.coords[1] < self.coords[1]:
                            console_scroll ('The {0} is north of here.'.format(other.base_id))
                    except:
                        pass
                elif other.flag_tracked:
                    pass
            elif not self.in_range(other):
                if other.flag_tracked:
                    try:
                        other.flag_tracked = False
                        console_scroll ('The {0} you were tracking fades from your senses.'.format(other.base_id))
                    except:
                        pass
                elif not other.flag_tracked:
                    pass
        if not tracking.active:
            try:
                other.flag_tracked = False
            except:
                pass


#STAG CARRY IS HANDLED AS A CURSOR FUNCTION VIA VARIABLES & CONTROLS, LINKS INTO INDIVIDUAL INSTANCE FUNCTIONS

#--- Critter classes here! ---

class Animal(pygame.sprite.Sprite):
    flag_illuminate = False
    flag_tracked = False
    layer = 4
    base_id = ('animal')
    greeting = 0
    coords = (0, 0)


    def __init__(self, x, y):
        super(Animal, self).__init__()
        self.images = []
        self.index = 0
        self.rect = pygame.Rect(0, 0, 31, 31)
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
        self.rect = pygame.Rect(0, 0, 31, 31)
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
                if self.flag_illuminate:
                    console_scroll('The {0} seems to be at ease now, comforted by the light of your illuminate!'.format(
                        self.base_id))
                    self.greeting = 1
                    self.index = 1
                    self.image = self.images[self.index]
                    player.essence.append('stag')
                    console_scroll(
                        'In response to your aid, the {0} has entreated its blessing to you.'.format(self.base_id))
                    console_scroll('You can now invoke the aspect of the [stag]!'.format(self.base_id))

                else:
                    console_scroll ('The {0} eyes the darkness around it in terrified silence.'.format(self.base_id))

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

    def update(self):
        self.rect.centerx = self.coords[0] * tile_size + self.rect.width / 2
        self.rect.centery = self.coords[1] * tile_size + self.rect.height / 2
        self.pack_mate_check(pawn)

    def look(self):
        if self.index == 0:
            console_scroll(
                'You look at the {0}. The {0} appears to have wounded its paw and cannot easily move.'.format(
                    self.base_id))

        if self.index == 1:
            console_scroll('The {0} seems happier now that it has been reunited with its pack mate!'.format(self.base_id))

    def interact(self):
        is_adjacent(self, player)

        #Needs puzzle implemented and wolf interaction pre/post puzzle solve
        if is_adjacent(self, player):

            if self.index == 1 and self.greeting == 0:
                console_scroll ('The wolves are much happier now that they have been reunited with each other.')
                self.greeting = 1
                if not 'wolf' in player.essence:
                    player.essence.append('wolf')
                    console_scroll('As a token of gratitude, the wolves have entreated their blessing to you.'.format(self.base_id))
                    console_scroll('You can now invoke the aspect of the {0}!'.format(self.base_id))
                    console_scroll(
                        'In thanks for your help, the wolves inform you of some food they have buried nearby.'.format(
                            self.base_id))
                    food = Food (0, 0)
                    food.place(0, 0)
                    random_coords(food)
                    food.update()
                    food.hidden = True
            elif self.index == 0:
                console_scroll ('The {0} longs to be with its packmate.'.format(self.base_id))

            elif self.greeting == 1:
                console_scroll('You have already helped the {0} and its packmate.'
                               'They bow their heads in gratitude.'.format(self.base_id))

        elif not is_adjacent(self, player):
            console_scroll('You are not close enough to interact with the {0}.'.format(self.base_id))

    #Checks if wolves are next to each other.
    def pack_mate_check(self, other):
        is_beside(self,other)
        adjacent_ids = []
        for pawn in pawn_group:
            if is_beside(self, pawn):
                adjacent_ids.append(pawn.base_id)
            if ('wolf') in adjacent_ids:
               self.index = 1
               self.image = self.images[self.index]




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

tracking = Ability_Track(player.coords[0], player.coords[1])

cursor = Cursor(player.coords[0], player.coords[1])

item = []

item_group = pygame.sprite.Group(item)

pawn = [Wolf(4, 12), Stag(12, 4), Rat(20, 12), Wolf(22, 3)]

pawn_group = pygame.sprite.Group(pawn)

#Array to funnel and kill all ability functions
effect_sprites = []
effect_sprites_group = pygame.sprite.Group(effect_sprites)


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

game_sprites = [pawn, player]
game_sprites_group = pygame.sprite.OrderedUpdates(game_sprites)

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
                if cursor.base_id == ('normal'):
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
                            for item in item_group:
                                if pygame.sprite.collide_rect(cursor, item):
                                    pawncollision = True
                                    pawnfetch = item
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


                        for item in item_group:
                            if pygame.sprite.collide_rect(cursor, item):
                                pawncollision = True
                                pawnfetch = item
                        if pawncollision:
                            pawnfetch.interact()

                        else:
                            console_scroll('There is nothing to interact with here.')

                        cursor.off()

                #CURSOR ABILITIES HERE, DIG, CARRY, ETC

                if cursor.base_id == ('ability'):
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
                        if not is_adjacent(cursor, player):
                            cursor.coords = (column, row)
                            cursor.update
                        #Debug Coordinates Printed to Console
                        print ('Cursor moved to: {0}'.format(cursor.coords))

                    if ev.type == pygame.KEYDOWN and ev.key == pygame.K_g:
                        cursor.ability_action()
                        print ('Calling cursor.ability_action')

            #Invoke action form changes here
            #When cursor is inactive and player does not have control (used to check for non selection prompts)
            if not cursor.alive():

                #Conditionals for form changing.  Checks number of blessings in list and then adjusts accordingly.
                if ev.type == pygame.KEYDOWN and ev.key == pygame.K_1 and len(player.essence) >= 1:
                    player.base_id = ('{0}'.format(player.essence[0]))
                    player.call_form()
                    player.isactive = True

                elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_2 and len(player.essence) >= 2:
                    player.base_id = ('{0}'.format(player.essence[1]))
                    player.call_form()
                    player.isactive = True

                elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_3 and len(player.essence) >= 3:
                    player.base_id = ('{0}'.format(player.essence[2]))
                    player.call_form()
                    player.isactive = True

                elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_4 and len(player.essence) >= 4:
                    player.base_id = ('{0}'.format(player.essence[3]))
                    player.call_form()
                    player.isactive = True

                #Turns off any active abilities when switching to a form that does not have them.
                player.ability_check()

        #If player is active use following inputs
        elif player.isactive:

            if ev.type == pygame.KEYDOWN:
                if ev.key in arrow_keys:
                    board_space(player)
                    (column, row) = player.coords
                    (dx, dy) = arrow_keys[ev.key]
                    player_newCoords = (column + dx, row + dy)
                    #Moves player to new Coordinates


                    if player.base_id == ('stag'):
						pawncollision = []
                        pawnfetch = []
                        for pawn in pawn_group:
                            if pygame.sprite.collide_rect(player, pawn):
                                pawncollision = True
                                pawnfetch = pawn
                        if pawncollision:
                                print ('Object Collision Detected!')
                                board_space(pawnfetch)
                                (pawn_column, pawn_row) = pawnfetch.coords
                                (pawn_dx, pawn_dy) = arrow_keys[ev.key]
                                pawn_newCoords = (pawn_column + pawn_dx, pawn_row + pawn_dy)

                                pawnfetch.coords = pawn_newCoords #set and reverse if needed
                                player.coords = player_newCoords  #set and reverse if needed

                                for pawn in pawn_group:
                                        if pawn_newCoords == pawn.coords:
                                                print ('Objects reverted:')
                                                pawnfetch.coords = (pawn_column, pawn_row)
                                                player.coords = (column,row)

                                if not board_space(pawnfetch):
                                        pawnfetch.coords = (pawn_column - pawn_dx, pawn_row - pawn_dy)
                                pawnfetch.update()
                        else:
                                player.coords = player_newCoords

                        player.update()

                    else:
                        player.coords = player_newCoords
                        player.update()

                    if not player.base_id == ('spirit'):
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
                    cursor.base_id = ('normal')
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

                    #Global function to detect collisions???  It's used here & for cursor targeting.
                    pawncollision = []

                    for pawn in pawn_group:
                        if pygame.sprite.collide_rect(player, pawn):
                            pawncollision = True

                    if pawncollision:
                        console_scroll ('You cannot invoke a blessing while floating above something!')

                    if player.is_carrying:
                        console_scroll ('You cannot shift forms while carrying an object!')

                    elif not pawncollision:
                        #Triggers invoke prompt
                        player.isactive = False
                        player.invoke()

                #Ability Controls go here.
                if ev.type == pygame.KEYDOWN and ev. key == pygame.K_g:
                    cursor.base_id = ('ability')

                    if player.base_id == ('spirit'):
                        illuminate.toggle()

                    if player.base_id == ('stag'):
                        print ('Carrying: {0} | ID: {1}'.format(player.is_carrying, player.carry_id))
                        if not player.is_carrying:
                            console_scroll ('Pick up and carry what?')
                        elif player.is_carrying:
                            console_scroll ('Place the {0} where?'.format(player.is_carrying))
                        cursor.on()

                    if player.base_id == ('wolf'):
                        print ('Digging Mode Active')
                        console_scroll ('Dig where?')
                        cursor.on()



        #Updates sprite positions on grid.  Main loop, otherwise sprites spawn at (0, 0) and snap later.
        player.update()

        for item in item_group:
            item.update()

        if tracking.alive:
            tracking.update()
            for item in item_group:
                tracking.detect(item)
            for pawn in pawn_group:
                tracking.detect(pawn)


        for effect_sprites in effect_sprites_group:
            effect_sprites.update()

        if cursor in game_sprites_group:
            cursor.update()

        for pawn in pawn_group:
            pawn.update()
            illuminate.trigger(pawn)


    #Graphics

    screen.blit(background, (0, 0))
    draw_sprite(testboard)
    background.blit(ui_surface, ui_surface_pos)
    effect_sprites_group.draw(background)
    game_sprites_group.draw(background)

    update_UI()

    if cursor in game_sprites_group:
        cursor.blink()

    pygame.display.flip()
    pygame.time.wait(30)

pygame.quit()

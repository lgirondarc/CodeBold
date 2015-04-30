# SWE100 - Intro to Python
# L G
#Final Assignment: Pygame "ANIMAL QUEST" Alpha 0.3

# NOTES:
# Player transformations.  HUD Interactivity/drawing/printing to HUD space.
# Map design and coding.  How to organize 'level designs'?
#!!!! HUD functionality
# Anything listed/printed with brackets [] can be re-coded as string formatting to better address a modular approach.
# Finish making sprites so I can import and start testing functionality.
# Is there a way to call the object that the cursor is colliding with?  I can call objects instead of having to hard code in collisions.
# Maybe set a variable that is determined by collision, and returns object.  Then can use (self, selection), where selection is the variable that calls objects.
# Apparently I am using super.() completely wrong...  Probably should fix this. --> BaseClassName.__init__(self, args*)
# Trying to make a base class "pawn" that player/cursor/animal loads into is proving to be too difficult, I get a ton of errors and have no idea how to solve them.


import pygame

pygame.init()
pygame.font.init()

title_font = pygame.font.SysFont("courier", 17, False, False)
console_font = pygame.font.SysFont("courier", 15, False, False)

#from pygame_utilities import draw_text, sign

#Statistics for window dimensions and tile definitions.
pygame.display.set_caption('Animal Quest ALPHA 0.3')
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

#board = Board (TILESIZE, TILESWIDTH, TILESHEIGHT)

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


def board_space(self):
    if 0 <= self.coords[0] <= 24 and 0 <= self.coords[1] <= 18:
        return True
    else:
        return False


def is_adjacent(self, other):
    x = (self.coords[0] - other.coords[0])
    y = (self.coords[1] - other.coords[1])
    if -1 <= x <= 1 and -1 <= y <= 1:
        self.adjacent = True
    else:
        self.adjacent = False


class Player(pygame.sprite.Sprite):
    adjacent = []
    essence = 0
    default_layer = 4
    coords = (0, 0)

    def __init__(self, x, y):
        super(Player, self).__init__()
        self.images = []
        #Insert animal forms in here
        self.images.append(load_image('spirit.png'))
        self.images.append(load_image('spiritstag.png'))
        self.images.append(load_image('spiritwolf.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(0, 0, 32, 32)
        self.mask = pygame.mask.from_surface(self.image)
        self.coords = (x, y)

        #Player control flag
        self.isactive = True

    #"Move" code, used to update sprites on the grid.  Should this be a Global variable???
    def update(self):
        self.rect.centerx = self.coords[0] * tile_size + self.rect.width / 2
        self.rect.centery = self.coords[1] * tile_size + self.rect.height / 2

    def shift(self):
        if player.essence <= 0:
            print ('You have no additional essences to [shift] into at this time.')
            player.isactive = True
        elif player.essence <= 1:
            print ('[Shift] into which form?\n1: Spirit\n2: Stag')
        elif player.essence <= 2:
            print ('[Shift] into which form?\n1: Spirit\n2: Stag\n3: Wolf')
        elif player.essence >= 3:
            print ('[Shift] into which form?\n1: Spirit\n2: Stag\n3: Wolf\n4: Rat')

        self.image = self.images[self.index]

    #Code Look commands relating to player here.  Probably a way to store commands globally instead of per class.
    def look(self):
        if self.index == 0:
            print ('You [look] at an [Aspect of Nature].\nYou glow with a brilliant radiance.')
        if self.index == 1:
            print ('You have taken the form of a [stag].\nYou glow with a comforting radiance.')
        if self.index == 2:
            print ('You have taken the form of a [wolf].\nYou glow with a comforting radiance.')
        if self.index == 3:
            print ('You have taken the form of a [rat].\nYou glow with a comforting radiance.')

            #def interact(self, other):
            #if player.interact[1] = animal ### etc, to store ALL player interactions under player for clarity.


#Self.index to detect different animal forms.

player = Player(6, 6)

#def interact (self,other) ??? for specific interactive inputs [look] [use] etc?

class Cursor(pygame.sprite.Sprite):  #ADD DRAW CONDITIONS WHEN PLAYER PRESSES KEY, ALSO DISAPPEARS
    coords = (player.coords)

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
        print 'Active:', player.isactive
        print 'Cursor spawn at:', cursor.coords
        print 'Cursor Toggle:', cursor in game_sprites_group

    def off(self):
        cursor.kill()
        cursor.counter = 0
        cursor.index = 0
        player.isactive = True
        print 'Active:', player.isactive
        print 'Cursor Mode:', cursor in game_sprites_group


cursor = Cursor(player.coords[0], player.coords[1])


class Animal(pygame.sprite.Sprite):
    adjacent = []
    greeting = 1
    coords = (0, 0)
    #Look up Inheritance based classes for other animals.  Animal = Base class Wolf = Derived class that inherits from base
    #class DerivedClassName(BaseClassName):
    def __init__(self, x, y):
        super(Animal, self).__init__()
        self.images = []
        #Add other animal images here! Animal bones for dead animal, or animal sitting/laying?
        self.index = 0
        self.rect = pygame.Rect(0, 0, 32, 32)
        self.coords = (x, y)
        print ('Base class method was called: Animal')

    def update(self):
        self.rect.centerx = self.coords[0] * tile_size + self.rect.width / 2
        self.rect.centery = self.coords[1] * tile_size + self.rect.height / 2

    def look(self):
        print ('There is an animal here')


    def interact(self):

        is_adjacent(self, player)
        print self.adjacent

        if self.adjacent == True:

            if self.greeting == 1:
                print ('Bleeeergh I am dead!')
                self.greeting = 0
                player.essence = 1
                self.index = 1
                self.image = pygame.transform.rotate(self.image, 180)
                self.update()
                print (
                    '''[A lone stag] has entreated its essence as its dying wish.\nYou can now [shift] into a [stag]!''')

            elif self.greeting == 0:
                print ('This poor creature has passed on to a better place.  There is nothing more you can do.')

        elif self.adjacent == False:
            print ('You are not close enough to interact with this creature.')


class Stag(Animal):
    def __init__(self, x, y):
        Animal.__init__(self, x, y)
        self.images = []
        self.images.append(load_image('npcstag.png'))
        self.images.append(load_image('npcstagdead.png'))
        #Add other animal images here! Animal bones for dead animal, or animal sitting/laying?
        self.index = 0

        self.image = self.images[self.index]
        self.rect = pygame.Rect(0, 0, 32, 32)
        self.coords = (x, y)
        print ('Derived class method was called: Stag.')

    def look(self):
        print ('You [look] at [a lone stag].')
        if self.greeting == 1:
            print (
                '[A lone stag] appears to be mortally injured.  Its wounds are too severe to mend, but perhaps you can still grant some final solace.')
        if self.greeting == 0:
            print (
                'The lifeless body of [a lone stag] lays almost peacefully here.  There is nothing more you can do for it.')


    def interact(self):

        is_adjacent(self, player)
        print self.adjacent

        if self.adjacent == True:

            if self.index == 0 and self.greeting == 1:
                print ('Bleeeergh I am dead!')
                self.greeting = 0
                player.essence = 1
                self.index = 1
                self.image = self.images[self.index]
                self.image = pygame.transform.flip(self.image, False, True)
                print (
                    '''[A lone stag] has entreated its essence to you as its dying wish.\nYou can now [shift] into a [stag]!''')

            elif self.greeting == 0:
                print ('This poor creature has passed on to a better place.  You have done all you could have to help.')

        elif self.adjacent == False:
            print ('You are not close enough to interact with this creature.')


class Wolf(Animal):
    def __init__(self, x, y):
        Animal.__init__(self, x, y)
        self.images = []
        self.images.append(load_image('npcwolf.png'))
        self.image = self.images[self.index]

        print ('Derived class method was called: Wolf.')

    def look(self):
        print ('You [look] at [a wolf].\nIt is a wolf.')

    def interact(self):
        is_adjacent(self, player)
        print ('Player is adjacent:'), self.adjacent

        if self.adjacent == True:
            print ('WOLFED')
            player.essence = 2
            self.image = pygame.transform.flip(self.image, False, True)
            print ('''[A wolf] has entreated its essence to you as its dying wish.\nYou can now [shift] into a [wolf]!''')

        elif self.adjacent == False:
            print ('You are not close enough to interact with this creature.')


creature = [Wolf (8, 12), Stag (12, 8)]
creature_group = pygame.sprite.Group(creature)

#Movement library
arrow_keys = {pygame.K_LEFT: (-1, 0),
              pygame.K_RIGHT: (+1, 0),
              pygame.K_UP: ( 0, -1),
              pygame.K_DOWN: ( 0, +1)
              }

cursor_keys = [pygame.K_a, pygame.K_s]

#class display_HUD (x,y): ?


#Test Board and HUD stuff
testboard = make_sprite('grid.png')
testui = make_sprite('testUI.png')

UI_sprites = Cursor(player.coords[0], player.coords[1])
UI_group = pygame.sprite.Group(UI_sprites)

game_sprites = [player, creature]
game_sprites_group = pygame.sprite.Group(game_sprites)

#Dsiplay HUD info @ coords.  Needs specifics still.
#def display_HUD (x, y):

#Font/String Library, with group...? (For text in text_group...)

#Defines dimensions of the UI!  Use this for placing text within the surface area.
ui_surface = pygame.Surface((800, 200))
ui_surface_pos = ui_surface.get_rect()
ui_surface_pos.x = 0
ui_surface_pos.y = background.get_rect().bottom - 192

#Need a new surface WITHIN ui_surface for text prints only...???
test_message = console_font.render("This is a test message!", 0, (255, 255, 255))
console_pos = test_message.get_rect()
console_pos.x = ui_surface.get_rect().centerx - 375
console_pos.y = ui_surface.get_rect().centery - 13

title_text = title_font.render('- - - - - - - - - - - - - - - Animal Quest v 0.3 - - - - - - - - - - - - - - -', 0, (255, 255, 255))
title_pos = title_text.get_rect()
title_pos.centerx = ui_surface.get_rect().centerx
title_pos.centery = ui_surface.get_rect().bottom - 178



#Runtime loop.
runtime = True
while runtime:

    for ev in pygame.event.get():
        #Quits on window close or Esc keypress.
        if (ev.type == pygame.QUIT or
                        ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE):
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
                    print 'Cursor moved to:', cursor.coords
                if ev.type == pygame.KEYDOWN and ev.key == pygame.K_a:
                    #Should I load in ALL "looks" here?  Seems like the best thing would be to have interacts stored in classes/different objects...
                    #Ideally all "[ACTIONS]" and [OBJECTS] can be handled by scripting.
                    if pygame.sprite.collide_rect(cursor, player):
                        player.look()
                    else:
                        creaturecollision = []
                        animalfetch = []
                        for creature in creature_group:
                            if pygame.sprite.collide_rect(cursor, creature):
                                creaturecollision = True
                                animalfetch = creature
                        if creaturecollision:
                            animalfetch.look()
                        else:
                            print ('There is nothing to look at here.')
                    cursor.off()

                if ev.type == pygame.KEYDOWN and ev.key == pygame.K_s:
                    #NEEDS TO DETECT PROXIMITY TO PLAYER AND REFUSE INTERACT IF PLAYER IS TOO FAR AWAY.
                    creaturecollision = []
                    animalfetch = []
                    for creature in creature_group:
                        if pygame.sprite.collide_rect(cursor, creature):
                            creaturecollision = True
                            animalfetch = creature
                    if creaturecollision:
                        animalfetch.interact()

                    else:
                        print ('There is nothing to interact with here.')

                    cursor.off()


            #SHIFT action form changes here
            if not cursor.alive():
                if ev.type == pygame.KEYDOWN and ev.key == pygame.K_1 and player.essence >= 0:
                    print ('You [shift] into the form of a [spirit].')
                    player.index = 0
                    player.shift()
                    player.isactive = True
                if ev.type == pygame.KEYDOWN and ev.key == pygame.K_2 and player.essence >= 1:
                    print ('You [shift] into the form of a [stag].')
                    player.index = 1
                    player.shift()
                    player.isactive = True
                if ev.type == pygame.KEYDOWN and ev.key == pygame.K_3 and player. essence >= 2:
                    print ('You [shift] into the form of a [wolf].')
                    player.index = 2
                    player.shift()
                    player.isactive = True


        #If player has control of avatar NORMAL ACTIONS HERE
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
                    #Forces player back to oldCoords if player collides with creature.
                    #Use this code to set border boundaries on the map...!
                    for creature in creature_group:
                        if pygame.sprite.collide_rect(player, creature):
                            player.coords = (column, row)
                            player.update()
                    if board_space(player) == False:
                        player.coords = (column, row)
                        player.update()

                    #Debug Coordinates Printed to Console              
                    print 'Player moved to:', player_newCoords
                    print 'Player is on board:', board_space(player)

                    #Spawns and sets "Cursor Mode"
                if ev.type == pygame.KEYDOWN and ev.key in cursor_keys:
                    print ('Target what you wish to interact with, then press the appropriate interaction key.')
                    #cursor function to draw cursor trigger
                    cursor.on()

                if ev.type == pygame.KEYDOWN and ev.key == pygame.K_d:
                    #maybe show display with cursor to select icons, if display is up overwrite controls like cursor mode?
                    player.isactive = False
                    player.shift()



        #Updates sprite positions on grid.  Main loop, otherwise sprites spawn at (0, 0) and snap later.
        player.update()
        cursor.update()

        for creature in creature_group:
            creature.update()



    #Graphics

    screen.blit(background, (0,0))
    draw_sprite(testboard)
    background.blit(ui_surface, ui_surface_pos)
    game_sprites_group.draw(background)


    ui_surface.blit(title_text, title_pos)
    ui_surface.blit(test_message, console_pos)

    if cursor in game_sprites_group:
        cursor.blink()

    #draw playmap and HUD
    #display_HUD (TILESWIDTH + 5, 5)

    #UI DRAWS, LINK TO ONLY DRAW/SHOW ON CERTAIN INPUTS
    #UI DEBUG
    #UI_group.update()
    #UI_group.draw(screen)

    pygame.display.flip()
    pygame.time.wait(30)

pygame.quit()

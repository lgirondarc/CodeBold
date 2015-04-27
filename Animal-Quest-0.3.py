#SWE100 - Intro to Python
#L G
#Final Assignment: Pygame "ANIMAL QUEST" Alpha 0.3

#NOTES:
# Player transformations.  HUD Interactivity/drawing/printing to HUD space.
# Map design and coding.  How to organize 'level designs'?
#!!!! HUD functionality
# Anything listed/printed with brackets [] can be re-coded as string formatting to better address a modular approach.
# Finish making sprites so I can import and start testing functionality.
# Find way to call object that a function targets, so it can call its own object? IE interact(self, variable): variable.interact
# Apparently I am using super.() completely wrong.  Find a way to address this.

import pygame

pygame.init()

#from pygame_utilities import draw_text, sign | Use for printing console to screen?

#Statistics for window dimentions and tile definitions.
pygame.display.set_caption('Animal Quest ALPHA 0.3')
window_width = 800
window_height = 600
tile_size = 32
tile_rows = 25
tile_columns = 18
ui_height = 200

screen = pygame.display.set_mode ([window_width, window_height + ui_height])
board_width = tile_size * tile_rows
board_height = tile_size * tile_columns

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
    screen.blit(sprite.image, sprite.rect)

def is_adjacent (self, other):
    x = (self.coords[0] - other.coords[0])
    y = (self.coords[1] - other.coords[1])
    if -1 <= x <= 1 and -1 <= y <= 1:
        self.adjacent = True
    else:
        self.adjacent = False
    
  
class Player(pygame.sprite.Sprite):
    adjacent = []
    essence = 0
    coords = (0, 0)
    def __init__(self, x, y):
        super(Player, self).__init__()
        self.images = []
        #Insert animal forms in here
        self.images.append(load_image('spirit.png'))
        self.images.append(load_image('spiritstag.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect (0, 0, 32, 32)
        self.mask = pygame.mask.from_surface(self.image)
        self.coords = (x, y)
    
        #Player control flag
        self.isactive = True

    #"Move" code, used to update sprites on the grid.  Should this be a Global variable???
    def update(self):
            self.rect.centerx = self.coords[0] * tile_size + self.rect.width/2
            self.rect.centery = self.coords[1] * tile_size + self.rect.height/2

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

class Cursor (pygame.sprite.Sprite): #ADD DRAW CONDITIONS WHEN PLAYER PRESSES KEY, ALSO DISAPPEARS
    coords = (player.coords)
    def __init__(self, x, y):
        super(Cursor, self).__init__()
        self.images = []
        self.images.append(load_image('cursor1.png'))
        self.images.append(load_image('cursor2.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect (0, 0, 32, 32)

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
        self.rect.centerx = self.coords[0] * tile_size + self.rect.width/2
        self.rect.centery = self.coords[1] * tile_size + self.rect.height/2

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
        self.images.append(load_image('npcstag.png'))
        self.images.append(load_image('npcstagdead.png'))
        #Add other animal images here! Animal bones for dead animal, or animal sitting/laying?

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect (0, 0, 32, 32)
        self.coords = (x, y)
        print ('Base class method was called.')
        
    def update(self):
        self.image = self.images[self.index]
        self.rect.centerx = self.coords[0] * tile_size + self.rect.width/2
        self.rect.centery = self.coords[1] * tile_size + self.rect.height/2

    def look(self):
        if self.index <= 1:
            print ('You [look] at [a lone stag].')
            if self.greeting == 1:
                print ('[A lone stag] appears to be mortally injured.  Its wounds are too severe to mend, but perhaps you can still grant some final solace.')
            if self.greeting == 0:
                print ('The lifeless body of [a lone stag] lays almost peacefully here.  There is nothing more you can do for it.')


    def interact(self):
        
        is_adjacent(player, animal)
        print self.adjacent

        if self.adjacent == True:
        
            if self.greeting == 1:
                print ('Bleeeergh I am dead!')
                self.greeting = 0
                player.essence = 1
                self.index = 1
                self.image = pygame.transform.rotate(self.image, 180)
                self.update()
                print ('''[A lone stag] has entreated its essence as its dying wish.\nYou can now [shift] into a [stag]!''')

            elif self.greeting == 0:
                print ('This poor creature has passed on to a better place.  There is nothing more you can do.')

        elif self.adjacent == False:
            print ('You are not close enough to interact with this creature.')

class Stag(Animal):
    def __init__(self, x, y):
        super(Animal, self).__init__()
        self.images = []
        self.images.append(load_image('npcstag.png'))
        self.images.append(load_image('npcstagdead.png'))
        #Add other animal images here! Animal bones for dead animal, or animal sitting/laying?

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect (0, 0, 32, 32)
        self.coords = (x, y)
        print ('Derived class method was called.')

    def look(self):
        print ('You [look] at [a lone stag].')
        if self.greeting == 1:
            print ('[A lone stag] appears to be mortally injured.  Its wounds are too severe to mend, but perhaps you can still grant some final solace.')
        if self.greeting == 0:
            print ('The lifeless body of [a lone stag] lays almost peacefully here.  There is nothing more you can do for it.')


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
                print ('''[A lone stag] has entreated its essence as its dying wish.\nYou can now [shift] into a [stag]!''')

            elif self.greeting == 0:
                print ('This poor creature has passed on to a better place.')

        elif self.adjacent == False:
            print ('You are not close enough to interact with this creature.')
    

creature = Stag(12, 8)


#Movement library
arrow_keys = {pygame.K_LEFT:    (-1,  0),
              pygame.K_RIGHT:   (+1,  0),
              pygame.K_UP:      ( 0, -1),
              pygame.K_DOWN:    ( 0, +1)
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



#Runtime loop.
runtime = True
while runtime:
    
    for ev in pygame.event.get ():      
        #Quits on window close or Esc keypress.
        if (ev.type == pygame.QUIT or
            ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE):
                runtime = False

        #When when player is not in control of character...
        if player.isactive == False:
            #When cursor is present
            if cursor.alive():
                if ev.type == pygame.KEYDOWN and ev.key in arrow_keys:
                    (column, row) = cursor.coords
                    (dx, dy) = arrow_keys[ev.key]
                    cursor_newCoords = (column + dx, row + dy)
                    #Moves player to new Coordinates
                    cursor.coords = cursor_newCoords
                    #Debug Coordinates Printed to Console
                    print 'Cursor moved to:', cursor.coords
                if ev.type == pygame.KEYDOWN and ev.key == pygame.K_a:
                    #Should I load in ALL "looks" here?  Seems like the best thing would be to have interacts stored in classes/different objects...
                    #Ideally all "[ACTIONS]" and [OBJECTS] can be handled by scripting.
                    if pygame.sprite.collide_rect(cursor, player):
                        player.look()
                    elif pygame.sprite.collide_rect(cursor, creature):
                        creature.look() 
                    else:
                        print ('There is nothing to look at here.')
                    cursor.off()

                if ev.type == pygame.KEYDOWN and ev.key == pygame.K_s:
                    #NEEDS TO DETECT PROXIMITY TO PLAYER AND REFUSE INTERACT IF PLAYER IS TOO FAR AWAY.
                    if pygame.sprite.collide_rect(cursor, creature):
                        creature.interact()
                                        
                    else:
                        print ('There is nothing to interact with here.')

                    cursor.off()

                    
            #SHIFT action form changes here
            if cursor not in game_sprites_group:
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
            

        #If player has control of avatar NORMAL ACTIONS HERE
        elif player.isactive:
            
            if ev.type == pygame.KEYDOWN:
                if ev.key in arrow_keys:           
                    (column, row) = player.coords
                    (dx, dy) = arrow_keys[ev.key]
                    player_newCoords = (column + dx, row + dy)
                    #Moves player to new Coordinates
                    player.coords = player_newCoords
                    player.update()
                    #Forces player back to oldCoords if player collides with creature.
                    #Use this code to set border boundaries on the map...!
                    if pygame.sprite.collide_rect(player, creature):
                        player.coords = (column, row)
                        player.update()
                    
                    #Debug Coordinates Printed to Console              
                    print 'Player moved to:', player_newCoords

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
        creature.update()
        

           
#Graphics
    screen.fill ([0, 0, 0])

    draw_sprite(testboard)
    draw_sprite(testui)
    game_sprites_group.draw(screen)

    if cursor in game_sprites_group:
        cursor.blink()    
    
    #draw playmap and HUD
    #display_HUD (TILESWIDTH + 5, 5)

    #UI DRAWS, LINK TO ONLY DRAW/SHOW ON CERTAIN INPUTS
    #UI DEBUG
    #UI_group.update()
    #UI_group.draw(screen)

    pygame.display.flip ()
    pygame.time.wait (30)

pygame.quit ()


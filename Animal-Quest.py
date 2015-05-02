# SWE100 - Intro to Python
# L G
# Final Assignment: Pygame "ANIMAL QUEST"

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

title_font = pygame.font.SysFont("Lucida Console", 17, False, False)
console_font = pygame.font.SysFont("Lucida Console", 14, False, False)

#from pygame_utilities import draw_text, sign

version = 0.4
#Statistics for window dimensions and tile definitions.
pygame.display.set_caption('Animal Quest v %s'%version)
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
    form_id = ('spirit')
    ability1 = ('Illuminate')
    trait = ('Hover')

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
        self.call_form()

    #"Move" code, used to update sprites on the grid.  Should this be a Global variable???
    def update(self):
        self.rect.centerx = self.coords[0] * tile_size + self.rect.width / 2
        self.rect.centery = self.coords[1] * tile_size + self.rect.height / 2

    def call_form(self):
        if self.index == 0:
            self.form_id = ('spirit')
        elif self.index == 1:
            self.form_id = ('stag')
        elif self.index == 2:
            self.form_id = ('wolf')
        elif self.index == 3:
            self.form_id = ('rat')

        if self.form_id == ('spirit'):
            self.ability1 = ('Illuminate')
            self.trait = ('Hover')
        if self.form_id == ('stag'):
            self.ability1 = ('Carry')
            self.trait = ('Strength')
        if self.form_id == ('wolf'):
            self.ability1 = ('Dig')
            self.trait = ('Track & Smell')
        if self.form_id == ('rat'):
            self.ability1 = ('Sneak')
            self.trait = ('Small')
           
            
    def shift(self):
        #Will have to manually input line breaks.  string format does not like \n and prints an invalid character in its place.
        if player.essence <= 0:
            console_scroll('You have no further blessings to manifest and [SHIFT] into at this time.')
            player.isactive = True
        elif player.essence <= 1:
            console_scroll('[SHIFT] into which form?\n1: Spirit\n2: Stag')
        elif player.essence <= 2:
            console_scroll('[SHIFT] into which form?\n1: Spirit\n2: Stag\n3: Wolf')
        elif player.essence >= 3:
            console_scroll('[SHIFT] into which form?\n1: Spirit\n2: Stag\n3: Wolf\n4: Rat')


        print ('FormID:', player.form_id)
        self.image = self.images[self.index]

    #Code Look commands relating to player here.  Probably a way to store commands globally instead of per class.
    def look(self):
        if self.form_id == ('spirit'):
            console_scroll ('You are an Aspect of Nature. You glow with a brilliant radiance.')
            console_scroll ('As a {0}, you can {1} your surroundings and reveal hidden objects or creatures.'.format(self.form_id, self.ability1))
            console_scroll ('You can also {0} over most terrain.'.format(self.trait))
        
        else:
            console_scroll ('You have invoked the blessing of the {}.'.format(self.form_id))

        if self.form_id == ('stag'):
            console_scroll ('The {0} can use its {1} to push objects, and can also {2} other animals.'.format(self.form_id, self.trait, self.ability1))

        if self.form_id == ('wolf'):
            console_scroll ('The {0} can {1} up objects with its paws.'.format(self.form_id, self.ability1))
            console_scroll ('It can also {0} other creatures and hidden treasure.'.format(self.trait))

        if self.form_id == ('rat'):
            console_scroll ('The {0} can use its {1} size to squeeze into tight spaces.  It can also {2} by other animals.'.format(self.form_id, self.trait, self.ability1))

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


cursor = Cursor(player.coords[0], player.coords[1])


class Animal(pygame.sprite.Sprite):
    form_id = ('animal')
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
        console_scroll('There is an {} here'.format(self.form_id))


    def interact(self):

        is_adjacent(self, player)
        print self.adjacent

        if self.adjacent == True:
            console_scroll('The {} regards you with a benign curiosity.'.format(self.form_id))


        elif self.adjacent == False:
            console_scroll('You are not close enough to interact with the {}.'.format(self.form_id))


class Stag(Animal):
    form_id = ('stag')
    def __init__(self, x, y):
        Animal.__init__(self, x, y)
        self.images = []
        self.images.append(load_image('npcstagsick.png'))
        self.images.append(load_image('npcstag.png'))
        #Add other animal images here! Animal bones for dead animal, or animal sitting/laying?
        self.index = 0

        self.image = self.images[self.index]
        self.rect = pygame.Rect(0, 0, 32, 32)
        self.coords = (x, y)
        print ('Derived class method was called: Stag.')

    def look(self):
        console_scroll ('You look at {0}.'.format(self.form_id))
        if self.greeting == 1:
            console_scroll(
                'The {0} trembles in fear of the darkness around it.  Perhaps you can aid the poor {0}?'.format(self.form_id))
        if self.greeting == 0:
            console_scroll(
                'The {0} seems to be at ease now.  You have helped cure the {0} of its worry!'.format(self.form_id))


    def interact(self):

        is_adjacent(self, player)
        print self.adjacent

        if self.adjacent == True:

            if self.index == 0 and self.greeting == 1:
                console_scroll('The {0} seems to be at ease now, comforted by the light of your [Illuminate].'.format(self.form_id))
                self.greeting = 0
                player.essence = 1
                self.index = 1
                self.image = self.images[self.index]
                console_scroll('In response to your aid, the {0} has entreated its blessing to you.'.format(self.form_id))
                console_scroll('You can now [shift] into a [stag]!'.format(self.form_id))

            elif self.greeting == 0:
                console_scroll('You have already helped the {0}.  The {0} gently bows its head in gratitude.'.format(self.form_id))

        elif self.adjacent == False:
            console_scroll('You are not close enough to interact with the {}.'.format(self.form_id))


class Wolf(Animal):
    form_id = ('wolf')
    def __init__(self, x, y):
        Animal.__init__(self, x, y)
        self.images = []
        self.images.append(load_image('npcwolfsick.png'))
        self.images.append(load_image('npcwolf.png'))
        self.image = self.images[self.index]

        print ('Derived class method was called: Wolf.')

    def look(self):
        #Wolf cannot move well?  Or code in AI so it paces along the cliff edge, then goes across when the path is created?
        #Then there is no reason for stag to have carry...  Unless it carries an object, I dunno.
        console_scroll('You [LOOK] at the {0}. The {0} appears to have wounded its paw and cannot easily move.'.format(self.form_id))
        console_scroll('The {0} looks longingly at the rising moon.  If only it could get a better view.'.format(self.form_id))

    def interact(self):
        is_adjacent(self, player)
        console_scroll('Player is adjacent: {}'.format(self.adjacent))
        
        if self.adjacent == True:
            console_scroll('The {0} bows its head in thanks to you, now the {0} can enjoy the view'.format(self.form_id))
            player.essence = 2
            self.index = 1
            self.image = self.images[self.index]
            
            console_scroll('As a token of gratitude, the {0} has entreated its blessing to you.'.format(self.form_id))
            console_scroll('You can now [SHIFT] into a {}!'.format(self.form_id))

        elif self.adjacent == False:
            console_scroll('You are not close enough to interact with the {}.'.format(self.form_id))


creature = [Wolf(8, 12), Stag(12, 8)]
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

#array for console line buffer
console_lines = []

def console_scroll(string):
    max_lines = 5
    console_lines.append(string)

    while len (console_lines) > max_lines:
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
        '''- - - - - - - - - - - - - - - Animal Quest v %s - - - - - - - - - - - - - - -'''%version, 0,(255, 255, 255))
    title_pos = title_text.get_rect()
    title_pos.centerx = ui_surface.get_rect().centerx
    title_pos.centery = ui_surface.get_rect().bottom - 178

    #These are the global actions, they do not change based on player form.
    ui_actions01 = console_font.render(
        '''[a] Look  [s] Interact  [d] Shift     |     ''' +'[z] {0}  [Trait] {1}'.format(
            player.ability1, player.trait), 0, (255, 255, 255))
    ui_actions01_pos = ui_actions01.get_rect()
    ui_actions01_pos.x = +85
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
                    print ('Cursor moved to: {}'.format(cursor.coords))
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
                            console_scroll('There is nothing to look at here.')
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
                        console_scroll('There is nothing to interact with here.')

                    cursor.off()


            #SHIFT action form changes here
            if not cursor.alive():
                if ev.type == pygame.KEYDOWN and ev.key == pygame.K_1 and player.essence >= 0:
                    player.index = 0
                    player.call_form()
                    player.shift()
                    console_scroll('You [SHIFT] into the form of a {}.'.format(player.form_id))
                    player.isactive = True
                    
                if ev.type == pygame.KEYDOWN and ev.key == pygame.K_2 and player.essence >= 1:
                    player.index = 1
                    player.call_form()
                    player.shift()
                    console_scroll('You [SHIFT] into the form of a {}.'.format(player.form_id))
                    player.isactive = True
                    
                if ev.type == pygame.KEYDOWN and ev.key == pygame.K_3 and player.essence >= 2:
                    player.index = 2
                    player.call_form()
                    player.shift()
                    console_scroll('You [SHIFT] into the form of a {}.'.format(player.form_id))
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
                    print('Player moved to: {}'.format(player_newCoords))
                    print('Player is on board: {}'.format(board_space(player)))

                    #Spawns and sets "Cursor Mode"
                if ev.type == pygame.KEYDOWN and ev.key in cursor_keys:
                    if ev.key == pygame.K_a:
                        console_scroll('Look at what?')
                    if ev.key == pygame.K_s:
                        console_scroll('Interact with what?')
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

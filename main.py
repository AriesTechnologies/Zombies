# --- Imports --- #

from background import *
from enemy import *
from player import*
import py_compile
py_compile.compile("main.py")
import pygame
from sprites import *
import sys

# --- Game --- #                                   

pygame.init()
global Game
Game = False
global Score
Score = 0
global paused
paused = False

xsmallfont = pygame.font.SysFont("8-Bit-Madness", 15)
smallfont = pygame.font.SysFont ("8-Bit-Madness", 30)
mediumfont = pygame.font.SysFont ("8-Bit-Madness", 50)
largefont = pygame.font.SysFont ("8-Bit-Madness", 95)
xlargefont = pygame.font.SysFont ("8-Bit-Madness", 105)

black = (0,0,0)
red = (200,0,0)
green = (50,165,0)
dark_green = (50,135,0)
white = (255,255,255)

clock = pygame.time.Clock()
background = Background()
player = Player()
enemy = Enemy()
enemy2 = Enemy()
Display_w = 1280
Display_h = 700
Title = pygame.display.set_caption("Zombies")
gameDisplay = pygame.display.set_mode((Display_w,Display_h), pygame.RESIZABLE)

#Convert pictures to pygame pics
for lists in sprites.All_Sprites:
    for pic in lists:
        pic.convert_alpha()

#Part of Message_To_Screen
def Text_Objects(Text, Color, Size):
    if Size == "xsmall":
        TextSurface = xsmallfont.render (Text, True, Color)
    elif Size == "small":
        TextSurface = smallfont.render (Text, True, Color)
    elif Size == "medium":
        TextSurface = mediumfont.render (Text, True, Color)
    elif Size == "large":
        TextSurface = largefont.render (Text, True, Color)
    elif Size == "xlarge":
        TextSurface = xlargefont.render (Text, True, Color)
    return TextSurface, TextSurface.get_rect()

#Return a message to be printed to the screen
def message_to_screen(msg, Color, x_Pos, x_Displace=0, y_Displace=0, Size="small"):
    TextSurf, TextRect = Text_Objects(msg, Color, Size)
    if x_Pos == 1:
        TextRect.left = (int(Display_w/6)+x_Displace, int(Display_h/2)+y_Displace)
    if x_Pos == 1.5:
        TextRect = (int(Display_w/3)+x_Displace, int(Display_h/2)+y_Displace)
    if x_Pos == 2:
        TextRect.center = (int(Display_w/2)+x_Displace, int(Display_h/2)+y_Displace)
    if x_Pos == 3:
        TextRect.right = (int(Display_w/1.5)+x_Displace, int(Display_h/2)+y_Displace)
    gameDisplay.blit(TextSurf, TextRect)

#Part of Button
def text_to_button(msg, Color, Button_X, Button_Y, Button_w, Button_h, Size="small"):
    textSurf, textRect  = Text_Objects(msg, Color, Size)
    textRect.center = ((Button_X+(Button_w/2)), Button_Y+(Button_h/2))
    gameDisplay.blit(textSurf, textRect)

#Returns a Button to be printed to screen
def Button(text, x, y, w, h, inactive_color, active_color, Action):
    Cursor = pygame.mouse.get_pos()
    if x + w > Cursor[0] > x and y + h > Cursor[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,w,h))
    else:
         pygame.draw.rect(gameDisplay, inactive_color, (x,y,w,h))
    text_to_button(text,white,x,y,w,h)

#Options Screen
def Options():
    Options = True
    while Options:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_BACKSPACE:
                    Options = False
                    pass
            
        gameDisplay.blit(sprites.Background_List[1], (0,0))
        message_to_screen("Instructions:", green, 2, 0, -250, Size="xlarge")
        message_to_screen("Right Arrow and Left Arrow Keys: Movement", white, 2, 0, -100, Size="medium")
        message_to_screen("Up Arrow Key: Jump", white, 2, 0, -25, Size="medium")
        message_to_screen("Down Arrow Key: Change Weapon", white, 2, 0, 50, Size="medium")
        message_to_screen("Shift Keys: Aim Weapon", white, 2, 0, 125, Size="medium")
        message_to_screen("Spacebar: Shoot Weapon", white, 2, 0, 200, Size="medium")
        message_to_screen("©2017 AtlasCorporations", white, 2, 0, 305, Size="small")
        pygame.display.flip()

#Updates Screen
def Updates():
    Updates = True
    while Updates:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_BACKSPACE:
                    Updates = False
                    pass
            
        gameDisplay.blit(sprites.Background_List[1], (0,0))
        message_to_screen("Updates:", green, 2, 0, -250, Size="xlarge")
        message_to_screen("Version 1.0.0 Alpha: Fully completed Zombies, bug fixes with weapons", white, 2, 0, -100, Size="small")
        message_to_screen("Version 1.1.0 Alpha: Added in multiple zombies, bug fixes", white, 2, 0, -25, Size="small")
        message_to_screen("Version 1.2.0 Alpha: Added in randomized player type, bug fixes with multiple zombie movements", white, 2, 0, 50, Size="small")
        message_to_screen("Version 1.3.0 Alpha: Added in boundaries on the edges of the screen", white, 2, 0, 125, Size="small")
        message_to_screen("Version 1.3.1 Alpha: Bug fixes with boundaries", white, 2, 0, 200, Size="small")
        message_to_screen("©2017 AtlasCorporations", white, 2, 0, 305, Size="small")
        pygame.display.flip()

#Title Screen
def __title__():
    global Game
    while Game == False:
        Cursor = pygame.mouse.get_pos()
        Click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if 536+208 > Cursor[0] > 536 and 371+58 > Cursor[1] > 371:
                if Click[0] == 1:
                    Game = True
                    player.moving = True
                    enemy.moving = True
                    enemy2.moving = True
            elif 540+200 > Cursor[0] > 540 and 440+50 > Cursor[1] > 440:
                if Click[0] == 1:
                    Options()
            elif 540+200 > Cursor[0] > 540 and 505+50 > Cursor[1] > 505:
                if Click[0] == 1:
                    Updates()
            
        gameDisplay.blit(sprites.Background_List[1], (0,0))
        message_to_screen("Zombies", green, 2, 0, -250, Size="xlarge")
        pygame.draw.rect(gameDisplay, white, (535,370,210,60))
        pygame.draw.rect(gameDisplay, white, (535,435,210,60))
        pygame.draw.rect(gameDisplay, white, (535,500,210,60))
        Button("Play", 536, 371, 208, 58, black, red, Action="Play")
        Button("Options", 536, 436, 208, 58, black, red, Action="Options")
        Button("Updates", 536, 501, 208, 58, black, red, Action="Updates")
        message_to_screen("©2017 AtlasCorporations", white, 2, 0, 305, Size="small")
        pygame.display.flip()
        clock.tick(20)

#Pause Screen
def Pause():
    global paused
    while paused == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
                    paused = False

            gameDisplay.fill(black)
            message_to_screen("Paused", red, 2, 0, 0, Size="large")
            message_to_screen("Score: "+str(score), white, 2, 0, -75, Size="medium")
            pygame.display.flip()
            clock.tick(10)

#Main Game
def __main__():
    global Score
    global Game
    global paused
    Title = pygame.display.set_caption("Zombies FPS: "+str(clock.get_fps()))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.moving_up = True
            if event.key == pygame.K_RIGHT:
                if player.X < 1280:
                    player.direction = "Right"
                    player.moving_right = True
            if event.key == pygame.K_LEFT:
                if player.X > 0:
                    player.direction = "Left"
                    player.moving_left = True
            if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
                player.aiming = True
            if event.key == pygame.K_SPACE:
                player.shooting = True
            if event.key == pygame.K_DOWN:
                player.change_weapon()
            if event.key == pygame.K_ESCAPE:
                paused = True
                Pause()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.moving_right = False
            if event.key == pygame.K_LEFT:
                player.moving_left = False
            if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
                player.aiming = False
            if event.key == pygame.K_SPACE:
                player.shooting = False

##    Runs Player movement, animation, etc.
    player.__main__()
    enemy.__main__(player.X)
    enemy2.__main__(player.X)

    #Checks for Zombie touching Player
    if player.X + 100 >= enemy.X >= player.X and not enemy.dead:
        player.damaged = True
        enemy.moving = False
        enemy.attack = True
        if player.damaged:
            player.damaged_counter += 1
            if player.damaged_counter >= 8:
                player.health -= enemy.damage
                player.damaged = False
                player.damaged_counter = 0
                if player.health <= 0:
                    enemy.moving = False
                    player.moving = False
                    Game = False
    else:
        player.damaged = False
        enemy.moving = True
        enemy.attack = False
        if player.health < player.max_health:
            player.regen()

    if player.X + 100 >= enemy2.X >= player.X and not enemy2.dead:
        player.damaged = True
        enemy2.moving = False
        enemy2.attack = True
        if player.damaged:
            player.damaged_counter += 1
            if player.damaged_counter >= 8:
                player.health -= enemy.damage
                player.damaged = False
                player.damaged_counter = 0
                if player.health <= 0:
                    enemy2.moving = False
                    player.moving = False
                    Game = False
    else:
        player.damaged = False
        enemy2.moving = True
        enemy2.attack = False
        if player.health < player.max_health:
            player.regen()

    #Checks for bullet touching Enemy
    if enemy.X < player.bullet_X < enemy.X+116 and enemy.Y < player.bullet_Y < enemy.Y+140 and not enemy.dead and not player.bullet_dead:
        if player.shot_counter >= 8:
            enemy.health -= player.weapon_damage
            player.bullet_counter = 0
            player.shot_counter = 0
            del player.bullets_list[:]
            player.bullet_dead = True
            if enemy.health <= 0:
                enemy.dead = True
                enemy.moving = False
                Score += 50

    if enemy2.X < player.bullet_X < enemy2.X+116 and enemy2.Y < player.bullet_Y < enemy2.Y+140 and not enemy2.dead and not player.bullet_dead:
        if player.shot_counter >= 8:
            enemy2.health -= player.weapon_damage
            player.bullet_counter = 0
            player.shot_counter = 0
            del player.bullets_list[:]
            player.bullet_dead = True
            if enemy2.health <= 0:
                enemy2.dead = True
                enemy2.moving = False
                Score += 50

    #Redisplay Background
    gameDisplay.blit(background.Bg[0], (background.X, background.Y))

    #Redisplay Player
    if player.direction == "Right":
        gameDisplay.blit(player.current[player.animation_int],(player.X, player.Y))
    elif player.direction == "Left":
        gameDisplay.blit(pygame.transform.flip(player.current[player.animation_int], True, False), (player.X, player.Y))

    #Redisplay Bullet
    if player.bullet_counter == 1:
        if player.bullet_direction == "Right":
            gameDisplay.blit(player.bullet[0], (player.bullet_X+110, player.bullet_Y))
        elif player.bullet_direction == "Left":
            gameDisplay.blit(pygame.transform.flip(player.bullet[0], True, False), (player.bullet_X, player.bullet_Y))

    #Redisplay Zombie
    if not enemy.dead:
        if enemy.direction == "Right":
            gameDisplay.blit(enemy.current[enemy.animation_int],(enemy.X, enemy.Y))
        elif enemy.direction == "Left":
            gameDisplay.blit(pygame.transform.flip(enemy.current[enemy.animation_int], True, False), (enemy.X, enemy.Y))

    if not enemy2.dead:
        if enemy2.direction == "Right":
            gameDisplay.blit(enemy2.current[enemy2.animation_int],(enemy2.X, enemy2.Y))
        elif enemy2.direction == "Left":
            gameDisplay.blit(pygame.transform.flip(enemy2.current[enemy2.animation_int], True, False), (enemy2.X, enemy2.Y))
            
    message_to_screen("Score: "+str(Score), white, 2, -575, -325, Size="small")

    pygame.display.flip()
    clock.tick(30)

#After Player Dead
def Death_Screen():
    player.current = sprites.Enemy_Walking_List
    gameDisplay.fill(black)
    gameDisplay.blit(player.current[0], (Display_w/2-58, player.ground))
    message_to_screen("Game Over!", red, 2, 0, 0, Size="xlarge")
    message_to_screen("Score: "+str(Score), white, 2, 0, 75, Size="medium") #Add score later
    pygame.display.flip()

    while Game == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        clock.tick(10)

while Game == False:
    __title__()
    
while Game == True:
    __main__()

Death_Screen()

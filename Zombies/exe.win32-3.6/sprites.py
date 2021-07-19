# --- Imports --- #

import pygame
import random

# --- All Sprites --- #

Player_Type_Int = random.randrange(0,4)
Map_Type = 0

if Player_Type_Int == 0:
    Player_Graphic = pygame.image.load("Images/Nerd.png")
    Player_Running = pygame.image.load("Images/Nerd_Running.png")
#    Player_Running_1 = pygame.image.load("Images/Nerd_Running1.png")
    Player_Shooting = pygame.image.load("Images/Nerd_Shooting.png")
    Player_Shooting_AR = pygame.image.load("Images/Nerd_Shooting_Assault_Rifle.png")
    Player_Shooting_AR_Running = pygame.image.load("Images/Nerd_Shooting_Assault_Rifle_Running.png")
#    Player_Shooting_AR_Running_1 = pygame.image.load("Images/Nerd_Shooting_Assault_Rifle_Running1.png")
    Player_Shooting_SMG = pygame.image.load("Images/Nerd_Shooting_Submachine_Gun.png")
    Player_Shooting_SMG_Running = pygame.image.load("Images/Nerd_Shooting_Submachine_Gun_Running.png")
#    Player_Shooting_SMG_Running_1 = pygame.image.load("Images/Nerd_Shooting_Submachine_Gun_Running1.png")
    Player_Shooting_MG = pygame.image.load("Images/Nerd_Shooting_Machine_Gun.png")
    Player_Shooting_MG_Running = pygame.image.load("Images/Nerd_Shooting_Machine_Gun_Running.png")
#    Player_Shooting_MG_Running_1 = pygame.image.load("Images/Nerd_Shooting_Machine_Gun_Running1.png")
    Player_Shooting_SR = pygame.image.load("Images/Nerd_Shooting_Sniper.png")
    Player_Shooting_SR_Running = pygame.image.load("Images/Nerd_Shooting_Sniper_Running.png")
#    Player_Shooting_SR_Running_1 = pygame.image.load("Images/Nerd_Shooting_Sniper_Running1.png")
    Player_Shooting_SG = pygame.image.load("Images/Nerd_Shooting_Shotgun.png")
    Player_Shooting_SG_Running = pygame.image.load("Images/Nerd_Shooting_Shotgun_Running.png")
#    Player_Shooting_SG_Running_1 = pygame.image.load("Images/Nerd_Shooting_Shotgun_Running1.png")
    Player_Shooting_HG = pygame.image.load("Images/Nerd_Shooting_Handgun.png")
    Player_Shooting_HG_Running = pygame.image.load("Images/Nerd_Shooting_Handgun_Running.png")
#    Player_Shooting_HG_Running_1 = pygame.image.load("Images/Nerd_Shooting_Handgun_Running1.png")
    Player_Walking_List = [Player_Graphic, Player_Running]
    Player_Shooting_Melee_List = [Player_Shooting]
    Player_Shooting_HG_List = [Player_Shooting_HG, Player_Shooting_HG_Running]
    Player_Shooting_SG_List = [Player_Shooting_SG, Player_Shooting_SG_Running]
    Player_Shooting_SR_List = [Player_Shooting_SR, Player_Shooting_SR_Running]
    Player_Shooting_MG_List = [Player_Shooting_MG, Player_Shooting_MG_Running]
    Player_Shooting_SMG_List = [Player_Shooting_SMG, Player_Shooting_SMG_Running]
    Player_Shooting_AR_List = [Player_Shooting_AR, Player_Shooting_AR_Running]
    
elif Player_Type_Int == 1:
    Player_Graphic = pygame.image.load("Images/Athlete.png")
    Player_Running = pygame.image.load("Images/Athlete_Running.png")
    Player_Shooting = pygame.image.load("Images/Athlete_Shooting.png")
    Player_Shooting_HG = pygame.image.load("Images/Athlete_Shooting_Handgun.png")
    Player_Shooting_HG_Running = pygame.image.load("Images/Athlete_Shooting_Handgun_Running.png")
    Player_Shooting_SG = pygame.image.load("Images/Athlete_Shooting_Shotgun.png")
    Player_Shooting_SG_Running = pygame.image.load("Images/Athlete_Shooting_Shotgun_Running.png")
    Player_Shooting_SR = pygame.image.load("Images/Athlete_Shooting_Sniper.png")
    Player_Shooting_SR_Running = pygame.image.load("Images/Athlete_Shooting_Sniper_Running.png")
    Player_Shooting_MG = pygame.image.load("Images/Athlete_Shooting_Machine_Gun.png")
    Player_Shooting_MG_Running = pygame.image.load("Images/Athlete_Shooting_Machine_Gun_Running.png")
    Player_Shooting_SMG = pygame.image.load("Images/Athlete_Shooting_Submachine_Gun.png")
    Player_Shooting_SMG_Running = pygame.image.load("Images/Athlete_Shooting_Submachine_Gun_Running.png")
    Player_Shooting_AR = pygame.image.load("Images/Athlete_Shooting_Assault_Rifle.png")
    Player_Shooting_AR_Running = pygame.image.load("Images/Athlete_Shooting_Assault_Rifle_Running.png")
    Player_Walking_List = [Player_Graphic, Player_Running]
    Player_Shooting_Melee_List = [Player_Shooting]
    Player_Shooting_HG_List = [Player_Shooting_HG, Player_Shooting_HG_Running]
    Player_Shooting_SG_List = [Player_Shooting_SG, Player_Shooting_SG_Running]
    Player_Shooting_SR_List = [Player_Shooting_SR, Player_Shooting_SR_Running]
    Player_Shooting_MG_List = [Player_Shooting_MG, Player_Shooting_MG_Running]
    Player_Shooting_SMG_List = [Player_Shooting_SMG, Player_Shooting_SMG_Running]
    Player_Shooting_AR_List = [Player_Shooting_AR, Player_Shooting_AR_Running]
    
elif Player_Type_Int == 2:
    Player_Graphic = pygame.image.load("Images/ValleyGirl.png")
    Player_Running = pygame.image.load("Images/ValleyGirl_Running.png")
    Player_Shooting = pygame.image.load("Images/ValleyGirl_Shooting.png")
    Player_Shooting_HG = pygame.image.load("Images/ValleyGirl_Shooting_Handgun.png")
    Player_Shooting_HG_Running = pygame.image.load("Images/ValleyGirl_Shooting_Handgun_Running.png")
    Player_Shooting_SG = pygame.image.load("Images/ValleyGirl_Shooting_Shotgun.png")
    Player_Shooting_SG_Running = pygame.image.load("Images/ValleyGirl_Shooting_Shotgun_Running.png")
    Player_Shooting_SR = pygame.image.load("Images/ValleyGirl_Shooting_Sniper.png")
    Player_Shooting_SR_Running = pygame.image.load("Images/ValleyGirl_Shooting_Sniper_Running.png")
    Player_Shooting_MG = pygame.image.load("Images/ValleyGirl_Shooting_Machine_Gun.png")
    Player_Shooting_MG_Running = pygame.image.load("Images/ValleyGirl_Shooting_Machine_Gun_Running.png")
    Player_Shooting_SMG = pygame.image.load("Images/ValleyGirl_Shooting_Submachine_Gun.png")
    Player_Shooting_SMG_Running = pygame.image.load("Images/ValleyGirl_Shooting_Submachine_Gun_Running.png")
    Player_Shooting_AR = pygame.image.load("Images/ValleyGirl_Shooting_Assault_Rifle.png")
    Player_Shooting_AR_Running = pygame.image.load("Images/ValleyGirl_Shooting_Assault_Rifle_Running.png")
    Player_Walking_List = [Player_Graphic, Player_Running]
    Player_Shooting_Melee_List = [Player_Shooting]
    Player_Shooting_HG_List = [Player_Shooting_HG, Player_Shooting_HG_Running]
    Player_Shooting_SG_List = [Player_Shooting_SG, Player_Shooting_SG_Running]
    Player_Shooting_SR_List = [Player_Shooting_SR, Player_Shooting_SR_Running]
    Player_Shooting_MG_List = [Player_Shooting_MG, Player_Shooting_MG_Running]
    Player_Shooting_SMG_List = [Player_Shooting_SMG, Player_Shooting_SMG_Running]
    Player_Shooting_AR_List = [Player_Shooting_AR, Player_Shooting_AR_Running]

elif Player_Type_Int == 3:
    Player_Graphic = pygame.image.load("Images/Rapp.png")
    Player_Running = pygame.image.load("Images/Rapp_Running.png")
    Player_Shooting = pygame.image.load("Images/Rapp_Shooting.png")
    Player_Shooting_HG = pygame.image.load("Images/Rapp_Shooting_Handgun.png")
    Player_Shooting_HG_Running = pygame.image.load("Images/Rapp_Shooting_Handgun_Running.png")
    Player_Shooting_SG = pygame.image.load("Images/Rapp_Shooting_Shotgun.png")
    Player_Shooting_SG_Running = pygame.image.load("Images/Rapp_Shooting_Shotgun_Running.png")
    Player_Shooting_SR = pygame.image.load("Images/Rapp_Shooting_Sniper.png")
    Player_Shooting_SR_Running = pygame.image.load("Images/Rapp_Shooting_Sniper_Running.png")
    Player_Shooting_MG = pygame.image.load("Images/Rapp_Shooting_Machine_Gun.png")
    Player_Shooting_MG_Running = pygame.image.load("Images/Rapp_Shooting_Machine_Gun_Running.png")
    Player_Shooting_SMG = pygame.image.load("Images/Rapp_Shooting_Submachine_Gun.png")
    Player_Shooting_SMG_Running = pygame.image.load("Images/Rapp_Shooting_Submachine_Gun_Running.png")
    Player_Shooting_AR = pygame.image.load("Images/Rapp_Shooting_Assault_Rifle.png")
    Player_Shooting_AR_Running = pygame.image.load("Images/Rapp_Shooting_Assault_Rifle_Running.png")
    Player_Walking_List = [Player_Graphic, Player_Running]
    Player_Shooting_Melee_List = [Player_Shooting]
    Player_Shooting_HG_List = [Player_Shooting_HG, Player_Shooting_HG_Running]
    Player_Shooting_SG_List = [Player_Shooting_SG, Player_Shooting_SG_Running]
    Player_Shooting_SR_List = [Player_Shooting_SR, Player_Shooting_SR_Running]
    Player_Shooting_MG_List = [Player_Shooting_MG, Player_Shooting_MG_Running]
    Player_Shooting_SMG_List = [Player_Shooting_SMG, Player_Shooting_SMG_Running]
    Player_Shooting_AR_List = [Player_Shooting_AR, Player_Shooting_AR_Running]
     
Enemy_Graphic = pygame.image.load("Images/Zombie1.png")
Enemy_Running = pygame.image.load("Images/Zombie1_Running.png")
#Enemy_Attacking = pygame.image.load("Images/")
Enemy_Walking_List = [Enemy_Graphic, Enemy_Running]
##Enemy_Attacking_List = [Enemy_Attacking]

Bullet = pygame.image.load("Images/Bullet.png")
Bullet_List = [Bullet]
if Map_Type == 0:
#    Background_Image = pygame.image.load("Images/Map_1.png")
    Background_Image = pygame.image.load("Images/Outside_Mansion.png")
    Background_Image1 = pygame.image.load("Images/Inside_Mansion.png")
Background_List = [Background_Image, Background_Image1]

All_Sprites = [Player_Walking_List, Player_Shooting_Melee_List, Player_Shooting_HG_List, Player_Shooting_SG_List, Player_Shooting_SR_List,
               Player_Shooting_MG_List, Player_Shooting_SMG_List, Player_Shooting_AR_List, Enemy_Walking_List]

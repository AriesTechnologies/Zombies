# --- Imports --- #

import sprites

# --- Player Class --- #

class Player(object):
    
    animation_int = 0
    Animation_Walking_List = sprites.Player_Walking_List
    current = sprites.Player_Shooting_HG_List
    bullet = sprites.Bullet_List
    
    
    X = 640
    counter = 0
    Y = 530
    ground = 530
    direction = "Right"
    speed = 10
    grav_speed = 5
    jump_height = 150
    gravity_speed = 5
    health = 100
    max_health = 100
    weapon = "Handgun"
    weapon_dict = {0:"Handgun", 1:"Shotgun", 2:"Sniper", 3:"Machine Gun", 4:"Submachine Gun", 5:"Assault Rifle"}
    weapon_damage_dict = {"Handgun":35, "Shotgun":90, "Sniper":100, "Machine Gun":55, "Submachine Gun":45, "Assault Rifle":60}
    weapon_damage = 35
    weapon_int = 0
    damaged_counter = 0
    bullets_list = []
    bullet_X = 0
    bullet_Y = 0
    shot_counter = 0
    bullet_counter = 0
    bullet_speed = 30
    bullet_direction = "Right"
    bullet_dead = False

    damaged = False
    dead = False
    moving = False
    aiming = False
    shooting = False
    moving_up = False
    moving_down = False
    moving_right = False
    moving_left = False
    next_0 = True
    next_1 = False
##    next_2 = False

    def movement(self):

        if not self.dead:
            if self.moving_left:
                if self.X > 0:
                    self.X -= self.speed
            if self.moving_right:
                if self.X < 1200:
                    self.X += self.speed

    def animation(self): #Edit to include checks for gun type and walk whilst aiming, etc.
        
        self.counter += 1

        if self.counter == 5:
            if self.moving_right or self.moving_left:
                if self.aiming:
                    if self.weapon == "Handgun":
                        self.current = sprites.Player_Shooting_HG_List
                        if self.next_0:
                            self.animation_int = 0
                            self.next_0 = False
                            self.next_1 = True
                        elif self.next_1:
                            self.animation_int = 1
                            self.next_1 = False
                            self.next_0 = True
##                            self.next_2 = True
##                        elif self.next_2:
##                            self.animation_int = 2
##                            self.next_2 = False
##                            self.next_0 = True
                    elif self.weapon == "Shotgun":
                        self.current = sprites.Player_Shooting_SG_List
                        if self.next_0:
                            self.animation_int = 0
                            self.next_0 = False
                            self.next_1 = True
                        elif self.next_1:
                            self.animation_int = 1
                            self.next_1 = False
                            self.next_0 = True
##                            self.next_2 = True
##                        elif self.next_2:
##                            self.animation_int = 2
##                            self.next_2 = False
##                            self.next_0 = True
                    elif self.weapon == "Sniper":
                        self.current = sprites.Player_Shooting_SR_List
                        if self.next_0:
                            self.animation_int = 0
                            self.next_0 = False
                            self.next_1 = True
                        elif self.next_1:
                            self.animation_int = 1
##                            self.next_2 = True
                            self.next_0 = True
                            self.next_1 = False
##                        elif self.next_2:
##                            self.animation_int = 2
##                            self.next_2 = False
##                            self.next_0 = True
                    elif self.weapon == "Machine Gun":
                        self.current = sprites.Player_Shooting_MG_List
                        if self.next_0:
                            self.animation_int = 0
                            self.next_0 = False
                            self.next_1 = True
                        elif self.next_1:
                            self.animation_int = 1
##                            self.next_2 = True
                            self.next_1 = False
                            self.next_0 = True
##                        elif self.next_2:
##                            self.animation_int = 2
##                            self.next_2 = False
##                            self.next_0 = True
                    elif self.weapon == "Submachine Gun":
                        self.current = sprites.Player_Shooting_SMG_List
                        if self.next_0:
                            self.animation_int = 0
                            self.next_0 = False
                            self.next_1 = True
                        elif self.next_1:
                            self.animation_int = 1
##                            self.next_2 = True
                            self.next_1 = False
                            self.next_0 = True
##                        elif self.next_2:
##                            self.animation_int = 2
##                            self.next_2 = False
##                            self.next_0 = True
                    elif self.weapon == "Assault Rifle":
                        self.current = sprites.Player_Shooting_AR_List
                        if self.next_0:
                            self.animation_int = 0
                            self.next_0 = False
                            self.next_1 = True
                        elif self.next_1:
                            self.animation_int = 1
##                            self.next_2 = True
                            self.next_1 = False
                            self.next_0 = True
##                        elif self.next_2:
##                            self.animation_int = 2
##                            self.next_2 = False
##                            self.next_0 = True
                else:
                    self.current = sprites.Player_Walking_List
                    if self.next_0:
                        self.animation_int = 0
                        self.next_0 = False
                        self.next_1 = True
                    elif self.next_1:
                        self.animation_int = 1
##                        self.next_2 = True
                        self.next_0 = True
                        self.next_1 = False
##                        elif self.next_2:
##                            self.animation_int = 2
##                            self.next_2 = False
##                            self.next_0 = True
            else:
                if not self.aiming:
                    self.current = sprites.Player_Walking_List
                    self.animation_int = 0
                else:
                    if self.weapon == "Handgun":
                        self.current = sprites.Player_Shooting_HG_List
                        self.animation_int = 0
                    if self.weapon == "Shotgun":
                        self.current = sprites.Player_Shooting_SG_List
                        self.animation_int = 0
                    if self.weapon == "Sniper":
                        self.current = sprites.Player_Shooting_SR_List
                        self.animation_int = 0
                    if self.weapon == "Machine Gun":
                        self.current = sprites.Player_Shooting_MG_List
                        self.animation_int = 0
                    if self.weapon == "Submachine Gun":
                        self.current = sprites.Player_Shooting_SMG_List
                        self.animation_int = 0
                    if self.weapon == "Assault Rifle":
                        self.current = sprites.Player_Shooting_AR_List
                        self.animation_int = 0
                
            self.counter = 0
            
    def jump(self):
        if self.moving_up:
            if self.Y == self.ground:
                self.Y -= self.jump_height
                
    def gravity(self):
        if self.Y < self.ground:
            self.moving_down = True
            self.moving_up = False
            self.Y += self.grav_speed
        else:
            self.moving_down = False

    def regen(self):
        if not self.dead:
            self.health += 0.5

    def shot(self):

        self.shot_counter += 1
        
        if self.shooting and self.aiming:
            if self.bullet_counter == 0:
                self.bullets_list.append((self.X, self.Y))
                self.bullet_X = self.X
                self.bullet_Y = self.Y + 50
                self.bullet_direction = self.direction
                self.bullet_counter += 1
                self.bullet_dead = False
                
        if self.bullet_direction == "Left" and not self.bullet_dead:
            self.bullet_X -= self.bullet_speed
        elif self.bullet_direction == "Right" and not self.bullet_dead:
            self.bullet_X += self.bullet_speed

        if self.bullet_counter >= 1:
            if self.bullet_X <= 0 or self.bullet_X >= 1280:
                self.bullet_counter = 0
                self.shot_counter = 0
                del self.bullets_list[:]
                    
    def change_weapon(self):
        self.weapon_int += 1
        if self.weapon_int > 5:
            self.weapon_int = 0
        self.weapon = self.weapon_dict.get(self.weapon_int)
        self.weapon_damage = self.weapon_damage_dict.get(self.weapon)

    def __main__(self):

        self.animation()
        self.movement()
        self.shot()
        self.jump()
        self.gravity()

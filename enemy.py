# --- Imports --- #

import sprites
import random

# --- Enemy Class --- #

class Enemy(object):

    X = random.randrange(0,1280)
    Y = 530
    direction = "Right"
    damage = 30
    animation_int = 0
    current = sprites.Enemy_Walking_List
    speed = 5
    health = 100
    counter = 0
    wait_counter = 0
    
    moving = False
    dead = False
    attack = False
    next_0 = True
    next_1 = False

    def movement(self, Player_X):
        if not self.attack and self.moving and not self.dead:
            if Player_X < self.X:
                self.direction = "Left"
                self.X -= self.speed
            elif Player_X > self.X:
                self.direction = "Right"
                self.X += self.speed

    def animation(self):

        self.counter += 1

        if self.counter == 10:
            if self.moving:
                self.current = sprites.Enemy_Walking_List
                if self.next_0:
                    self.animation_int = 0
                    self.next_0 = False
                    self.next_1 = True
                elif self.next_1:
                    self.animation_int = 1
                    self.next_0 = True
                    self.next_1 = False

                if self.dead == True:
                    self.moving = False
                    self.wait_counter += 1
                    if self.wait_counter == 8:
                        self.X = self.new_X()
                        self.Y = 530
                        self.health = 100
                        self.dead = False
                        self.moving = False
                        self.wait_counter = 0


            else:
                if self.dead == True and self.moving == False:
                    self.wait_counter += 1
                    if self.wait_counter == 8:
                        self.moving = True
                        self.wait_counter = 0

            self.counter = 0 

    def new_X(self):
        return random.randrange(0,1280)

    def __main__(self, Player_X):

        self.animation()
        self.movement(Player_X)

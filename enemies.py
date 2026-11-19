#importing related libraries and data from external files
from settings import *
import random
import math
import pygame
#creating a class
class Enemy():
	#declaring attributes of the class
    def __init__(self, current_pos):
        self.current_pos = current_pos
        self.alive = True
        self.speed = resolution[0]/128
        self.size = [resolution[0] / 45, resolution[0] / 45]
        self.destination = [random.randint(0, resolution[0]), random.randint(0, resolution[1])]
        self.reloading = 0
	#creating method for enemy movement
    def movement(self, screen, world):
    	#drawing enemy
        enemy_rect = pygame.Rect(self.current_pos, self.size)
        pygame.draw.rect(screen, red, enemy_rect)
        #establishing motion of the enemy
        angle = math.atan2((self.destination[1] - self.current_pos[1]), (self.destination[0] - self.current_pos[0]))
        new_x = self.current_pos[0] + self.speed * math.cos(angle)
        new_y = self.current_pos[1] + self.speed * math.sin(angle)
        new_rect = pygame.Rect(new_x, new_y, self.size[0], self.size[1])
        #check if movement causes a collision
        collision = False
        for wall in world:
            wall_rect = pygame.Rect(wall, wall_size)
            if new_rect.colliderect(wall_rect):
                collision = True
                break
        #move if no collision
        if collision == False:
            self.current_pos = [new_x, new_y]
        else:
            self.destination = [random.randint(0, resolution[0]), random.randint(0, resolution[1])]
        #if the enemy reaches the destination pick a new one
        if math.hypot(self.current_pos[0] - self.destination[0], self.current_pos[1] - self.destination[1]) < self.speed:
            self.destination = [random.randint(0, resolution[0]), random.randint(0, resolution[1])]
    #creating method for enemy triggering
    def trigger(self, player_pos, world):
    	#turning coordinates into integer tuples
        player_tupple = (int(player_pos[0]), int(player_pos[1]))
        current_tupple = (int(self.current_pos[0]), int(self.current_pos[1]))
        #check for obstructions
        for wall in world:
            wall_rect = pygame.Rect(wall, wall_size)
            obstruction = wall_rect.clipline(player_tupple, current_tupple)
            if obstruction:
                self.speed = resolution[0]/128
                return False
        self.speed = 0
        return True
#create list of enemy class objects
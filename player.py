#import data from other files and libraries
from settings import *
import pygame
import math
#initializing pygame modules
pygame.init()
#declaring variables related to the functionality of the player's subroutines
player_speed = resolution[0]/128
player_alive = True
player_size = [resolution[0]/45, resolution[0]/45]
launch = None
reload_timer = 0
#creating subroutine for movement
def player_move(world, player_speed, player_pos, player_size, screen):
    new_position = player_pos.copy()
    #getting data about keys that are pressed currently
    key = pygame.key.get_pressed()
    #moving character based on the keys pressed
    if key[pygame.K_s] and key[pygame.K_d]:
        new_position[0] += player_speed * math.cos(math.pi/4)
        new_position[1] += player_speed * math.sin(math.pi/4)
    elif key[pygame.K_s] and key[pygame.K_a]:
        new_position[0] += player_speed * math.cos(math.pi - math.pi/4)
        new_position[1] += player_speed * math.sin(math.pi - math.pi/4)
    elif key[pygame.K_w] and key[pygame.K_d]:
        new_position[0] += player_speed * math.cos(-math.pi/4)
        new_position[1] += player_speed * math.sin(-math.pi/4)
    elif key[pygame.K_w] and key[pygame.K_a]:
        new_position[0] += player_speed * math.cos(math.pi + math.pi/4)
        new_position[1] += player_speed * math.sin(math.pi + math.pi/4)
    elif key[pygame.K_a]:
        new_position[0] -= player_speed
    elif key[pygame.K_d]:
        new_position[0] += player_speed
    elif key[pygame.K_w]:
        new_position[1] -= player_speed
    elif key[pygame.K_s]:
        new_position[1] += player_speed
    #preventing player from leaving the screen
    if new_position[0] > resolution[0] - resolution[0] / 50:
        new_position[0] = resolution[0] - resolution[0] / 50
    if new_position[0] < 0:
        new_position[0] = 0
    if new_position[1] > resolution[1] - resolution[0] / 50:
        new_position[1] = resolution[1] - resolution[0] / 50
    if new_position[1] < 0:
        new_position[1] = 0
    #creating future player position
    new_rect = pygame.Rect(new_position, player_size)
    #checking if this future player position is colliding with any of the obstacles
    collision = False
    for wall in world:
        wall_rect = pygame.Rect(wall, wall_size)
        if new_rect.colliderect(wall_rect):
            collision = True
            break
    #if there is no collision possible position is converted into a current position
    if not collision:
        player_pos[:] = new_position
    #draw main character
    player_box = pygame.Rect(player_pos, player_size)
    pygame.draw.rect(screen, green, player_box)
#creating subroutine for player shooting
def shoot(reload_timer):
    if pygame.mouse.get_pressed(3)[0] == True and reload_timer == 0:
        return True
    else:
        return False
#import data from other files and libraries
import pygame
from settings import *
from map import *
from player import *
from bullets import *
from enemies import * 
from maps import map_pool
from menus import *
import random
#create variable to store state of the game
state = 'main_menu'
#create initial list of enemy class objects
enemy_list = []
for enemy in enemies:
    enemy_list.append(Enemy(enemy))
#initializing pygame modules
pygame.init()
#creating screen object
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
#loop that creates and updates the window
run = True
while run:
    #checks if the state is main menu
    if state == 'main_menu':
        state = main_menu(screen)
    #checks if the player is alive
    if player_alive == False:
        bullet_list = []
        enemy_list = []
        player_alive = True
        state = death_screen(screen)
        new_outline = random.choice(map_pool)
        world = room_generation(new_outline)[0]
        enemies = room_generation(new_outline)[1]
        player_pos = room_generation(new_outline)[2]
        for enemy in enemies:
            enemy_list.append(Enemy(enemy))
    #checks if the state is game
    if state == 'game':
        #changing the room once all enemies are dead
        if len(enemy_list) == 0:
            new_outline = random.choice(map_pool)
            world = room_generation(new_outline)[0]
            enemies = room_generation(new_outline)[1]
            player_pos = room_generation(new_outline)[2]
            for enemy in enemies:
                enemy_list.append(Enemy(enemy))
        #making the background black
        screen.fill(black)
        #variables and subroutines related to the enemies
        for enemy in enemy_list:
            #change position of the enemy and move him
            enemy.movement(screen, world)
            #shoot if the player within enemies field of view and reloading time is 0
            if enemy.trigger(player_pos, world) == True and enemy.reloading == 0:
                enemy.reloading = 30
                bullet_list.append(Bullet('enemy', enemy.current_pos, player_pos))
            #reduce reloading time each frame
            if enemy.reloading > 0:
                enemy.reloading -= 1
            #kill enemy if he is hit by bullet
            if enemy.alive == False:
                enemy_list.remove(enemy)
        #variables and subroutines related to player movement
        player_move(world, player_speed, player_pos, player_size, screen)
        #detecting clicks of the left mouse button
        launch = shoot(reload_timer)
        #if click is detected bullet onject is created and reloading timer is set to 60
        if launch == True:
            bullet_list.append(Bullet('player', player_pos, pygame.mouse.get_pos()))
            reload_timer = 30
        #if bullet is colliding with the obstacle it stops existing
        new_bullet_list = []
        for bullet in bullet_list:
            #detect collision with enemies or player
            if bullet.deal_damage(enemy_list, player_pos, player_size):
                player_alive = False
            if bullet.bullet_flight(screen, world):
                new_bullet_list.append(bullet)
        bullet_list = new_bullet_list
        #timer decreasing each frame
        if reload_timer > 0:
            reload_timer -= 1
        #variables and subroutines related to obstacles
        draw_walls(world, screen)
        #loop that checks if the player is trying to exit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    #set frame rate to a fixed value
    clock.tick(60)
#closing pygame modules
pygame.quit()
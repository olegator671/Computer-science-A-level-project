#importing related libraries and data from external files
import pygame
import math
from settings import *
from map import world
#create an indicator for bullet state and array where existing bullets are stored
flight = False
bullet_list = []
#creating class bullet
class Bullet():
	#declaring attributes of the class
	def __init__(self, source, start, destination):
		self.source = source
		self.start = start.copy()
		self.destination = destination
		self.speed = resolution[0]/64
		self.size = [resolution[0]/90, resolution[0]/90]
		self.angle = math.atan2((destination[1] - start[1]), (destination[0] - start[0]))
	#creating method of the class bulet that is responsible for bullet flight
	def bullet_flight(self, screen, world):
		#drawing bullet
		bullet_rect = pygame.Rect(self.start, self.size)
		pygame.draw.rect(screen, white, bullet_rect)
		#detect collisions
		for wall in world:
			wall_rect = pygame.Rect(wall, wall_size)
			if bullet_rect.colliderect(wall_rect):
				return False
		#moving the bullet
		self.start[0] += self.speed * math.cos(self.angle)
		self.start[1] += self.speed * math.sin(self.angle)
		#if no collisions detected bullet keeps flying
		return True
	#create method to deal damage
	def deal_damage(self, enemies, player_pos, player_size):
		#detect collision with enemies
		if self.source == 'player':
			for enemy in enemies:
				if pygame.Rect(enemy.current_pos, enemy.size).colliderect(pygame.Rect(self.start, self.size)):
					enemy.alive = False
		#detect collision with player
		if self.source == 'enemy':
			if pygame.Rect(player_pos, player_size).colliderect(pygame.Rect(self.start, self.size)):
				return True
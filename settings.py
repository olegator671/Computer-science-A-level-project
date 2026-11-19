import pygame
pygame.init()

#resolution
infoObject = pygame.display.Info()
resolution = (infoObject.current_w, infoObject.current_h)

#colors
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
grey = (30, 30, 30)

#walls
wall_size = [resolution[0]/21, resolution[1]/11]
starting_point = (0, 0)
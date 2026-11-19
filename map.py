#import data from external files
from settings import *
from maps import *
#creating subroutine for room generation
def room_generation(outline):
	#storing coordinates of the enemies, player and obstacles
	player_pos = None
	world = []
	enemies = []
	#creating counter to keep track of the room generation
	counter_x = 0
	counter_y = 0
	for line in outline:
		#check the character
		for tile in line:
			if tile == 'W':
				world.append([starting_point[0] + wall_size[0] * counter_x, starting_point[1] + wall_size[1] * counter_y])
			elif tile == 'E':
				enemies.append([(starting_point[0] + wall_size[0] * counter_x) + wall_size[0] * 0.25, (starting_point[1] + wall_size[1] * counter_y) + wall_size[1] * 0.25])
			elif tile == 'X':
				player_pos = [(starting_point[0] + wall_size[0] * counter_x) + wall_size[0] * 0.25, (starting_point[1] + wall_size[1] * counter_y) + wall_size[1] * 0.25]
			counter_x += 1
		counter_y += 1
		counter_x = 0
	return world, enemies, player_pos
#storing output of the room generation subroutine
world = room_generation(map1)[0]
enemies = room_generation(map1)[1]
player_pos = room_generation(map1)[2]
#subroutine to draw obstacles
def draw_walls(world, screen):
    for wall in world:
        wall_rect = pygame.Rect(wall, wall_size)
        pygame.draw.rect(screen, white, wall_rect, 1)

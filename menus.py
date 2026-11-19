import pygame
from settings import *
#create main menu subroutine
def main_menu(screen):
    #create a fond
    font = pygame.font.Font(None, int(resolution[0]/15))
    #variables to store button characteristics
    button_size = [resolution[0]/3.6, resolution[0]/13]
    button_pos2 = [resolution[0]/2 - resolution[0]/7.2 , resolution[1]/2 - resolution[0]/26]
    button_pos1 = [resolution[0]/2 - resolution[0]/7.2 , resolution[1]/2 - resolution[0]/7]
    #creating button rectangles to interact with
    start_button = pygame.Rect(button_pos1, button_size)
    exit_button = pygame.Rect(button_pos2, button_size)
    #creating individual loop for the main menu
    while True:
        #fill the screen with grey color
        screen.fill(grey)
        #draw buttons
        pygame.draw.rect(screen, red, start_button)
        pygame.draw.rect(screen, red, exit_button)
        #create a text
        start_text = font.render("Start Game", True, white)
        exit_text = font.render("Exit Game", True, white)
        #put this texts on each button
        screen.blit(start_text, (start_button.x + button_size[0]/20, start_button.y + button_size[1]/4))
        screen.blit(exit_text, (exit_button.x + button_size[0]/20, exit_button.y + button_size[1]/4))
        #detect player actions
        for event in pygame.event.get():
            #detect attempts to close the window
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            #detect player pressing the buttons 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return 'game'
                if exit_button.collidepoint(event.pos):
                    pygame.quit()
                    exit()
        #update the window
        pygame.display.update()
#creating subroutine for death screen
def death_screen(screen):
    #create a font
    font = pygame.font.Font(None, int(resolution[0]/27))
    #variables to store button characteristics
    button_size = [resolution[0]/3.6, resolution[0]/13]
    button_pos = [resolution[0]/2 - resolution[0]/7.2 , resolution[1]/2 - resolution[0]/7]
    button_rect = pygame.Rect(button_pos, button_size)
    #creating individual loop for the death screen
    while True:
        #fill the background with grey color
        screen.fill(grey)
        #draw button
        pygame.draw.rect(screen, red, button_rect)
        #create a text
        text_surface = font.render("Return to Main Menu", True, white)
        #put this text on a button
        screen.blit(text_surface, (button_rect.x + button_size[0]/20, button_rect.y + button_size[1]/4))
        #detect player actions
        for event in pygame.event.get():
            #detect attempts to close the window
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            #detect player pressing the button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return "main_menu"
        #update the window
        pygame.display.update()
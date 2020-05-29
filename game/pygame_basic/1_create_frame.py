import pygame

pygame.init() # initailize

# screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# screen title
pygame.display.set_caption("Nado Game") # Game Name

# event loop
running = True # False : finish
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if push X button
            running = False # Game finish

#pygame finish
pygame.quit()
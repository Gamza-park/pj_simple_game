import pygame

pygame.init() # initailize

# screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# screen title
pygame.display.set_caption("Nado Game") # Game Name

# backgoround image
background = pygame.image.load("/Users/gamza/PycharmProjects/game/pygame_basic/background.png")

# event loop
running = True # False : finish
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if push X button
            running = False # Game finish
    screen.blit(background,(0,0)) # drawing background

    pygame.display.update() # background update
#pygame finish
pygame.quit()
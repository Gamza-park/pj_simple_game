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

# insert sprite
character = pygame.image.load("/Users/gamza/PycharmProjects/game/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) # center pos
character_y_pos = screen_height - character_height # under pos

# event loop
running = True # False : finish
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if push X button
            running = False # Game finish
    screen.blit(background,(0,0)) # drawing background
    screen.blit(character,(character_x_pos,character_y_pos)) # drawing character

    pygame.display.update() # background update
#pygame finish
pygame.quit()
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
to_x = 0
to_y = 0
# event loop
running = True # False : finish
while running:
    for event in pygame.event.get(): # event mean
        if event.type == pygame.QUIT: # if push X button
            running = False # Game finish

        if event.type == pygame.KEYDOWN: # push the key
            if event.key == pygame.K_LEFT: # left key
                to_x -= 5
            elif event.key == pygame.K_RIGHT: # right key
                to_x += 5
            elif event.key == pygame.K_UP: # up key
                to_y -= 5
            elif event.key == pygame.K_DOWN: # down key
                to_y += 5

        if event.type == pygame.KEYUP: #
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    # Width Limit
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    # Height Limit
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background,(0,0)) # drawing background
    screen.blit(character,(character_x_pos,character_y_pos)) # drawing character

    pygame.display.update() # background update
#pygame finish
pygame.quit()
import pygame

pygame.init() # initailize

# screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# screen title
pygame.display.set_caption("Nado Game") # Game Name

# FPS
clock = pygame.time.Clock()

# backgoround image
background = pygame.image.load("/Users/gamza/PycharmProjects/game/pygame_basic/background.png")

# insert sprite
character = pygame.image.load("/Users/gamza/PycharmProjects/game/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) # center pos
character_y_pos = screen_height - character_height # under pos

# moving
to_x = 0
to_y = 0

# move speed
character_speed = 0.6

# enemy character
enemy = pygame.image.load("/Users/gamza/PycharmProjects/game/pygame_basic/enemy.png")
enemy_size = character.get_rect().size
enemy_width = character_size[0]
enemy_height = character_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) # center pos
enemy_y_pos = (screen_height / 2) - (enemy_height / 2) # under pos

# event loop
running = True # False : finish
while running:

    dt = clock.tick(20) # Game's frame
    print("fps :" + str(clock.get_fps()))

    for event in pygame.event.get(): # event mean
        if event.type == pygame.QUIT: # if push X button
            running = False # Game finish

        if event.type == pygame.KEYDOWN: # push the key
            if event.key == pygame.K_LEFT: # left key
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # right key
                to_x += character_speed
            elif event.key == pygame.K_UP: # up key
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # down key
                to_y += character_speed

        if event.type == pygame.KEYUP: #
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

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

    # Collision
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # collision check
    if character_rect.colliderect(enemy_rect):
        print("collision")
        running = False
    

    screen.blit(background,(0,0)) # drawing background
    screen.blit(character,(character_x_pos,character_y_pos)) # drawing character
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos)) # draw enemy

    pygame.display.update() # background update

#pygame finish
pygame.quit()
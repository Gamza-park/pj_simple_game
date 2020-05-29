import pygame
import random
############################################################
# must
pygame.init()  # initailize

# screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# screen title
pygame.display.set_caption("Rain game")  # Game Name

# FPS
clock = pygame.time.Clock()

########################################################################

# 1. game setting ( background, image, point, speed, font )

# background image
background = pygame.image.load("/Users/gamza/PycharmProjects/game/rain_game/background.png")

# character image
character = pygame.image.load("/Users/gamza/PycharmProjects/game/rain_game/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = (screen_height) - (character_height)

# moving point
to_x = 0
character_speed = 10

# enemy
enemy = pygame.image.load("/Users/gamza/PycharmProjects/game/rain_game/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0,screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 10


# event loop
running = True  # False : finish
while running:

    dt = clock.tick(20)  # Game's frame
    print("fps :" + str(clock.get_fps()))

    # 2. event
    for event in pygame.event.get():  # event mean
        if event.type == pygame.QUIT:  # if push X button
            running = False  # Game finish
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. game character position
    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > (screen_width - character_width):
        character_x_pos = (screen_width - character_width)

    enemy_y_pos += enemy_speed
    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    # 4. character collision
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        running = False

    # 5. draw screen
    screen.blit(background, (0, 0))  # drawing background
    screen.blit(character, (character_x_pos, character_y_pos))  # drawing character
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))

    pygame.display.update()  # background update

pygame.time.delay(1500) # wait time 1.5(s)

# pygame finish
pygame.quit()
import pygame
import os
############################################################
# must
pygame.init()  # initailize

# screen size
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# screen title
pygame.display.set_caption("misail game")  # Game Name

# FPS
clock = pygame.time.Clock()

########################################################################

# 1. game setting ( background, image, point, speed, font )
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

# background
background = pygame.image.load(os.path.join(image_path, "background.png"))
# stage
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]
# character
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = (screen_height - stage_height - character_height)


# event loop
running = True  # False : finish
while running:

    dt = clock.tick(20)  # Game's frame
    print("fps :" + str(clock.get_fps()))

    # 2. event
    for event in pygame.event.get():  # event mean
        if event.type == pygame.QUIT:  # if push X button
            running = False  # Game finish

    # 3. game character position

    # 4. character collision

    # 5. draw screen
    screen.blit(background, (0, 0))  # drawing background
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos,character_y_pos))

    pygame.display.update()  # background update

pygame.time.delay(1500) # wait time 1.5(s)

# pygame finish
pygame.quit()
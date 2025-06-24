import pygame
import sys
from random import randint


# start my game example
pygame.init()

game_font = pygame.font.Font(None, 30)

screen_width, screen_height = 800, 600
screen_fill_color = (32, 52, 71)
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Awesome Shooter Game")

FIGHTER_STEP = 0.1 # step of moving of ship #
# function of moving of this ship #
fighter_image = pygame.image.load('images_game/fighter.png')
fighter_width, fighter_height = fighter_image.get_size()
fighter_x, fighter_y = screen_width / 2 - fighter_width / 2, screen_height - fighter_height
fighter_is_moving_left, fighter_is_moving_right = False, False

# rocket load and moving process
ROCKET_STEP = 0.3
rocket_image = pygame.image.load('images_game/racket.png')
rocket_width, rocket_height = rocket_image.get_size()
rocket_x, rocket_y = 0, 0
rocket_was_fired = False

# enemy creation alien
ALIEN_STEP = 0.08
alien_image = pygame.image.load('images_game/alien.png')
alien_width, alien_height = alien_image.get_size()
alien_x, alien_y = randint(0, screen_width - alien_width), 0

game_is_running = True

while game_is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            # moving to left and right that shown below and space
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = True

            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = True

            if event.key == pygame.K_SPACE:
                rocket_was_fired = True
                rocket_x = fighter_x + fighter_width / 2 - rocket_width / 2
                rocket_y = fighter_y - rocket_height

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = False
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = False

    if fighter_is_moving_left and fighter_x >= FIGHTER_STEP:
        fighter_x -= FIGHTER_STEP
    if fighter_is_moving_right and fighter_x <= screen_width - fighter_width - FIGHTER_STEP:
        fighter_x += FIGHTER_STEP
# alien goes down
    alien_y += ALIEN_STEP


    if rocket_was_fired and rocket_y + rocket_height < 0:
        rocket_was_fired = False
    # this movies rocket to the topy by y
    if rocket_was_fired:
        rocket_y -= ROCKET_STEP

    screen.fill(screen_fill_color)
    screen.blit(fighter_image, (fighter_x, fighter_y))
# showing alien
    screen.blit(alien_image, (alien_x, alien_y))

    if rocket_was_fired:
        screen.blit(rocket_image, (rocket_x, rocket_y))

    pygame.display.update()

    if alien_y + alien_height > fighter_y:
        game_is_running = False
# finishing game
game_over_text = game_font.render("Game Over", True, 'white')
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (screen_width / 2, screen_height / 2)
screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()
pygame.time.wait(5000)

pygame.quit()
import pygame
import sys



pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Awesome Shooter Game")

fighter_image = pygame.image.load('images_game/starship.png')

fighter_width, fighter_height = fighter_image.get_size()

fighter_x, fighter_y = screen_width / 2 - fighter_width / 2, screen_height - fighter_height


while True:
    for event in pygame.event.get():




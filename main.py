import pygame
import sys



pygame.init()

screen_width, screen_height = 800, 600


screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("My Pygame")

rect_width, rect_height = 100, 200
rect_x = screen_width / 2 - rect_width / 2
rect_y = screen_height / 2 - rect_height / 2
rect_color = pygame.Color('lightyellow')

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))


    pygame.display.update()






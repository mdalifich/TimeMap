import requests
import pygame
from pygame import *
from random import randint, randrange
import os
from maps import *


if __name__ == '__main__':
    pygame.init()
    size = width, heigth = (800, 450)
    screen = pygame.display.set_mode((width, heigth))
    running = True
    MMM = Map(0, 0, screen)

    while running:
        screen.fill((130, 25, 75))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        MMM.draw()
        pygame.display.update()
        pygame.display.flip()
    pygame.quit()

response = requests.get("https://static-maps.yandex.ru/1.x/?ll=135.695439%2C-26.781760&l=map&z=4")
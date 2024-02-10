import pygame
from pygame import *
import os
import load_image
from load_image import *
from random import randint
import requests
from io import BytesIO


class Map(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        super().__init__()
        self.x, self.y = x, y
        self.response = requests.get("https://static-maps.yandex.ru/1.x/?ll=135.695439%2C-26.781760&l=map&z=4")
        print(self.response.content)
        self.image = pygame.image.load(BytesIO(self.response.content))


        self.image = pygame.transform.scale(self.image, (600, 450))
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
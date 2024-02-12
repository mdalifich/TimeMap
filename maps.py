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
        self.WorldX, self.WorldY = 135.6, 26.7
        self.plusMetka = f'&pt=0%2C0'
        self.t = 'https://static-maps.yandex.ru/1.x/?'
        self.zoom = 4
        self.HTTPS = f"{self.t}ll={str(self.WorldX)}%2C-{str(self.WorldY)}&l=map&z=4"
        self.response = requests.get(self.HTTPS)
        self.image = pygame.image.load(BytesIO(self.response.content))
        self.image = pygame.transform.scale(self.image, (600, 450))
        self.screen = screen

    def Point(self, x, y):
        self.plusMetka += f'~{x}%2C{y}'
        self.HTTPS += self.plusMetka
        self.image = pygame.image.load(BytesIO(self.response.content))

    def zooming(self, zoom):
        self.zoom = zoom
        self.update(0, 0)

    def update(self, plusX, plusY):
        self.WorldX += plusX
        self.WorldY += plusY
        self.HTTPS = self.t + f"ll={str(self.WorldX)}%2C-{str(self.WorldY)}&l=map&z={self.zoom}" + self.plusMetka
        self.response = requests.get(self.HTTPS)
        self.image = pygame.image.load(BytesIO(self.response.content))

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
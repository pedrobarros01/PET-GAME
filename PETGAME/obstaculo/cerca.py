import pygame
from pygame.locals import *

class Cerca(pygame.sprite.Sprite):
    def __init__(self, altura, largura, velocidade):
        pygame.sprite.Sprite.__init__(self)
        self.__altura_da_tela = altura
        self.__largura_da_tela = largura
        self.image = pygame.image.load('assets/image/sprite_cerca.png')
        self.rect = self.image.get_rect()
        self.__velocidade_cerca = velocidade * 5
        self.rect.y = self.__altura_da_tela - (self.image.get_height() * 1.4)
        self.rect.x = self.__largura_da_tela - self.image.get_width()

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = self.__largura_da_tela
        self.rect.x -= self.__velocidade_cerca

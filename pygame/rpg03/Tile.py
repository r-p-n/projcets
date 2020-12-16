import pygame
from Constants import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y, group):
        pygame.sprite.Sprite.__init__(self, group)
        self.screen = pygame.display.get_surface()
        self.image = image
        self.raw = x, y
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * STEP
        self.rect.y = y * STEP

    # def set_x(self, x):
    #     self.x = x
    #
    # def set_y(self, y):
    #     self.x = y

    # def set_z(self, z):
    #     self.x = z

    def draw(self, offset):
        self.screen.blit(self.image, (self.x * STEP + offset[0], self.y * STEP + offset[1], STEP, STEP))


    # TODO make a subclass for each imageset, which will have onwalk, custom scripts, etc


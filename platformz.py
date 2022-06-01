import settings
import pygame
import os


# x location, y location, img width, img height, img file
class Platformz(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(settings.png_folder, img)).convert()
        self.image.convert_alpha()
        self.image.set_colorkey(settings.plat_ALPHA)
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc
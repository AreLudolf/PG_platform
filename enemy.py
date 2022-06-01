import pygame
import os
import settings

class Enemy(pygame.sprite.Sprite):
    """
    Spawn an enemy
    """
    def __init__(self,x,y,img, distance):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(settings.png_folder,img))
        self.image.convert_alpha()
        self.image.set_colorkey(settings.enemy_ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0 # counter variable for movement
        self.distance = distance
        

    def move(self):
        '''
        enemy movement
        '''
        speed = settings.enemy_speed
        if self.counter >= 0 and self.counter <= self.distance:
            self.rect.x += speed
        elif self.counter >= self.distance and self.counter <= self.distance*2:
            self.rect.x -= speed
        else:
            self.counter = 0

        self.counter += 1
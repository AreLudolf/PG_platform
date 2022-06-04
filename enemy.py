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
        self.movey = 1

    def move(self, ground_list, plat_list):
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
        self.movey += 1 #gravity

        #ground and platform collision detect
        ground_hit_list = pygame.sprite.spritecollide(self, ground_list, False)
        if self.movey > 0:
            for g in ground_hit_list:
                self.movey = 0
                #self.gravityon = False
                self.rect.bottom = g.rect.top +1
        plat_hit_list = pygame.sprite.spritecollide(self, plat_list, False)
        if self.movey > 0:
            for p in plat_hit_list:
                #self.gravityon = False
                self.movey = 0
                self.rect.bottom = p.rect.top +1
        
        #walk off platforms and ground
        if not plat_hit_list or not ground_hit_list:
            self.movey += 1


        self.rect.y = self.rect.y + self.movey

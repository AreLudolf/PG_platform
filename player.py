import settings
import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.movex = 0
        self.movey = settings.gravity
        self.frame = 0
        self.hp = 10
        self.gravityon = True

        for i in range(1, 5):
            img = pygame.image.load(os.path.join(settings.png_folder, 'hero' + str(i) + '.png')).convert()

            img.convert_alpha()     # optimise alpha
            img.set_colorkey(settings.player_ALPHA)
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    def control(self,x,y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y

    def update(self, enemy_list, ground_list, plat_list, tx, ty):
        # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3*settings.ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // settings.ani], True, False)

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3*settings.ani:
                self.frame = 0
            self.image = self.images[self.frame//settings.ani]

        #enemy collision
        hit_list = pygame.sprite.spritecollide(self, enemy_list, False)
        for enemy in hit_list:
            self.hp -= 1
            print(self.hp)

        #ground collision
        ground_hit_list = pygame.sprite.spritecollide(self, ground_list, False)
        if self.movey > 0:
            for g in ground_hit_list:
                self.movey = 0
                self.gravityon = False
                self.rect.bottom = g.rect.top +1

        #Platform collision
        plat_hit_list = pygame.sprite.spritecollide(self, plat_list, False)
        if self.movey > 0:
            for p in plat_hit_list:
                self.gravityon = False
                self.movey = 0
                self.rect.bottom = p.rect.top +1

        # fall off the world
        if self.rect.y > settings.window_height:
            self.hp -=1
            print(self.hp)
            self.rect.x = tx
            self.rect.y = ty
        
        self.movey +=1
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

    def jump(self, plat_list, ground_list):
        plat_hit_list = pygame.sprite.spritecollide(self, plat_list, False)
        ground_hit_list = pygame.sprite.spritecollide(self, ground_list, False)
        if plat_hit_list or ground_hit_list:
            self.movey -= settings.jump_height
            self.gravityon = True


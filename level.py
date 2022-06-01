import pygame
import enemy
import os
import settings
import platformz

class Level():
    def bad(lvl, eloc):
        if lvl == 1:
            enemi1 = enemy.Enemy(eloc[0],eloc[1],'enemy.png', 40) # spawn enemy
            enemi2 = enemy.Enemy(eloc[0] + 50,eloc[1],'enemy.png', 80)
            enemy_list = pygame.sprite.Group() # create enemy group
            enemy_list.add(enemi1, enemi2)              # add enemy to group
        if lvl == 2:
            print("Level " + str(lvl) )

        return enemy_list

    def ground(lvl,gloc,tx,ty):
        ground_list = pygame.sprite.Group()
        i=0
        if lvl == 1:
            while i < len(gloc):
                ground = platformz.Platformz(gloc[i],settings.window_height-ty,tx,ty,'tile_grass.png')
                ground_list.add(ground)
                i=i+1

        if lvl == 2:
            print("Level " + str(lvl) )

        return ground_list

    def platform(lvl,tx,ty):
        plat_list = pygame.sprite.Group()
        ploc = []
        i=0
        if lvl == 1:
            ploc.append((200,settings.window_height-ty-128,3))
            ploc.append((300,settings.window_height-ty-256,3))
            ploc.append((500,settings.window_height-ty-128,4))
            while i < len(ploc):
                j=0
                while j <= ploc[i][2]:
                    plat = platformz.Platformz((ploc[i][0]+(j*tx)),ploc[i][1],tx,ty,'tile_grass.png')
                    plat_list.add(plat)
                    j=j+1
                print('run' + str(i) + str(ploc[i]))
                i=i+1
           
        if lvl == 2:
            print("Level " + str(lvl) )

        return plat_list
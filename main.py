import pygame
import sys
import os
import settings
import player
import enemy
import level
import platform

'''
Variables
'''
worldx = settings.window_width
worldy = settings.window_height
world = pygame.display.set_mode([worldx,worldy])


'''
Setup
'''
clock = pygame.time.Clock()
pygame.init()
main = True
backdrop = pygame.image.load(os.path.join(settings.png_folder,'tmp_bckgr.png'))
backdropbox = world.get_rect()

all_sprites = pygame.sprite.Group()
player = player.Player()   # spawn player
player.rect.x = 0   # go to x
player.rect.y = 0   # go to y
player_list = pygame.sprite.Group()
player_list.add(player)

eloc = [] #enemy location
eloc = [400,0]
#level = level.Level()
enemy_list = level.Level.bad(1, eloc)
all_sprites.add(enemy_list)

gloc = [] #ground location
tx   = 64 #tile size x
ty   = 64 #tile size y

i=0
while i <= (worldx/tx)+tx:
    gloc.append(i*tx)
    i=i+1

ground_list = level.Level.ground(1,gloc,tx,ty)
all_sprites.add(ground_list)
plat_list = level.Level.platform(1, tx, ty)
all_sprites.add(plat_list)

'''
Main Loop
'''
while main:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-settings.move_speed,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(settings.move_speed,0)
            if event.key == pygame.K_SPACE:
                print("jump")
                player.jump()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(settings.move_speed,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-settings.move_speed,0)

        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

    # scroll the world forward
    if player.rect.x >= settings.scrl_forwardx:
            scroll = player.rect.x - settings.scrl_forwardx
            player.rect.x = settings.scrl_forwardx
            for obj in all_sprites:
                    obj.rect.x -= scroll

    # scroll the world backward
    if player.rect.x <= settings.scrl_backwardx:
            scroll = settings.scrl_backwardx - player.rect.x
            player.rect.x = settings.scrl_backwardx
            for obj in all_sprites:
                    obj.rect.x += scroll

    player.gravity()
    player.update(enemy_list, ground_list, plat_list, tx, ty)  # update player position
    world.blit(backdrop, backdropbox)
    player_list.draw(world)
    enemy_list.draw(world)
    for e in enemy_list:
        e.move()
    ground_list.draw(world)
    plat_list.draw(world)
    pygame.display.flip()
    clock.tick(settings.fps)

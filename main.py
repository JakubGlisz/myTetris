#from _typeshed import SupportsKeysAndGetItem
import pygame
import sys
import manager
import var

pygame.init()

screen = pygame.display.set_mode((var.width * var.size_of_tile, var.height * var.size_of_tile))
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
CONTROL = pygame.USEREVENT + 1
pygame.time.set_timer(SCREEN_UPDATE, var.REGULAR_FALL)
pygame.time.set_timer(CONTROL, var.CONTROL_RATE)

manager = manager.TILE_MANAGER()

move_left = False
move_right = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_DOWN:
                pygame.time.set_timer(SCREEN_UPDATE, var.FAST_FALL)
            if event.key == pygame.K_UP:
                manager.shape.rotateRight()
                if manager.checkCollision():
                    manager.shape.rotateLeft()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_DOWN:
                pygame.time.set_timer(SCREEN_UPDATE, var.REGULAR_FALL)
        if event.type == CONTROL:
            if move_left:
                manager.moveLeft()
            elif move_right:
                manager.moveRight()
        if event.type == SCREEN_UPDATE:
            if manager.haveFallen() == 0:
                manager.fall()
            manager.haveFallen()
    screen.fill(pygame.Color('black'))
    manager.drawBoard(screen)
    pygame.display.update()
    clock.tick(60)
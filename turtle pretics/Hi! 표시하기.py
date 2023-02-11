import pygame
import sys
from pygame.locals import*
from random import*

pygame.init()

screen=pygame.display.set_mode((600,500))

pygame.display.set_caption('Hi! 표시하기')

CLOCK=pygame.time.Clock()

sysfont=pygame.font.SysFont(None,36)

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255,255,255))

    cnt_txt=sysfont.render('Hi!',True,(0,0,0))

    screen.blit(cnt_txt,(randint(50,550),randint(50,450)))

    pygame.display.update()

    CLOCK.tick(1)
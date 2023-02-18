import pygame
from pygame.locals import*
import sys

pygame.init()
SURFACE=pygame.display.set_mode((300,300))
CLOCK=pygame.time.Clock()

BLACK=(0,0,0)
RED=(255,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
BLUE=(0,0,255)

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    SURFACE.fill(WHITE)

    pygame.draw.circle(SURFACE,GREEN,(150,150),150)

    rec=Rect(300/6,300/6,200,200)
    pygame.draw.rect(SURFACE,BLUE,rec)
    
    pygame.draw.polygon(SURFACE,BLACK,[[300/6*2,300/6*2],[300/6*4,300/6*2],[300/6*4,300/6*4]])    
    pygame.draw.polygon(SURFACE,RED,[[300/6*2,300/6*2],[300/6*2,300/6*4],[300/6*4,300/6*4]])    
    pygame.display.update()
    CLOCK.tick(1)
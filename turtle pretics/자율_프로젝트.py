import pygame
import sys
from pygame.locals import*

a=[]
b=[a,'Input password']
check=1

pygame.init()
SCREEN=pygame.display.set_mode((600,600))
pygame.display.set_caption('금고 프로그램')
CLOCK=pygame.time.Clock()
sysfont=pygame.font.SysFont(None,36)

while True:
    b=[a,'Input password']
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_p:
                password=input('비밀번호를 설정하세요.')
                print('\n비밀번호가 설정되었습니다.')
                a.clear()
                a.append(input('내용을 입력하세요.'))
                print('\n내용이 저장되었습니다.')
                check=1
            if event.key==K_y:
                open=input('\n비밀번호를 입력하세요.')
                if open==password:
                    print('\n금고가 열렸습니다.\n내용을 확인하세요.')
                    check=0
                else:
                    print('\n비밀번호가 잘못 입력되었습니다.\n')
                    print('다시 시도해주세요.\n')
                    check=1
            if event.key==K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    cnt_txt=sysfont.render(str(b[check]),True,(0,0,0))
    SCREEN.fill((255,255,255))
    rec=Rect(150,150,300,300)
    pygame.draw.rect(SCREEN,('#919090'),rec)
    pygame.draw.circle(SCREEN,('#3b3b3b'),(300,300),100)
    pygame.draw.line(SCREEN,(0,0,0),(250,350),(250,250))
    pygame.draw.line(SCREEN,(0,0,0),(251,350),(251,250))
    pygame.draw.line(SCREEN,(0,0,0),(252,350),(252,250))
    pygame.draw.line(SCREEN,(0,0,0),(253,350),(253,250))
    pygame.draw.line(SCREEN,(0,0,0),(254,350),(254,250))
    pygame.draw.line(SCREEN,(0,0,0),(255,350),(255,250))
    pygame.draw.line(SCREEN,(0,0,0),(256,350),(256,250))
    pygame.draw.line(SCREEN,(0,0,0),(257,350),(257,250))
    SCREEN.blit(cnt_txt,(300,75))
    pygame.display.update()
    CLOCK.tick(1)
import pygame
pygame.init()
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption('Draw')
screen.fill(255, 255, 255)




while True :
    for even in pygame.event.get():
        if event.type ==pygame.QUIT :
            sys.exit()

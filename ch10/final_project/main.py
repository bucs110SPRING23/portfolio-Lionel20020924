import pygame
from src import board, incident


def main():
    '''
    :describe:   Main program launcher, initializes music, events, screen refresh, chessboard background and
                a series of classes.
    :param :None
    :return:None
    '''
    pygame.mixer.init()
    pygame.init()
    bgm = pygame.mixer.music.load('./etc/the diva dance.mp3')
    pygame.mixer.music.play(-1)
    c = board.Checkerboard()# init Checkerboard
    show = incident.Show(c)# init screen refresh
    e = incident.Event(c, show)#init events
    while incident.Others.running:# events loop
        show.refresh_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                incident.Others.running = False
                pygame.quit()

        for player in range(4):
            c.screen.fill((255, 255, 255))
            e.event_wait_space(player)
            num = 1
            e.event_move(player, num - 1)


if __name__ == '__main__':
    main()

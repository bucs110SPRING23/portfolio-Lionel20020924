import pygame
import json
class Checkerboard:

    back_ground_color=(255, 255, 255)
    fps=60

    def __init__(self,width=1050,height=550):
        '''
        :describe   Initialization function, sets the dimensions of the interface, background image
            and reads the flight path.
        :param width int:defalut 1050
        :param height int:defalut 550
        :return:self instance
        '''
        pygame.display.set_caption("Flying chess")
        self.width=width
        self.height=height
        self.screen = pygame.display.set_mode([self.width, self.height])#set width and height
        self.screen.fill(Checkerboard.back_ground_color)
        self.bgimg = pygame.image.load("assets/bgimg.png")#load back ground image
        self.clock=pygame.time.Clock().tick(Checkerboard.fps)#set fps
        self.running=True
        with open('etc/data.json') as f:
            dic1 = json.load(f)
        self.fly_path = {int(k): v for k, v in dic1.items()}

    def __str__(self):
        return f"Windows width: {self.width}, height: {self.height} fps: {Checkerboard.fps}"



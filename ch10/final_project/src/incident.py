import pygame
import time
import random
pygame.init()


class Plane:

    def __init__(self, type, pos, img):
        '''
        :describe:Initialization function,load plane image,sets the Plane type,Plane position  and other status.
        :param type int:between 1~4
        :param pos tuple:The x y coordinates of the plane
        :param img str:path of plane image
        :return:self instance
        '''

        self.type = type  # Plane type: 1: yellow 2: green 3: blue 4: red
        self.position = pos  # Plane position
        self.img = pygame.image.load(img)  # load plane image
        self.fly = False  # Has taken off
        self.fina = False  # Whether it is in the end circle or not(the last straight path).
        self.fina_flag = [43, 4, 17, 30]
        self.direction = True
        self.list1 = [94, 73, 80, 87]  # start of the last straight path
        self.list2 = [100, 79, 86, 93]  # end of the last straight path
        self.win = False

    def move(self):
        '''
        :describe:The logical rules of aircraft movement.
        :param None
        :return:None
        '''
        if not self.fina:
            if self.position == 52:
                self.position = 0
            self.position += 1
            if self.position == self.fina_flag[self.type - 1]:
                self.fina = True
        else:
            if self.position < 60:
                self.position = self.list1[self.type - 1]
            if self.direction:
                self.position += 1
            else:
                self.position -= 1
            if self.position == self.list2[self.type - 1]:
                self.direction = False

    def __str__(self):
        return f"Status win:{self.win}, fly:{self.fly} fina:{self.fina}"


class Others:
    '''
    :describe:
    1. Initialize 4 planes for 4 players
    2. Set the starting and ending points of the plane
    3 Set the font and color
    4. Set the prompt
    '''
    # for 1
    yellow = [Plane(1, 53, "assets/yellow1.png"),
              Plane(1, 54, "assets/yellow2.png"),
              Plane(1, 55, "assets/yellow3.png"),
              Plane(1, 56, "assets/yellow4.png")]
    green = [Plane(2, 58, "assets/green1.png"),
             Plane(2, 59, "assets/green2.png"),
             Plane(2, 60, "assets/green3.png"),
             Plane(2, 61, "assets/green4.png")]
    blue = [Plane(3, 63, "assets/blue1.png"),
            Plane(3, 64, "assets/blue2.png"),
            Plane(3, 65, "assets/blue3.png"),
            Plane(3, 66, "assets/blue4.png")]
    red = [Plane(4, 68, "assets/red1.png"),
           Plane(4, 69, "assets/red1.png"),
           Plane(4, 70, "assets/red1.png"),
           Plane(4, 71, "assets/red1.png")]

    # for 2
    players_init_pos = [[53, 54, 55, 56], [58, 59, 60, 61], [63, 64, 65, 66], [68, 69, 70, 71]]
    players_score_pos = [[101, 102, 103, 104], [105, 106, 107, 108], [109, 110, 111, 112], [113, 114, 115, 116]]

    # for 3&4
    font_name = pygame.font.match_font('Microsoft YaHei')  # 2.获得字体文件
    font = pygame.font.Font(font_name, 20)  # 1.获取font对象（需要字体文件）
    text1 = font.render("Press Space To Shake The Dice", True, (0, 0, 0))
    text_color = [font.render("Yellow", True, (255, 184, 8)),
                  font.render("Green", True, (11, 136, 80)),
                  font.render("Blue", True, (34, 133, 226)),
                  font.render("Red", True, (240, 17, 12))]

    inital_pos = [57, 62, 67, 72]
    begin_pos = [46, 7, 20, 33]
    players = [yellow, green, blue, red]
    running = True

    def __str__(self):
        return f"Initializes some additional information"


class Event:

    def __init__(self, checkerboard, show):
        '''
        :describe:Bind to two other classes
        :param checkerboard:instannce of Checkerboard
        :param show:instannce of Show
        :return:self instance
        '''
        self.checkerboard = checkerboard
        self.show = show
        self.config = {0: {'color': 'Yellow', 'RGB': (255, 184, 8)},
                       1: {'color': 'Green', 'RGB': (11, 136, 80)},
                       2: {'color': 'Blue', 'RGB': (34, 133, 226)},
                       3: {'color': 'Red', 'RGB': (240, 17, 12)}
                       }

    def event_wait_space(self, plane_now):
        '''
        :describe: Wait for the player to shake the dice, and move accordingly.
        :param plane_now type:int between 0~3
        :return:
        '''
        global n, text1
        text1 = Others.font.render("Press Space To Shake The Dice", True, (0, 0, 0))
        self.show.refresh_screen()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    n = random.randint(1, 6)
                    text = Others.font.render(str(n), True, (0, 0, 0))  # shows the number of rolled points
                    self.checkerboard.screen.fill((255, 255, 255))
                    self.checkerboard.screen.blit(text, (850, 150))
                    text1 = Others.font.render('{} plane ready to take off'.format(self.config[plane_now]['color']),
                                               True,
                                               self.config[plane_now]['RGB'])
                    self.show.refresh_screen()
                    waiting = False

    def event_move(self, x, y=0):
        '''
        :describe: Event handling, such as player shaker,plane movement, collision, same-color jump, etc.
        :param x int:0~3 for user
        :param y int:0~3 for plane
        :return:
        '''
        if Others.players[x][y].win:
            num = 1
            return Event.event_move(x, num - 1)
        else:
            Others.players[x][y].direction = True  # Set the direction (for the last straight path)
            if not Others.players[x][y].fly:
                Others.players[x][y].position = Others.inital_pos[x]
                Others.players[x][y].fly = True
            for i in range(n):  # Set initial position
                if Others.players[x][y].position == Others.inital_pos[Others.players[x][y].type - 1]:
                    Others.players[x][y].position = Others.begin_pos[Others.players[x][y].type - 1]
                    self.show.refresh_screen()
                else:
                    Others.players[x][y].move()
                    self.show.refresh_screen()

            if not Others.players[x][y].fina and self.checkerboard.fly_path[Others.players[x][y].position][2] == \
                    Others.players[x][y].type:  # Jump or not
                for i in range(self.checkerboard.fly_path[Others.players[x][y].position][3]):
                    Others.players[x][y].move()
                    self.show.refresh_screen()

            for user in range(4):  # Whether it hit another plane
                for plane in range(4):
                    if user != x and Others.players[user][plane].position == Others.players[x][y].position:
                        Others.players[user][plane].position = Others.players_init_pos[user][plane]
                        Others.players[user][plane].fly = False
                        Others.players[user][plane].fina = False
                        self.show.refresh_screen()

            if Others.players[x][y].position == Others.players[x][y].list2[x]:  # Whether to fly to destination
                Others.players[x][y].position = Others.players_score_pos[x][y]
                Others.players[x][y].win = True
                self.show.refresh_screen()

    def __str__(self):
        return 'Event handling, such as player shaker,plane movement, collision, same-color jump, etc.'


class Show:

    def __init__(self, checkerboard):
        '''
        :describe:Bind to other class
        :param checkerboard:instannce of Checkerboard
        :return:self instance
        '''
        self.checkerboard = checkerboard

    def refresh_screen(self):
        '''
        :describe:Refresh mask to form overanimation.
        :return: None
        '''
        self.checkerboard.screen.blit(self.checkerboard.bgimg, (0, 0))
        self.checkerboard.screen.blit(Others.text1, (750, 50))
        self.checkerboard.screen.blit(Others.text_color[0], (750, 250))
        self.checkerboard.screen.blit(Others.text_color[1], (750, 300))
        self.checkerboard.screen.blit(Others.text_color[2], (750, 350))
        self.checkerboard.screen.blit(Others.text_color[3], (750, 400))
        for i in range(4):
            self.checkerboard.screen.blit(Others.yellow[i].img,
                                          (self.checkerboard.fly_path[Others.yellow[i].position][0],
                                           self.checkerboard.fly_path[Others.yellow[i].position][1]))
            self.checkerboard.screen.blit(Others.green[i].img,
                                          (self.checkerboard.fly_path[Others.green[i].position][0],
                                           self.checkerboard.fly_path[Others.green[i].position][1]))
            self.checkerboard.screen.blit(Others.blue[i].img,
                                          (self.checkerboard.fly_path[Others.blue[i].position][0],
                                           self.checkerboard.fly_path[Others.blue[i].position][1]))
            self.checkerboard.screen.blit(Others.red[i].img,
                                          (self.checkerboard.fly_path[Others.red[i].position][0],
                                           self.checkerboard.fly_path[Others.red[i].position][1]))

        pygame.display.update()
        time.sleep(0.5)
    def __str__(self):
        return 'Refresh mask to form overanimation'
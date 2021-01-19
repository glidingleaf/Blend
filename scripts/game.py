import pygame 



class Game():

    def __init__(self):

        pygame.init()
        self.running = True
        self.playing = False
        
        self.COLOR_BG = (99,155,255)
        self.FRAMERATE = 60
        self.UP_KEY = False
        self.DONW_KEY = False
        self.LEFT_KEY = False
        self.RIGHT_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False

        self.GAMEWINDOW_W, self.GAMEWINDOW_H = 480, 270
    

        self.gamescreen = pygame.Surface((self.GAMEWINDOW_W,self.GAMEWINDOW_H))
        self.window = pygame.display.set_mode((self.GAMEWINDOW_W,self.GAMEWINDOW_H))
        self.clock = pygame.time.Clock()



    def game_loop(self):

        while self.playing:
            
            self.check_events()

            if self.START_KEY == True:

                self.playing = False


            self.gamescreen.fill(self.COLOR_BG)
            self.window.blit(self.gamescreen,(0,0))
            pygame.display.update()
            self.reset_keys()
            
            self.clock.tick(self.FRAMERATE)




    def check_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False

            if event.type == pygame.K_RETURN:
                self.START_KEY = True

            if event.type == pygame.K_UP:
                self.START_KEY = True

            if event.type == pygame.K_DOWN:
                self.START_KEY = True

            if event.type == pygame.K_RIGHT:
                self.START_KEY = True

            if event.type == pygame.K_LEFT:
                self.START_KEY = True

            if event.type == pygame.K_BACKSPACE:
                self.START_KEY = True


    def reset_keys(self):
        
        self.UP_KEY = False
        self.DONW_KEY = False
        self.LEFT_KEY = False
        self.RIGHT_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False


        
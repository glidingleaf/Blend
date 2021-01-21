import pygame 
from .map import Map
import os



class Game():

    def __init__(self):

        pygame.init()
        self.running = True
        self.playing = False
        
        self.COLOR_BG = (99,155,255)
        self.FRAMERATE = 60

        
        # input keys

        self.UP_KEY = False
        self.DONW_KEY = False
        self.LEFT_KEY = False
        self.RIGHT_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False

        self.GAMEWINDOW_W, self.GAMEWINDOW_H = 512, 288
        self.A_GAMEWINDOW_W, self.A_GAMEWINDOW_H = 512*4, 288*4
    

        self.gamescreen = pygame.Surface((self.GAMEWINDOW_W,self.GAMEWINDOW_H))
        self.window = pygame.display.set_mode((self.A_GAMEWINDOW_W,self.A_GAMEWINDOW_H))
        self.clock = pygame.time.Clock()

        self.level = Map("./assets/maps/world_test2.tmx")


    def game_loop(self):

        while self.playing:
            
            self.check_events()

            if self.START_KEY == True:

                self.playing = False


            self.gamescreen.fill(self.COLOR_BG)
            self.gamescreen = self.level.drawmap(self.gamescreen)  # testing maps

            scaled_surface = pygame.transform.scale(self.gamescreen,(self.A_GAMEWINDOW_W,self.A_GAMEWINDOW_H))
            self.window.blit(scaled_surface,(0,0))

            #self.window.blit(self.gamescreen,(0,0)) ---> non scaled blit


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


        
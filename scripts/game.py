import pygame 
from .map import Map
import os
from .player import Player




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
        self.A_GAMEWINDOW_W, self.A_GAMEWINDOW_H = int(512*3), int(288*3)
    

        self.gamescreen = pygame.Surface((self.GAMEWINDOW_W,self.GAMEWINDOW_H))
        self.window = pygame.display.set_mode((self.A_GAMEWINDOW_W,self.A_GAMEWINDOW_H))
        self.clock = pygame.time.Clock()

        self.level = Map("./assets/maps/world_test2.tmx")

        self.p = Player("assets/images/player/player.png")


    def game_loop(self):

        while self.playing:
            
        #    self.p.reset_keys()
            self.check_events()

            if self.START_KEY == True:
                self.playing = False


            self.gamescreen.fill(self.COLOR_BG)
            self.gamescreen = self.level.drawmap(self.gamescreen)  # testing maps
        
            # Player Render
            player_with_world= self.p.update(self.gamescreen, self.level.tile_rects) 
            scaled_surface = pygame.transform.scale(player_with_world,(self.A_GAMEWINDOW_W,self.A_GAMEWINDOW_H))                   

            # Window Render
            self.window.blit(scaled_surface,(0,0))          

            pygame.display.update()            
            self.clock.tick(self.FRAMERATE)


    #  Check_ events is not yet completed 


    def check_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    self.p.START_KEY = True

                if event.key == pygame.K_UP:
                    self.p.UP_KEY = True

                if event.key == pygame.K_DOWN:
                    self.p.DOWN_KEY = True

                if event.key == pygame.K_RIGHT:
                    self.p.RIGHT_KEY = True

                if event.key == pygame.K_LEFT:
                    self.p.LEFT_KEY = True

                if event.key == pygame.K_BACKSPACE:
                    self.p.BACK_KEY = True


            if event.type == pygame.KEYUP:

                if event.key == pygame.K_RIGHT:
                    self.p.RIGHT_KEY = False

                if event.key == pygame.K_LEFT:
                    self.p.LEFT_KEY = False





    
        


import pygame
from .map import Map
import os
from .player import Player
from .camera import Camera
import particles


class Game():


    def __init__(self):

        
        pygame.init()
        
        self.font = pygame.font.SysFont("Arial", 18)
        self.running = True
        self.playing = False

        # self.COLOR_BG = (99, 155, 255)
        self.COLOR_BG =(160,78,83)
        self.FRAMERATE = 60

        # input keys

        self.UP_KEY = False
        self.DOWN_KEY = False
        self.LEFT_KEY = False
        self.RIGHT_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False

        self.GAMEWINDOW_W, self.GAMEWINDOW_H = 512, 288
        self.A_GAMEWINDOW_W, self.A_GAMEWINDOW_H = int(512*3), int(288*3)
        self.WINDOW_SIZE = (self.A_GAMEWINDOW_W, self.A_GAMEWINDOW_H)

        self.gamescreen = pygame.Surface(
            (self.GAMEWINDOW_W, self.GAMEWINDOW_H))
        self.window = pygame.display.set_mode(
            (self.A_GAMEWINDOW_W, self.A_GAMEWINDOW_H))
        self.clock = pygame.time.Clock()

        self.level = Map("./assets/maps/NewWorld.tmx", self.WINDOW_SIZE)
        os.chdir("../")

        print(os.getcwd())

        self.bg = pygame.image.load("./images/background/bg.png").convert()


        os.chdir("./images/player")
        self.p = Player(os.getcwd())

        self.camera = Camera(self.p, self.GAMEWINDOW_W, self.GAMEWINDOW_H)

        

        

    def game_loop(self):

        while self.playing:

            #    self.p.reset_keys()
            self.check_events()

            if self.START_KEY == True:
                self.playing = False

            # player update
            self.p.update(self.level.tile_rects)

            # camera update
            self.camera.update(self.p)

            # screen fill
            self.gamescreen.fill(self.COLOR_BG)

            # background render

            self.gamescreen.blit(self.bg, (0, -150))
            
            # self.gamescreen = self.level.render_background(self.gamescreen,self.camera.offset)


            # Map render
            self.gamescreen = self.level.drawmap(
                self.gamescreen, self.camera.offset,self.p.pos)  # testing maps


            # Player Render
            player_with_world = self.p.render(
                self.gamescreen, self.camera.offset)
            scaled_surface = pygame.transform.scale(
                player_with_world, (self.A_GAMEWINDOW_W, self.A_GAMEWINDOW_H))

            # Window Render
            self.window.blit(scaled_surface, (0, 0))

            #framerate display 
            self.window.blit(self.update_fps(), (10, 0))

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

                if event.key == pygame.K_q:
                    self.camera.C += -100

                if event.key == pygame.K_e:
                    self.camera.C += 100

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_RIGHT:
                    self.p.RIGHT_KEY = False

                if event.key == pygame.K_LEFT:
                    self.p.LEFT_KEY = False

                if event.key == pygame.K_UP:
                    self.p.UP_KEY = False

    def update_fps(self):
        fps = str(int(self.clock.get_fps()))
        fps_text = self.font.render(fps, 1, pygame.Color("coral"))
        return fps_text

import pygame
from .map import Map
import os
from .player import Player
from .camera import Camera
import particles
import shared
import time
from .vfx import Mask

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

        self.GAMEWINDOW_W, self.GAMEWINDOW_H = shared.GAMEWINDOW_W, shared.GAMEWINDOW_H
        self.A_GAMEWINDOW_W, self.A_GAMEWINDOW_H = shared.A_GAMEWINDOW_W, shared.A_GAMEWINDOW_H

        self.WINDOW_SIZE = (self.A_GAMEWINDOW_W, self.A_GAMEWINDOW_H)

        self.gamescreen = pygame.Surface((self.GAMEWINDOW_W, self.GAMEWINDOW_H))
        self.window = pygame.display.set_mode((self.A_GAMEWINDOW_W, self.A_GAMEWINDOW_H))
        pygame.display.set_caption("Blend")

        self.clock = pygame.time.Clock()

        self.level = Map("./assets/maps/NewWorld.tmx", self.WINDOW_SIZE)
        os.chdir("../")

        print(os.getcwd())

        self.bg = pygame.image.load("./images/background/bg.png").convert()
        
        self.mask = Mask("./images/lighting")


        os.chdir("./images/player")
        self.p = Player(os.getcwd())

        self.camera = Camera(self.p, self.GAMEWINDOW_W, self.GAMEWINDOW_H)

        self.prev_time = time.time()
        self.cur_time = 0
        self.dt = 0
        self.LOCKED_FPS = 30
        self.eff_dt = 0

    def timedamper(self):

        self.cur_time = time.time()
        self.dt = self.cur_time - self.prev_time
        self.prev_time = self.cur_time

        self.eff_dt = self.dt * self.LOCKED_FPS
        

        

    def game_loop(self):

        while self.playing:

            # self.timedamper()

            # self.p.reset_keys()
            # self.check_events()

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
            self.gamescreen.fill((0,0,0))
            
            # self.gamescreen = self.level.render_background(self.gamescreen,self.camera.offset)


            # Map render
            self.gamescreen = self.level.drawmap(
                self.gamescreen, self.camera.offset,self.p.pos,self.camera.box)  # testing maps

            # self.gamescreen = self.level.getmapsurface(self.gamescreen,self.camera.box)
            

            # Player Render
            player_with_world = self.p.render(
                self.gamescreen, self.camera.offset)

            # self.mask.apply_darkmask(player_with_world)
            # self.mask.apply_lightmask(player_with_world, self.p.centerpos - self.camera.offset)

            #surface scaling
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

                if event.key == pygame.K_SPACE:
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

                if event.key == pygame.K_SPACE:
                    self.p.UP_KEY = False

    def update_fps(self):
        fps = str(int(self.clock.get_fps()))
        fps_text = self.font.render(fps, 1, pygame.Color("coral"))
        return fps_text
